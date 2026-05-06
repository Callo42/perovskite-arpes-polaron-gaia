# Cold-Start Root Candidates

Topic: ARPES effective mass / polaron vs thermal disorder in halide perovskites.

Only `chain-backed` claims (`total_chains > 0`) are eligible for cold-start root selection.

## Chain-Backed Candidates

### 1. `gcn_1544d55444d743c8` — experimental anchor

- Evidence status: `chain-backed`
- Source: paper:812638467241541632 / DOI 10.1103/physrevlett.124.206402
- Paper: Evidence of Large Polarons in Photoemission Band Mapping of the Perovskite Semiconductor CsPbBr3
- Raw evidence: `input/evidence_gcn_1544d55444d743c8_retry.json`
- Claim: Room-temperature ARPES on orthorhombic CsPbBr3 fits the upper valence band near the VBM and reports m_exp = 0.26 ± 0.02 m_e.
- Root-selection note: Good neutral root if we want the graph to branch into competing interpretations from the shared measurement.

### 2. `gcn_5e907da32c114d34` — polaron interpretation side

- Evidence status: `chain-backed`
- Source: paper:812638467241541632 / DOI 10.1103/physrevlett.124.206402
- Paper: Evidence of Large Polarons in Photoemission Band Mapping of the Perovskite Semiconductor CsPbBr3
- Raw evidence: `input/evidence_gcn_5e907da32c114d34.json`
- Claim: Ab initio Fröhlich coupling plus Feynman-polaron treatment reproduces the ARPES-measured CsPbBr3 hole effective mass within uncertainty.
- Root-selection note: Best root if we want to start from the original large-polaron claim and expand outward to challenges.

### 3. `gcn_4d0e277c6d2c4cdc` — reinterpretation experimental benchmark

- Evidence status: `chain-backed`
- Source: paper:arXiv.2203.15070 / DOI 10.48550/arXiv.2203.15070
- Paper: Is there a polaron signature in angle-resolved photoemission of CsPbBr3?
- Raw evidence: `input/evidence_gcn_4d0e277c6d2c4cdc.json`
- Claim: Room-temperature ARPES on freshly cleaved CsPbBr3 reports a hole mass m_h* = 0.203 ± 0.016 m0 at the bulk R-point VBM.
- Root-selection note: Good root if we want the package centered on a direct challenge/re-measurement of the polaron signature.

### 4. `gcn_78dd3a5f6fb84289` — thermal-disorder / no-small-polaron side

- Evidence status: `chain-backed`
- Source: paper:1096665743648358400 / DOI 10.48550/arXiv.2502.06904
- Paper: Distinguishing thermal fluctuations from polaron formation in halide perovskites
- Raw evidence: `input/evidence_gcn_78dd3a5f6fb84289.json`
- Claim: A 300 K HSE-SOC AIMD calculation with an extra hole in bulk CsPbBr3 finds no localized in-gap states or substantial valence-band dispersion changes, indicating no thermally stabilized small-hole polaron under those simulated conditions.
- Root-selection note: Best root if we want to start from the recent counter-interpretation and expand back to the original ARPES/polaron evidence.

### 5. `gcn_cb768fb24af34a91` — broader dynamic-disorder mechanism

- Evidence status: `chain-backed`
- Source: paper:867757485061046539 / DOI 10.48550/arXiv.1902.00950
- Paper: Dynamic Shortening of Disorder Potentials in Anharmonic Halide Perovskites
- Raw evidence: `input/evidence_gcn_cb768fb24af34a91.json`
- Claim: Finite-temperature dynamics confine electronic disorder potentials to nearest-neighbor scales and explain sharp absorption edges despite strong anharmonic motion.
- Root-selection note: Useful supporting branch, but broader than the ARPES mass dispute; less ideal as the first root.

### 6. `gcn_f10ef84d019c497e` — adjacent finite-temperature mass-renormalization mechanism

- Evidence status: `chain-backed`
- Source: paper:867745366357836180 / DOI 10.48550/arXiv.2105.06525
- Paper: Thermal fluctuations and carrier localization induced by dynamic disorder in MAPbI3 described by a first-principles based tight-binding model
- Raw evidence: `input/evidence_gcn_f10ef84d019c497e.json`
- Claim: For MAPbI3 at 300 K, full local spatial disorder increases hole/electron masses by about 66%/71% relative to the ideal static Hamiltonian, making spatial disorder the dominant finite-temperature mass-enhancement contributor.
- Root-selection note: Excellent later support for the thermal-disorder branch, but not the CsPbBr3 ARPES root itself.

## Search Leads / Not Eligible As Cold-Start Root

- `gcn_1fc9a84fbc6e4a1b` (lkm_no_chain; `input/evidence_gcn_1fc9a84fbc6e4a1b.json`): Orthorhombic G0W0 comparison to room-temperature ARPES assumes the orthorhombic model represents ARPES-probed electronic states; total_chains=0, so not eligible as cold-start root.
- `gcn_e4a5cac31481497c` (transient evidence failure; `input/evidence_gcn_e4a5cac31481497c_retry.json`): Promising finite-temperature CsPbBr3 AIMD/HSE-SOC mass-agreement claim appeared in match results, but evidence hydration returned code=290001 twice; keep as a lead for a later retry, not as cold-start root.

## Recommended Root

For the most balanced graph, choose `gcn_1544d55444d743c8` as the experimental measurement anchor: it lets the package branch naturally into the original polaron interpretation (`gcn_5e907da32c114d34`) and the later thermal-disorder/no-polaron reinterpretation (`gcn_78dd3a5f6fb84289`, plus later retry of `gcn_e4a5cac31481497c`).
