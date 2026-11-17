# Regulatory Frameworks — Product Classification & Guardrails

Complete this before any search. The product class sets what you can and cannot claim; it is the difference between MLR-ready claims and unusable ones.

## The 5-question classifier

1. **Market?** US · EU · Canada · UK · Australia · APAC · Multi-market
2. **Labeled/intended use?** e.g., relieve cold symptoms · support immunity · improve sleep · manage glucose · heal wound · reduce pain
3. **How regulated?** FDA OTC Drug · FDA Supplement · OTC Homeopathic · Health Canada NHP · EFSA Food Supplement · FDA Device · Rx (if unknown, use Q4–Q5 + routing table)
4. **How consumed/used?** Oral (tablet/capsule/gummy/liquid/lozenge) · topical · inhaled · injectable · implant · wearable · diagnostic
5. **Claim type?** Disease (treat/cure/diagnose/prevent/mitigate) vs. wellness (support/maintain/promote/help)

## Routing table

| If the product is… | …and the claim is… | → Product Type | → Regulatory Body |
|---|---|---|---|
| Oral; vitamin/mineral/herb/botanical | Wellness (structure/function), US | Dietary Supplement | FDA (DSHEA 1994) |
| Oral; HPUS homeopathic dilution | Symptom relief (OTC-style), US | OTC Homeopathic Drug | FDA (CPG 400.400 + 2019 guidance) |
| Oral; OTC monograph active | Disease treat/relieve/prevent, US | OTC Drug (Monograph/NDA) | FDA OTC Monograph |
| Oral/topical; drug outside a monograph | Disease treat/prevent/diagnose, US | Rx Drug (NDA/sNDA) | FDA CDER |
| Oral; vitamin/mineral/herb/botanical | Wellness/nutrient content, EU/UK | Food Supplement | EFSA / FSA |
| Oral; herb/vitamin/traditional/homeopathic | Health maintenance/traditional, Canada | Natural Health Product | Health Canada (NHPD) |
| Topical; cream/gel/serum, no drug claim | Cosmetic aesthetics, US | Cosmetic (21 CFR 700) | FDA (post-market) |
| Topical; anti-itch/SPF/antifungal/acne active | Disease/condition treatment, US | OTC Drug (Topical Monograph) | FDA OTC Monograph |
| Physical device | Diagnose/monitor/treat, US | Medical Device | FDA CDRH (510k/PMA/De Novo) |
| Food/beverage + functional ingredient | Authorized disease-risk reduction, US | Functional Food + Health Claim | FDA (21 CFR 101.14) |
| Food/beverage + functional ingredient | Qualified health claim, US | Functional Food + QHC | FDA (enforcement discretion) |

## Required disclaimers

| Product type | Disclaimer |
|---|---|
| US Dietary Supplement | This statement has not been evaluated by the FDA. This product is not intended to diagnose, treat, cure, or prevent any disease. |
| US OTC Homeopathic | Structure-function disclaimer + ✢ footnote on each labeled indication. |
| US OTC Drug (Monograph) | Drug Facts; "Uses" verbatim from monograph. Off-label DTC needs legal review. |
| EU Food Supplement | This is a food supplement and should not be used as a substitute for a varied and balanced diet. |
| Canada NHP | Licensed claim language verbatim; NPN on label; "Does not replace a healthy diet and lifestyle" where licensed. |
| US Qualified Health Claim | Although there is scientific evidence supporting this claim, the evidence is not conclusive. |
| US Medical Device | Cleared intended use from 510(k)/PMA. No drug-like efficacy claims. "Rx only" if applicable. |

## Guardrails by product type

**US Dietary Supplement (DSHEA):** Permitted — structure-function ("supports/helps maintain/promotes") with 30-day FDA notification; nutrient-content claims. Prohibited — any disease claim; treat/cure/prevent/diagnose; implied disease claims via symptom-specific language. Caution — "clinically studied" OK with a study; "clinically proven" implies disease treatment (avoid). Certifications (USP/NSF) must not imply FDA approval.

**US OTC Homeopathic (CPG 400.400 + 2019 guidance):** Permitted — HPUS-consistent labeled indications; traditional homeopathic use; temporary symptom relief; ✢ footnote. Prohibited — permanent cure; indications beyond HPUS at the dilution; oncology/cardiovascular/serious chronic disease claims; implying FDA approval. Required — HPUS ingredient ID with potency (1X/2X/3X). Auto-elevate to SAB review. Frame mechanism as "proposed"/"traditional," never established pharmacology.

**US OTC Drug (Monograph):** Permitted — only monograph "Uses" language; Drug Facts format. Prohibited — off-monograph indications without NDA/sNDA; structure-function on Drug Facts; comparative superiority without head-to-head data. Rx-to-OTC switch copy must stay within approved indication.

**EU Food Supplement / Functional Food (Reg. 1924/2006):** Permitted — only Union-list authorized health claims (verbatim); nutrient-content claims. Prohibited — unauthorized disease-risk-reduction; medical treatment/diagnosis; child-targeted claims unless authorized.

**Canada NHP (2004):** Permitted — licensed claim language verbatim; traditional-use claims with evidence + ✢. Required — NPN; licensed dose; bilingual (EN/FR).

**US Medical Device (CDRH):** Permitted — cleared intended use; performance data from the cleared submission; "FDA cleared" (510k). Prohibited — off-label promotion; drug-like efficacy claims; "FDA approved" for 510(k).

## Regulatory Identity Block — template

> Product: [name] · Class: [type] · Body: [regulator] · Permitted claim types: [...] · Prohibited: [...] · Required disclaimer: "[...]" · Population restrictions: [...]
