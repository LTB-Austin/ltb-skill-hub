#!/usr/bin/env python3
"""
score_runs.py — compute the LLM-pass metrics from runs.csv (schema in references/llm-capture-schema.md).

Usage
  python score_runs.py --runs runs.csv --client "Centrum" --out llm_scores [--tiers ingredient_tiers.csv]

Outputs (in --out)
  metrics_by_model.csv   client metrics per model x prompt_type (+ ALL rows)
  brand_table.csv        presence / share / first-mention / mean position / sentiment for every brand, per model and ALL
  attribute_map.csv      attribute frequency by brand x variable x polarity, with verbatim samples
  source_map.csv         domain frequency by model, with brand association (positive/negative client runs)
  stability.csv          consistency index (mean pairwise Jaccard of named sets) and presence 95% CI per prompt x model
  convergence.csv        (only with --tiers) attributes cited by models matched to rubric-pass tiers
  summary.txt            N, run counts, version strata, headline numbers

Nothing here is a ranking. Every number is a sample statistic across N runs on the dates logged.
"""
import argparse
import csv
import math
import os
import re
from collections import defaultdict, Counter
from itertools import combinations


def split_pipe(s):
    return [x.strip() for x in (s or "").split("|") if x.strip()]


def brand_of(product):
    return product.split("–")[0].split("-")[0].strip() if product else ""


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    r = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (max(0.0, (c - r) / d), min(1.0, (c + r) / d))


def parse_attr(entry):
    # "Brand – SKU :: variable :: polarity :: "verbatim""
    parts = [p.strip() for p in entry.split("::")]
    if len(parts) < 3:
        return None
    prod, var, pol = parts[0], parts[1], parts[2]
    quote = parts[3].strip('" ') if len(parts) > 3 else ""
    return brand_of(prod), prod, var, pol, quote


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", required=True)
    ap.add_argument("--client", required=True, help="client brand name as it appears in products_named")
    ap.add_argument("--out", default="llm_scores")
    ap.add_argument("--tiers", default=None, help="ingredient_tiers.csv from the rubric pass for the convergence test")
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)
    client = args.client.strip().lower()

    with open(args.runs, newline="", encoding="utf-8") as f:
        runs = list(csv.DictReader(f))
    if not runs:
        raise SystemExit("no runs")

    for r in runs:
        r["_products"] = split_pipe(r.get("products_named"))
        r["_brands"] = [brand_of(p).lower() for p in r["_products"]]
        r["_client"] = client in r["_brands"] or str(r.get("client_named", "")).strip().upper() == "Y"
        r["_sources"] = [d.lower() for d in split_pipe(r.get("sources"))]
        r["_attrs"] = [a for a in (parse_attr(e) for e in split_pipe(r.get("attributes"))) if a]

    models = sorted({r["model"] for r in runs})
    ptypes = sorted({r.get("prompt_type", "") for r in runs})

    # ---- client metrics by model x prompt_type ----
    rows = []
    for m in models + ["ALL"]:
        for pt in ptypes + ["ALL"]:
            sub = [r for r in runs if (m == "ALL" or r["model"] == m) and (pt == "ALL" or r.get("prompt_type") == pt)]
            n = len(sub)
            if n == 0:
                continue
            present = [r for r in sub if r["_client"]]
            k = len(present)
            lo, hi = wilson(k, n)
            all_mentions = sum(len(r["_brands"]) for r in sub)
            client_mentions = sum(r["_brands"].count(client) for r in sub)
            first = sum(1 for r in sub if r["_brands"] and r["_brands"][0] == client)
            positions = [int(r["client_position"]) for r in present if str(r.get("client_position", "")).strip().isdigit()]
            sent = Counter(r.get("client_sentiment", "").strip() for r in present if r.get("client_sentiment", "").strip())
            neg = sum(1 for r in sub if str(r.get("client_negative_mention", "")).strip().upper() == "Y")
            rows.append({
                "model": m, "prompt_type": pt, "n_runs": n,
                "presence_rate_pct": round(100 * k / n, 1),
                "presence_ci95_pct": f"{round(100*lo)}–{round(100*hi)}",
                "share_of_recommendation_pct": round(100 * client_mentions / all_mentions, 1) if all_mentions else 0.0,
                "first_mention_rate_pct": round(100 * first / n, 1),
                "mean_position_when_named": round(sum(positions) / len(positions), 2) if positions else "",
                "pos1_pct": round(100 * sum(1 for p in positions if p == 1) / len(positions), 1) if positions else "",
                "pos2_3_pct": round(100 * sum(1 for p in positions if p in (2, 3)) / len(positions), 1) if positions else "",
                "pos4plus_pct": round(100 * sum(1 for p in positions if p >= 4) / len(positions), 1) if positions else "",
                "sent_recommended_pct": round(100 * sent.get("Recommended", 0) / k, 1) if k else "",
                "sent_acceptable_pct": round(100 * sent.get("Acceptable", 0) / k, 1) if k else "",
                "sent_caveated_pct": round(100 * sent.get("Caveated", 0) / k, 1) if k else "",
                "sent_not_recommended_pct": round(100 * sent.get("Not recommended", 0) / k, 1) if k else "",
                "negative_mention_rate_pct": round(100 * neg / n, 1),
            })
    write(os.path.join(args.out, "metrics_by_model.csv"), rows)

    # ---- brand table ----
    brows = []
    for m in models + ["ALL"]:
        sub = [r for r in runs if m == "ALL" or r["model"] == m]
        n = len(sub)
        all_mentions = sum(len(r["_brands"]) for r in sub)
        brands = Counter(b for r in sub for b in set(r["_brands"]))
        for b, k in brands.most_common():
            mentions = sum(r["_brands"].count(b) for r in sub)
            first = sum(1 for r in sub if r["_brands"] and r["_brands"][0] == b)
            poss = [r["_brands"].index(b) + 1 for r in sub if b in r["_brands"]]
            brows.append({
                "model": m, "brand": b, "n_runs": n,
                "presence_rate_pct": round(100 * k / n, 1),
                "share_of_recommendation_pct": round(100 * mentions / all_mentions, 1) if all_mentions else 0.0,
                "first_mention_rate_pct": round(100 * first / n, 1),
                "mean_position_when_named": round(sum(poss) / len(poss), 2) if poss else "",
                "is_client": "Y" if b == client else "N",
            })
    write(os.path.join(args.out, "brand_table.csv"), brows)

    # ---- attribute map ----
    amap = defaultdict(lambda: {"count": 0, "runs": set(), "quotes": []})
    for r in runs:
        for b, prod, var, pol, quote in r["_attrs"]:
            key = (r["model"], b.lower(), var, pol)
            amap[key]["count"] += 1
            amap[key]["runs"].add(r["run_id"])
            if quote and len(amap[key]["quotes"]) < 5 and quote not in amap[key]["quotes"]:
                amap[key]["quotes"].append(quote)
    arows = []
    n_by_model = Counter(r["model"] for r in runs)
    for (m, b, var, pol), v in amap.items():
        arows.append({"model": m, "brand": b, "variable": var, "polarity": pol,
                      "n_runs_citing": len(v["runs"]), "pct_of_model_runs": round(100 * len(v["runs"]) / n_by_model[m], 1),
                      "n_mentions": v["count"], "is_client": "Y" if b == client else "N",
                      "verbatim_samples": " | ".join(v["quotes"])})
    # pooled ALL rows
    pooled = defaultdict(lambda: {"runs": set(), "quotes": []})
    for r in runs:
        for b, prod, var, pol, quote in r["_attrs"]:
            k = (b.lower(), var, pol)
            pooled[k]["runs"].add(r["run_id"])
            if quote and len(pooled[k]["quotes"]) < 5 and quote not in pooled[k]["quotes"]:
                pooled[k]["quotes"].append(quote)
    for (b, var, pol), v in pooled.items():
        arows.append({"model": "ALL", "brand": b, "variable": var, "polarity": pol,
                      "n_runs_citing": len(v["runs"]), "pct_of_model_runs": round(100 * len(v["runs"]) / len(runs), 1),
                      "n_mentions": "", "is_client": "Y" if b == client else "N",
                      "verbatim_samples": " | ".join(v["quotes"])})
    arows.sort(key=lambda x: (x["model"], x["is_client"] != "Y", -x["n_runs_citing"]))
    write(os.path.join(args.out, "attribute_map.csv"), arows)

    # variable split
    vs = Counter((r["model"], var) for r in runs for _, _, var, _, _ in r["_attrs"])
    tot = Counter(r["model"] for r in runs for _ in r["_attrs"])
    vrows = [{"model": m, "variable": var, "share_of_cited_attributes_pct": round(100 * c / tot[m], 1)}
             for (m, var), c in sorted(vs.items())]
    write(os.path.join(args.out, "attribute_variable_split.csv"), vrows)

    # ---- source map ----
    srows = []
    for m in models + ["ALL"]:
        sub = [r for r in runs if m == "ALL" or r["model"] == m]
        n = len(sub)
        cited = sum(1 for r in sub if r["_sources"])
        dom = Counter(d for r in sub for d in set(r["_sources"]))
        for d, k in dom.most_common():
            pos_runs = sum(1 for r in sub if d in r["_sources"] and r["_client"] and r.get("client_sentiment") in ("Recommended", "Acceptable"))
            neg_runs = sum(1 for r in sub if d in r["_sources"] and (r.get("client_sentiment") in ("Caveated", "Not recommended") or str(r.get("client_negative_mention", "")).upper() == "Y"))
            srows.append({"model": m, "domain": d, "n_runs_citing": k, "pct_of_runs": round(100 * k / n, 1),
                          "source_class": classify_domain(d),
                          "runs_with_client_positive": pos_runs, "runs_with_client_negative": neg_runs,
                          "citation_presence_pct_for_model": round(100 * cited / n, 1)})
    write(os.path.join(args.out, "source_map.csv"), srows)

    # ---- stability ----
    strows = []
    groups = defaultdict(list)
    for r in runs:
        groups[(r["model"], r["prompt_id"])].append(r)
    for (m, pid), sub in sorted(groups.items()):
        sets = [set(r["_products"]) for r in sub]
        jac = []
        for a, b in combinations(sets, 2):
            u = a | b
            jac.append(len(a & b) / len(u) if u else 1.0)
        k = sum(1 for r in sub if r["_client"])
        lo, hi = wilson(k, len(sub))
        versions = sorted({r.get("version", "") for r in sub})
        strows.append({"model": m, "prompt_id": pid, "n_runs": len(sub),
                       "consistency_index": round(sum(jac) / len(jac), 2) if jac else "",
                       "client_presence_pct": round(100 * k / len(sub), 1),
                       "presence_ci95_pct": f"{round(100*lo)}–{round(100*hi)}",
                       "distinct_products_named": len(set().union(*sets)) if sets else 0,
                       "versions_seen": " | ".join(versions), "version_change": "Y" if len(versions) > 1 else "N"})
    write(os.path.join(args.out, "stability.csv"), strows)

    # ---- convergence ----
    if args.tiers:
        with open(args.tiers, newline="", encoding="utf-8") as f:
            tiers = list(csv.DictReader(f))
        # key on ingredient alone and on "ingredient form"; longest match wins so forms beat bare names
        tier_by_key = {}
        for t in tiers:
            k = t["ingredient_key"].strip().lower()
            fm = (t.get("form") or "").strip().lower()
            if fm:
                tier_by_key[f"{k} {fm}"] = t.get("tier", "")
                tier_by_key[f"{fm} {k}"] = t.get("tier", "")
            tier_by_key.setdefault(k, t.get("tier", ""))
        crows = []
        seen = set()
        for r in runs:
            for b, prod, var, pol, quote in r["_attrs"]:
                if var not in ("Ingredient", "Dose", "Form", "Testing"):
                    cls, tier = "Not testable", ""
                else:
                    tier, matched = "", ""
                    q = re.sub(r"\s+", " ", quote.lower().replace("&", " and "))
                    for key in sorted(tier_by_key, key=len, reverse=True):
                        if key and key in q:
                            tier, matched = tier_by_key[key], key
                            break
                    if not tier:
                        cls = "Unmatched (check by hand)"
                    elif (pol == "-" and tier == "Drags") or (pol == "+" and tier == "Helps"):
                        cls = "Converges"
                    elif tier == "Mixed":
                        cls = "Diverges (rubric mixed)"
                    else:
                        cls = "Diverges"
                sig = (b.lower(), var, pol, quote.lower())
                if sig in seen:
                    continue
                seen.add(sig)
                crows.append({"brand": b, "variable": var, "model_polarity": pol, "verbatim": quote,
                              "rubric_tier": tier, "classification": cls, "analyst_note": ""})
        crows.sort(key=lambda x: (x["classification"], x["brand"]))
        write(os.path.join(args.out, "convergence.csv"), crows)

    # ---- summary ----
    with open(os.path.join(args.out, "summary.txt"), "w", encoding="utf-8") as f:
        f.write(f"runs: {len(runs)} | models: {', '.join(models)} | prompts: {len({r['prompt_id'] for r in runs})}\n")
        per = Counter((r["model"], r["prompt_id"]) for r in runs)
        f.write(f"runs per prompt x model: min {min(per.values())}, max {max(per.values())}\n")
        dates = sorted({r["date"] for r in runs})
        f.write(f"run window: {dates[0]} to {dates[-1]}\n")
        for m in models:
            vers = sorted({r.get("version", "") for r in runs if r["model"] == m})
            f.write(f"{m} versions seen: {' | '.join(vers)}\n")
        allrow = [x for x in rows if x["model"] == "ALL" and x["prompt_type"] == "ALL"][0]
        f.write(f"\nclient '{args.client}' overall presence: {allrow['presence_rate_pct']}% (CI {allrow['presence_ci95_pct']}) over {allrow['n_runs']} runs; "
                f"first-mention {allrow['first_mention_rate_pct']}%; share of recommendation {allrow['share_of_recommendation_pct']}%; "
                f"negative-mention {allrow['negative_mention_rate_pct']}%\n")
        p1 = [x for x in rows if x["model"] == "ALL" and x["prompt_type"] == "P1"]
        if p1:
            f.write(f"client P1 (unprompted) presence: {p1[0]['presence_rate_pct']}% (CI {p1[0]['presence_ci95_pct']}) over {p1[0]['n_runs']} runs\n")
        f.write("\nReminder: sampled, not scored. Report N and dates next to every number. Never present as a ranking.\n")
    print(open(os.path.join(args.out, "summary.txt")).read())


def classify_domain(d):
    d = d.lower()
    if any(x in d for x in ["nih.gov", "cdc.gov", "mayoclinic", "harvard", "clevelandclinic", ".edu", "usda", "fda.gov", "nhs.uk", "who.int"]):
        return "institutional"
    if any(x in d for x in ["amazon", "target", "walmart", "cvs", "walgreens", "costco", "iherb", "gnc", "vitacost"]):
        return "retail"
    if any(x in d for x in ["supp.co", "labdoor", "consumerlab", "examine.com", "illuminatelabs"]):
        return "scoring/review platform"
    if any(x in d for x in ["youtube", "tiktok", "reddit", "instagram", "facebook", "quora"]):
        return "social/video"
    if any(x in d for x in ["healthline", "verywell", "medicalnewstoday", "everydayhealth", "webmd", "forbes", "nytimes", "wirecutter", "cnet", "goodrx", "menshealth", "womenshealth", "prevention", "eatingwell"]):
        return "editorial"
    return "brand-owned/other"


def write(path, rows):
    if not rows:
        open(path, "w").close()
        return
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    main()
