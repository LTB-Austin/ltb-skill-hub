# Evidence workbook schema — Rubric Pass

One workbook per project, `<Client>_Rubric_Pass_<YYYY-MM-DD>.xlsx`. Build with the xlsx skill. Freeze header rows; filter on every tab. Color finding direction: Helps = green, Mixed = amber, Drags = red.

## Tab 1 — Platform Inventory
| Platform | Criterion | What is published | Disclosed weighting | NOT disclosed | Source URL | Source date | Notes |

One row per criterion per platform. "NOT disclosed" is required text, never blank.

## Tab 2 — Category Set
| Role (Client / Competitor / Population) | Brand | Product | Audience segment (Adult / Men / Women / 50+ / Gummy …) | Closest client SKU match | Platform URL | Agreed with client (Y/N, date) |

## Tab 3 — Product Capture (wide, one row per product)
| product_id | role | brand | product | segment | format | serving_size | overall_score | score_scale | sub_1_label | sub_1 | sub_2_label | sub_2 | sub_3_label | sub_3 | sub_4_label | sub_4 | flags_verbatim | certifications | third_party_tested | price_per_serving | platform_data_date | capture_date | url | screenshot_score | screenshot_ingredients | gated_sections | notes |

Add sub_N columns as the platform requires; keep labels as shown on the page.

## Tab 4 — Ingredient Long (one row per ingredient per product)
| product_id | brand | product | overall_score | ingredient_type (active / inactive) | ingredient_name | form | amount | unit | pct_dv | platform_note_verbatim | flagged (Y/N) | flag_reason |

Normalize names in a separate `ingredient_key` column (lowercase, no salts duplicated: "vitamin d3 (cholecalciferol)" → key `vitamin d3`, form `cholecalciferol`). The tiering script keys on `ingredient_key` + `form`.

## Tab 5 — Ingredient Tiers (script output)
| ingredient_key | form | type | n_products_with | prevalence_pct | prevalence_top_quartile_pct | prevalence_bottom_quartile_pct | mean_score_with | mean_score_without | score_delta | tier | support (strong / moderate / weak) | platform_explicitly_flags (Y/N) | agrees_with_platform (Y/N/NA) | confound_note |

## Tab 6 — Dose Bands (script output, actives only)
| ingredient_key | dose_band | n_products | mean_score | median_score |

## Tab 7 — Scoring Model
| Criterion | Direction (+/−) | Relative weight (High / Medium / Low / Not recoverable) | Statement type (Published / Observed / Inferred) | Evidence | Confidence |

## Tab 8 — Brand Read
| Client SKU | Score | Population rank / percentile | Penalties (ingredient → component) | What holds up | Closest competitor SKU | Competitor score | Gap explanation |

## Tab 9 — Guardrails
| # | Guardrail (constraint statement) | Variable (Ingredient / Dose / Form / Testing-Transparency) | SKUs affected | Score association in population | Statement type | Caveat |

## Tab 10 — Limits
| Limit | Why it matters | Affects which findings |

## Tab 11 — Method Log
| Timestamp | Platform | Action | URL | Result | Gated / skipped | Notes |

Plus a top block: capture window (first/last date), population size, score range, platform methodology page version/date, tools used, script version.
