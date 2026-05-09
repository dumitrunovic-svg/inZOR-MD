# inZOR-ND — Artificial-Life Research Platform

**inZOR-ND** is an artificial-life system in which populations of autonomous organisms explore
parameter spaces through biological dynamics — reproduction, competition, environmental pressure,
and emergent social behavior. It is not reinforcement learning, not a neural network, and does
not use backpropagation. Discovery emerges from the interaction between organisms and their
environment.

The research results are public. The biological engine is proprietary.

**Live research archive:** [dumitrunovic-svg.github.io/inZOR-ND](https://dumitrunovic-svg.github.io/inZOR-ND/)

---

## What is inZOR-ND?

The engine operates on a continuous 2D world. Each organism carries a genome that encodes
a candidate solution (hyperparameters, orbital selections, control parameters, etc.).
The environment provides a fitness landscape — food and danger fields — derived from the
actual scientific problem. Organisms evolve, compete, and reproduce. The population converges
toward high-fitness regions without gradient computation or explicit optimization objectives.

Key properties:
- Non-RL, non-NN, non-backprop
- Biologically inspired: organisms, genomes, food, danger, reproduction, death
- Population-level emergent search with social dynamics
- Applicable to any domain where a fitness proxy can be defined
- Extended by Z2W (world memory) for long-horizon evolutionary continuity

---

## Architecture

```
Scientific Problem
        │
        ▼
  Environment (2D world)
  ┌─────────────────────────────┐
  │  Food field  (fitness+)     │
  │  Danger field (fitness-)    │
  │  World memory (Z2W priors)  │
  └──────────────┬──────────────┘
                 │
         ┌───────┴────────┐
         │   Population   │
         │  [organism₁]   │
         │  [organism₂]   │
         │       …        │
         │  [organismₙ]   │
         └───────┬────────┘
                 │ genome → parameter mapping
                 ▼
        Validated Discovery
```

---

## Research Portfolio

26 published experiments across 6 scientific domains.

### Quantum Chemistry (8 experiments)

| Experiment | Key Result | Report |
|---|---|---|
| Active-Space Comparative (8 benchmarks) | 8/8 benchmarks: correct active space, 0 failures | [report](https://dumitrunovic-svg.github.io/inZOR-ND/tests/active_space_comparative/index.html) |
| Cross-Family Robustness (15 molecules) | 15/15 systems, 43 seeds, 0 failures | [report](https://dumitrunovic-svg.github.io/inZOR-ND/tests/active_space_universality/index.html) |
| Chemistry-Consistent Validation | 11/11 winners chemically meaningful and converged | [report](https://dumitrunovic-svg.github.io/inZOR-ND/tests/active_space_chemistry_consistent/index.html) |
| Photochemical Multi-Geometry (Fulvene) | 12/12 wins vs NOON-MP2 across 3 molecules | [report](https://dumitrunovic-svg.github.io/inZOR-ND/tests/photochem_multi_geom_active_space/index.html) |
| Active Space — Cr₂ | 30M candidates explored, 0.005% coverage sufficient | [report](https://dumitrunovic-svg.github.io/inZOR-ND/tests/active_space_cr2/index.html) |
| Active Space — N₂ Dissociation | Bio-adaptive selection across 3 geometries | [report](https://dumitrunovic-svg.github.io/inZOR-ND/tests/active_space_n2/index.html) |
| Ethylene 3D Quasi-Degenerate Regions | Gap structure mapped via evolutionary search | [report](https://dumitrunovic-svg.github.io/inZOR-ND/tests/qc_gaps_h2_ethylene_unified/index.html) |
| QC Gaps H₂ + Ethylene Unified | Unified motivation, methods, results | [report](https://dumitrunovic-svg.github.io/inZOR-ND/tests/qc_gaps_h2_ethylene_unified/index.html) |

Dedicated repo: [inZOR-ActiveSpace](https://github.com/dumitrunovic-svg/inZOR-ActiveSpace)

---

### Quantum Computing (1 experiment)

| Experiment | Key Result | Report |
|---|---|---|
| QEC on IBM Quantum 7-qubit Heron | Hardware-native error correction, reduced circuit depth | [report](https://dumitrunovic-svg.github.io/inZOR-ND/tests/qec_zor/index.html) |

Dedicated repo: [inZOR-QEC](https://github.com/dumitrunovic-svg/inZOR-QEC)

---

### Fusion / Plasma Physics (1 experiment)

| Experiment | Key Result | Report |
|---|---|---|
| Disruption Proximity Law | Machine-agnostic 3-term law from Ip dynamics; validated MAST, C-Mod, HL-2A | [report](https://dumitrunovic-svg.github.io/inZOR-ND/tests/fusion_disruption/index.html) |

Dedicated repo: [inZOR-Fusion](https://github.com/dumitrunovic-svg/inZOR-Fusion)

---

### BAWS + Power Systems (8 experiments)

| Experiment | Key Result | Report |
|---|---|---|
| BAWS-NR Universal Speedup | 1.59× speedup across 6 scientific domains | [report](https://dumitrunovic-svg.github.io/inZOR-ND/tests/baws_nr_study/index.html) |
| N-1 Grid Security (RE volatility) | 1.66× faster under renewable volatility | [report](https://dumitrunovic-svg.github.io/inZOR-ND/tests/re_study/index.html) |
| PFΔ Phase 6 — 1354-bus Pan-European | Capacity boundary discovery on case1354pegase | [report](https://dumitrunovic-svg.github.io/inZOR-ND/tests/pfdelta_phase6_capacity/index.html) |
| PFΔ Phase 5 — ENTSO-E Real Load | Romania, Germany, France 2024 real data | [report](https://dumitrunovic-svg.github.io/inZOR-ND/tests/pfdelta_phase5_entsoe/index.html) |
| PFΔ Phase 4 — Real Profiles + Blackouts | UA/DE/FR profiles + 3 historical blackouts | [report](https://dumitrunovic-svg.github.io/inZOR-ND/tests/pfdelta_phase4_real/index.html) |
| PFΔ Phase 3 — N-2 Contingency | +16pp, 2.8× faster recovery | [report](https://dumitrunovic-svg.github.io/inZOR-ND/tests/pfdelta_phase3_n2/index.html) |
| PFΔ Phase 2 — Real AC Power Flow | 118-bus + N-1 real AC | [report](https://dumitrunovic-svg.github.io/inZOR-ND/tests/pfdelta_phase2_real/index.html) |
| PFΔ Phase 1 — 118-bus + N-1 | Foundation benchmark | [report](https://dumitrunovic-svg.github.io/inZOR-ND/tests/pfdelta_phase1_118/index.html) |

Dedicated repo: [inZOR-BAWS](https://github.com/dumitrunovic-svg/inZOR-BAWS)

---

### Chaotic Systems (1 experiment)

| Experiment | Key Result | Report |
|---|---|---|
| KS_Official Benchmark (AI-DEEDS 2026) | Discovered structural IID anomaly; −20.55 → +38.30 mean score (+286%) | [report](https://dumitrunovic-svg.github.io/inZOR-ND/tests/ctf_ks_chaotic/index.html) |

Dedicated repo: [inZOR-Chaotic](https://github.com/dumitrunovic-svg/inZOR-Chaotic)

---

### Core Biology — Foundational Experiments (7 experiments)

These experiments demonstrate the biological engine directly, without an external scientific
benchmark. They establish the behavioral properties of the platform.

| Experiment | What it shows | Report |
|---|---|---|
| Scenario 1: Dynamic Environment Adaptation | Population of 40 organisms adapts to periodically alternating worlds (A ↔ B) | [report](https://dumitrunovic-svg.github.io/inZOR-ND/tests/scenario1_dynamic/index.html) |
| Scenario 2: Social Behavior (IQ & Fertility) | IQ-encoded genomes; emergence of social dynamics and fertility coupling | [report](https://dumitrunovic-svg.github.io/inZOR-ND/tests/scenario2_social_iq/index.html) |
| Scenario 3: TESS Signal Prioritization | Multi-criteria prioritization of TESS light-curve signals | [report](https://dumitrunovic-svg.github.io/inZOR-ND/tests/tess/index.html) |
| Scenario 4: Adaptive Robotics | Robot navigates 100×100 grid across 5 phases with mobile hazards | [report](https://dumitrunovic-svg.github.io/inZOR-ND/tests/scenario4_robotics/index.html) |
| Scenario 5: SDC — Slow World Drift | Behavioral continuity under slow drift vs. collapse under chaotic drift | [report](https://dumitrunovic-svg.github.io/inZOR-ND/tests/scenario5_sdc/index.html) |
| Social Density Effect | Emergent intelligence under varying population densities (20 / 60 / 100) | [report](https://dumitrunovic-svg.github.io/inZOR-ND/tests/social_density_effect/index.html) |
| REFRACT (20 seeds) | Emergent minimum-time refraction behavior in Fast/Slow medium | [report](https://dumitrunovic-svg.github.io/inZOR-ND/tests/refract_20seeds/index.html) |

---

## Method Availability

This repository hosts the public research archive (GitHub Pages) and the portfolio index
for the inZOR-ND research program.

The inZOR-ND engine — biological evolution core, organism dynamics, genome encoding,
world memory system (Z2W) — is proprietary and not included in any public repository.

The domain research repos (`inZOR-ActiveSpace`, `inZOR-QEC`, `inZOR-Fusion`, `inZOR-BAWS`,
`inZOR-Chaotic`) contain experiment descriptions, benchmark configurations, visualizations,
and result artifacts only.

For methodology questions, contact the author via GitHub.

---

## Published Research Repos

| Repo | Domain | Experiments |
|---|---|---|
| [inZOR-ActiveSpace](https://github.com/dumitrunovic-svg/inZOR-ActiveSpace) | Quantum Chemistry | 8 |
| [inZOR-QEC](https://github.com/dumitrunovic-svg/inZOR-QEC) | Quantum Computing | 1 |
| [inZOR-Fusion](https://github.com/dumitrunovic-svg/inZOR-Fusion) | Fusion / Plasma | 1 |
| [inZOR-BAWS](https://github.com/dumitrunovic-svg/inZOR-BAWS) | BAWS + Power Systems | 8 |
| [inZOR-Chaotic](https://github.com/dumitrunovic-svg/inZOR-Chaotic) | Chaotic Systems | 1 |

---

*Researcher: Dumitru Novic*
