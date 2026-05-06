# Cold-Start Contradictions And Open Questions

## Hypothesis-Only Open Questions

| scope | compared leads | open_problem | verdict | rationale |
|---|---|---|---|---|
| package::gcn_1544d55444d743c8 | gcn_5e907da32c114d34 vs gcn_78dd3a5f6fb84289 / gcn_e4a5cac31481497c | What observable can distinguish whether the CsPbBr3 ARPES hole effective-mass enhancement requires Fröhlich-polaron electron-phonon renormalization or can be explained by finite-temperature thermal fluctuations and dynamic disorder? | hypothesis_only | The polaron and thermal-disorder sides are LKM-grounded leads, but only the ARPES measurement root has been admitted to executable Gaia DSL in round_0000. Frontier expansion will hydrate and map the competing interpretation claims before any direct contradiction is considered. |

## Round 0001 Hypothesis-Only Tensions

| pair | open_problem | decision | relation_type | dsl_action |
|---|---|---|---|---|
| gcn_5e907da32c114d34 vs gcn_762777de8c644c17 | Does ARPES effective-mass agreement with a Feynman-polaron model uniquely indicate Fröhlich polaron dressing, or can a G0W0/electron-correlation baseline account for the measured mass without electron-phonon mass renormalization? | hypothesis_only | competing_interpretation | no contradiction operator yet; scope and experimental mass values differ across source papers. |
| gcn_e4a5cac31481497c vs gcn_5e907da32c114d34 | Can a polaron-free finite-temperature AIMD/HSE-SOC band structure and a Feynman-polaron treatment both match the same ARPES mass, and what observable discriminates the mechanisms? | hypothesis_only | underdetermination | no contradiction operator yet; both can reproduce the mass but explain it differently. |

## Round 0002 Accepted Contradictions

| pair | open_problem | decision | relation_type | dsl_action |
|---|---|---|---|---|
| gcn_4ad259a13be9454a vs gcn_762777de8c644c17 | Which ARPES observable or matched theory baseline can distinguish genuine electron-phonon polaron mass dressing from quasiparticle/structural baseline effects in CsPbBr3? | accepted_contradiction | scientific_inconsistency | arpes_polaron_signature_vs_gw_no_polaron |
