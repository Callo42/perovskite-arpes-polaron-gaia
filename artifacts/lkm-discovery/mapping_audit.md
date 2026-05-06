# Mapping Audit

## Selected Root

| root_id | evidence_status | source_paper | rationale |
|---|---|---|---|
| gcn_1544d55444d743c8 | chain-backed | paper:812638467241541632 | User selected the ARPES effective-mass measurement as the neutral experimental anchor for the polaron-vs-thermal-disorder graph. |

## Factors -> Deductions

| factor_id | source_paper | premises | conclusion | dsl_kind | notes |
|---|---|---|---|---|---|
| gfac_31bb841408184d5e | paper:812638467241541632 | gcn_2e9e6e30a5d7431c, gcn_0a71cf6357114b76, gcn_e24a3d64aa604555 | gcn_1544d55444d743c8 | deduction | Preserved six LKM reasoning steps as deduction reason. |

## Claims

| claim_id | source_paper | role | dsl_label | content_missing |
|---|---|---|---|---|
| gcn_1544d55444d743c8 | paper:812638467241541632 | root conclusion | gcn_1544d55444d743c8 | false |
| gcn_2e9e6e30a5d7431c | paper:812638467241541632 | premise | gcn_2e9e6e30a5d7431c | false |
| gcn_0a71cf6357114b76 | paper:812638467241541632 | premise | gcn_0a71cf6357114b76 | false |
| gcn_e24a3d64aa604555 | paper:812638467241541632 | premise | gcn_e24a3d64aa604555 | false |

## Contradictions

| pair | open_problem | decision | relation_type | dsl_action |
|---|---|---|---|---|
| (none in round_0000) | Whether this ARPES effective-mass measurement requires polaronic renormalization or can be reinterpreted through finite-temperature thermal disorder remains the frontier question for expansion. | hypothesis for later expansion | open_question | none yet |

## Dismissed

| pair | origin | rationale |
|---|---|---|
| (none in round_0000) | | |

## Round 0001 Frontier Expansion

| candidate | channel | evidence_status | action | rationale |
|---|---|---|---|---|
| gcn_5e907da32c114d34 | open_question_conflict | chain-backed | claim + deduction | Original Feynman-polaron interpretation branch; useful frontier claim, not a direct contradiction to the measurement root. |
| gcn_e4a5cac31481497c | support/open_question_conflict | chain-backed | claim + deduction + support to root | Finite-temperature AIMD/HSE-SOC reproduces the ARPES mass, supporting the root as a benchmark while motivating thermal-disorder interpretation. |
| gcn_78dd3a5f6fb84289 | open_question_conflict | chain-backed | claim + deduction | No-small-polaron result under simulated 300 K bulk-like conditions; admitted as interpretation frontier, not as direct contradiction to root measurement. |
| gcn_4d0e277c6d2c4cdc | open_question_conflict | chain-backed | claim + deduction | Independent ARPES mass measurement at 0.203 +/- 0.016 m0; scope/value tension retained for later review. |
| gcn_8c3c520295d7488c | support/open_question_conflict | chain-backed | claim + deduction + weak support to root | G0W0/SOC bare-band benchmark near ARPES mass scale; weak contextual support due theory/experiment scope difference. |
| gcn_762777de8c644c17 | open_question_conflict | chain-backed | claim + deduction | Claim that ARPES mass does not require additional Fröhlich-polaron renormalization; scientific tension with gcn_5e907... retained as hypothesis-only. |

## Round 0002 Theory-Experiment Gap Expansion

| candidate | evidence_status | action | rationale |
|---|---|---|---|
| gcn_ffcf3464e99c47ed | chain-backed | claim + deduction + support | Atomic Feynman-polaron mass calculation supporting the polaron-model branch. |
| gcn_3f848904ab0d4b48 | chain-backed | claim + deduction + support | Quantifies thermal-lattice mass renormalization supporting finite-temperature explanation. |
| gcn_4ad259a13be9454a | lkm_no_chain | source claim + contradiction | Clear provenance in Puppin2020 match output; states ARPES mass extraction is a valid polaronic dressing signature despite unresolved replicas. |

## Display Title Cleanup

All executable science claims now carry concise `title=` metadata so Gaia starmap
renders scientific descriptions rather than raw `gcn_*` labels. The accepted
contradiction helper also has a post-construction title assignment:
`ARPES polaron signature vs G0W0 baseline`.
