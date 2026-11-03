#!/usr/bin/env python3
"""
tier_ingredients.py — Tier ingredients by how product scores move with them.

Inputs
  --ingredients  CSV in the "Ingredient Long" layout (one row per ingredient per product).
                 Required columns: product_id, overall_score, ingredient_type, ingredient_name
                 Optional: form, amount, unit, ingredient_key, flagged, platform_note_verbatim
  --products     (optional) CSV in the "Product Capture" layout, used only for the product count
                 and score distribution summary.

Outputs (written next to --out, default ./tier_output/)
  ingredient_tiers.csv   one row per ingredient_key (+ form when --by-form)
  dose_bands.csv         actives only: score by dose band (per ingredient, tercile bands)
  summary.txt            population size, score quartile cut points, tier counts

Tiering logic (deliberately simple and explainable — the report must say how tiers were made):
  * Compare mean overall_score of products WITH the ingredient vs WITHOUT.
  * Compare prevalence in the top score quartile vs the bottom quartile.
  * Tier:
      Helps  — score_delta >= +threshold AND top-quartile prevalence > bottom-quartile prevalence
      Drags  — score_delta <= -threshold AND bottom-quartile prevalence > top-quartile prevalence
      Mixed  — anything else, or support too weak (n_with < min_n or n_without < min_n)
  * Support: strong (n_with >= 8 and |delta| >= 2*threshold), moderate (n_with >= min_n), weak otherwise.
  threshold defaults to 10% of the score scale range in the data (e.g. 1.0 on a 0–10 scale).

Usage
  python tier_ingredients.py --ingredients ingredient_long.csv --out tier_output --by-form
"""
import argparse
import csv
import os
import re
import statistics
from collections import defaultdict


def norm_key(name: str) -> str:
    s = name.strip().lower().replace("&", " and ")
    s = re.sub(r"\(.*?\)", "", s)          # drop parenthetical form text
    s = re.sub(r"\bas\b.*$", "", s)          # drop "as cholecalciferol" tails
    s = re.sub(r"[^a-z0-9+\- ]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def to_float(x):
    try:
        return float(str(x).strip())
    except Exception:
        return None


def quartiles(values):
    vs = sorted(values)
    n = len(vs)
    if n < 4:
        return vs[0], vs[-1]
    q1 = vs[int(0.25 * (n - 1))]
    q3 = vs[int(0.75 * (n - 1))]
    return q1, q3


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ingredients", required=True)
    ap.add_argument("--products", default=None)
    ap.add_argument("--out", default="tier_output")
    ap.add_argument("--by-form", action="store_true", help="key on ingredient + form, not ingredient alone")
    ap.add_argument("--min-n", type=int, default=4)
    ap.add_argument("--threshold", type=float, default=None, help="score delta threshold; default 10%% of observed range")
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)

    with open(args.ingredients, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise SystemExit("No rows in ingredients file.")

    # product -> score
    score_by_product = {}
    for r in rows:
        pid = r["product_id"].strip()
        sc = to_float(r.get("overall_score"))
        if sc is not None:
            score_by_product[pid] = sc
    products = sorted(score_by_product)
    scores = [score_by_product[p] for p in products]
    if len(products) < 8:
        print(f"WARNING: only {len(products)} scored products. Tiers will be weak; keep capturing.")

    lo, hi = min(scores), max(scores)
    threshold = args.threshold if args.threshold is not None else max(0.05, 0.10 * (hi - lo))
    q1, q3 = quartiles(scores)
    top_q = {p for p in products if score_by_product[p] >= q3}
    bot_q = {p for p in products if score_by_product[p] <= q1}

    # ingredient key -> set of products; also notes/flags
    have = defaultdict(set)
    itype = {}
    flagged = defaultdict(int)
    notes = defaultdict(set)
    doses = defaultdict(dict)  # key -> product -> amount

    for r in rows:
        pid = r["product_id"].strip()
        if pid not in score_by_product:
            continue
        key = (r.get("ingredient_key") or "").strip().lower() or norm_key(r["ingredient_name"])
        form = (r.get("form") or "").strip().lower()
        k = (key, form) if args.by_form else (key, "")
        have[k].add(pid)
        itype[k] = (r.get("ingredient_type") or "").strip().lower()
        if str(r.get("flagged", "")).strip().upper().startswith("Y"):
            flagged[k] += 1
        note = (r.get("platform_note_verbatim") or "").strip()
        if note:
            notes[k].add(note[:120])
        amt = to_float(r.get("amount"))
        if amt is not None and itype[k] == "active":
            doses[k][pid] = amt

    out_rows = []
    tier_counts = defaultdict(int)
    for k, pids in have.items():
        n_with = len(pids)
        without = [score_by_product[p] for p in products if p not in pids]
        with_ = [score_by_product[p] for p in pids]
        mean_with = statistics.mean(with_) if with_ else None
        mean_without = statistics.mean(without) if without else None
        delta = (mean_with - mean_without) if (mean_with is not None and mean_without is not None) else None
        prev = 100.0 * n_with / len(products)
        prev_top = 100.0 * len(pids & top_q) / max(1, len(top_q))
        prev_bot = 100.0 * len(pids & bot_q) / max(1, len(bot_q))

        if len(without) == 0:
            tier, support = "Mixed", "universal (in every product; no comparison possible)"
        elif delta is None or n_with < args.min_n or len(without) < args.min_n:
            tier, support = "Mixed", "weak"
        elif delta >= threshold and prev_top > prev_bot:
            tier = "Helps"
            support = "strong" if (n_with >= 8 and delta >= 2 * threshold) else "moderate"
        elif delta <= -threshold and prev_bot > prev_top:
            tier = "Drags"
            support = "strong" if (n_with >= 8 and -delta >= 2 * threshold) else "moderate"
        else:
            tier, support = "Mixed", ("moderate" if n_with >= args.min_n else "weak")
        tier_counts[tier] += 1

        out_rows.append({
            "ingredient_key": k[0],
            "form": k[1],
            "type": itype.get(k, ""),
            "n_products_with": n_with,
            "prevalence_pct": round(prev, 1),
            "prevalence_top_quartile_pct": round(prev_top, 1),
            "prevalence_bottom_quartile_pct": round(prev_bot, 1),
            "mean_score_with": round(mean_with, 2) if mean_with is not None else "",
            "mean_score_without": round(mean_without, 2) if mean_without is not None else "",
            "score_delta": round(delta, 2) if delta is not None else "",
            "tier": tier,
            "support": support,
            "platform_explicitly_flags": "Y" if flagged[k] else "N",
            "n_flagged": flagged[k],
            "agrees_with_platform": "",  # filled by the analyst after reading platform notes
            "platform_notes_sample": " | ".join(sorted(notes[k]))[:300],
            "confound_note": "",
        })

    out_rows.sort(key=lambda r: (r["tier"], -(abs(r["score_delta"]) if r["score_delta"] != "" else 0)))
    with open(os.path.join(args.out, "ingredient_tiers.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()))
        w.writeheader()
        w.writerows(out_rows)

    # dose bands: per active ingredient, split captured doses into terciles
    dose_rows = []
    for k, pmap in doses.items():
        if len(pmap) < 6:
            continue
        amts = sorted(pmap.values())
        t1 = amts[len(amts) // 3]
        t2 = amts[(2 * len(amts)) // 3]
        bands = {"low": [], "mid": [], "high": []}
        for pid, a in pmap.items():
            b = "low" if a < t1 else ("mid" if a < t2 else "high")
            bands[b].append(score_by_product[pid])
        for b, vals in bands.items():
            if vals:
                dose_rows.append({
                    "ingredient_key": k[0], "form": k[1], "dose_band": b,
                    "band_cut_low": {"low": amts[0], "mid": t1, "high": t2}[b],
                    "n_products": len(vals),
                    "mean_score": round(statistics.mean(vals), 2),
                    "median_score": round(statistics.median(vals), 2),
                })
    with open(os.path.join(args.out, "dose_bands.csv"), "w", newline="", encoding="utf-8") as f:
        fields = ["ingredient_key", "form", "dose_band", "band_cut_low", "n_products", "mean_score", "median_score"]
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(dose_rows)

    with open(os.path.join(args.out, "summary.txt"), "w", encoding="utf-8") as f:
        f.write(f"products scored: {len(products)}\n")
        f.write(f"score range: {lo} to {hi}; Q1 {q1}; Q3 {q3}; top-quartile n {len(top_q)}; bottom-quartile n {len(bot_q)}\n")
        f.write(f"delta threshold: {threshold:.3f}; min_n: {args.min_n}; keyed by form: {args.by_form}\n")
        f.write("tiers: " + ", ".join(f"{t} {c}" for t, c in sorted(tier_counts.items())) + "\n")
        f.write("ingredients analysed: %d\n" % len(out_rows))
        f.write("\nMethod statement for the report:\n")
        f.write("Each ingredient was compared on (a) the mean overall score of products containing it versus products that do not, "
                "and (b) its prevalence in the top score quartile versus the bottom quartile. An ingredient was tiered 'Helps' when "
                f"the score difference was at least +{threshold:.2f} and it was more prevalent among top-quartile products; 'Drags' when "
                f"the difference was at most -{threshold:.2f} and it was more prevalent among bottom-quartile products; otherwise 'Mixed'. "
                f"Ingredients present in fewer than {args.min_n} products were marked weak support. Co-occurrence confounds were reviewed by hand.\n")
    print(open(os.path.join(args.out, "summary.txt")).read())


if __name__ == "__main__":
    main()
