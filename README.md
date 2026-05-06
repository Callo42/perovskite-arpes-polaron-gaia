# Perovskite ARPES Polaron Gaia

This repository is a standalone Gaia knowledge package for the CsPbBr3 ARPES effective-mass dispute.

## Scientific Focus

The package is anchored on this open question:

> Does the ARPES-observed hole effective mass in CsPbBr3 constitute evidence for large-polaron mass dressing, or can the same mass scale be explained by finite-temperature disorder, quasiparticle baselines, or experimental/modeling protocol differences?

The current graph stops at one accepted scientific tension: whether ARPES effective-mass enhancement is itself a valid polaron signature, or whether it must be judged only after comparison with matched finite-temperature and quasiparticle baselines.

See `docs/scientific_story.md` for the self-contained narrative.

## Package Contents

- `src/perovskite_arpes_polaron/` — Gaia DSL claims, deductions, supports, contradiction, and priors.
- `references.json` — bibliographic references used by the package.
- `artifacts/lkm-discovery/` — raw LKM payloads, retrieval timeline, graph growth log, and mapping audits.
- `.gaia/` — compiled Gaia artifacts, beliefs, inquiry state, and starmap outputs.
- `.gaia/starmaps/round_0002.svg` — current graph visualization.

## Quality Gates

The package currently passes:

```bash
gaia compile .
gaia check --brief .
gaia check --hole .
gaia infer .
gaia inquiry review --strict .
```

Current compiled state: 48 knowledge nodes, 13 strategies, and 1 contradiction operator.
