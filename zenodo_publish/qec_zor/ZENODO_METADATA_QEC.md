# Zenodo Upload — Metadata QEC v2
## inZORi QEC: Hardware-Native Quantum Error Correction on IBM Quantum — v1 + v2

## ⏳ DE ACTUALIZAT PE ZENODO
**Fișier PDF:** `inZORi_QEC_Zenodo.pdf`
**Web report:** https://dumitrunovic-svg.github.io/inZOR-MD/tests/qec_zor/

---

## Câmpuri de completat pe Zenodo (zenodo.org/uploads/new)

### 1. Files (fișiere de încărcat)
```
inZORi_QEC_Zenodo.pdf
```

### 2. Upload type
```
Publication → Preprint
```

### 3. Basic information

**Title:**
```
inZORi QEC v1+v2: Hardware-Native Quantum Error Correction Discovered by Genomic Evolution on IBM Quantum (7-qubit, Heron Processor)
```

**Authors:**
```
Novic, Dumitru
  Affiliation: Independent Researcher
  Email: dumitru.novic@gmail.com
```

**Description / Abstract:**
```
We apply the inZOR-ND bio-adaptive genomic discovery engine to quantum error
correction (QEC) on real IBM Quantum hardware, without implementing any known
QEC code structure. Two versions are presented: v1 (21 Ry parameters, X-only
correction with 8 syndromes, 4 test states) and v2 (42 Ry+Rz parameters,
Full Pauli correction with 22 syndromes, 6 test states, multi-noise training
over 4 CZ error rate levels).

Both versions discover hardware-native 7-qubit encoding circuits optimized
for the IBM Heron processor's tree topology (ibm_fez physical qubits 3, 2,
4, 16, 1, 5, 23). Across 7 hardware runs on ibm_fez and ibm_marrakesh,
inZOR-ND outperforms Steane [[7,1,3]] in all observed hardware runs, with
gains from +0.2 to +5.1 percentage points.

The key finding is not that inZOR-ND produces a theoretically superior
code — in ideal depolarizing noise simulation, Steane's Full Pauli correction
remains stronger at all tested noise levels. Rather, these results suggest
that genomic search can discover hardware-native QEC encoders whose reduced
transpiled cost yields consistent advantage over theoretically stronger but
hardware-mismatched codes on NISQ devices. This demonstrates that theoretical
optimality is not the same as hardware optimality on current processors.

The core hardware advantage: inZOR-ND's native CZ circuits transpile to depth
~53–58 on IBM Heron, while the Steane code (CNOT-based) transpiles to ~115,
because CZ is a native IBM Heron gate while CNOT requires decomposition. v2
Rz gates are virtual (zero depth, zero error) on Heron.

v1 LUPA precision zoom: simulation fidelity 0.999843 (p_cz=0.002, X-only,
3 rounds × 20 cycles, ~5 min). v2 Qiskit AerSimulator cross-validation:
perfect match with NumPy simulator (diff < 1e-16).

Key results:
  - inZOR-ND outperforms Steane in 7/7 observed hardware runs
  - v1 sim fidelity (LUPA): 0.999843
  - v2 sim fidelity (multi-noise avg, Full Pauli): 0.990244
  - Best hardware gain vs Steane: +5.1 pp (ibm_marrakesh, noisy regime)
  - v1 transpiled depth: ~53 | v2: ~58 | Steane: ~115 (IBM Heron)
  - v1: 21 params (Ry) | v2: 42 params (Ry+Rz) | 12 CZ gates
  - v2 syndromes: 22 (Full Pauli: I + 7X + 7Y + 7Z)
  - 8000 shots per circuit, SamplerV2 runtime API
```

**Publication date:**
```
2026-03-17
```

**Version:**
```
2.0.0
```

### 4. License
```
Creative Commons Attribution 4.0 International (CC BY 4.0)
```

### 5. Keywords (una pe rand)
```
quantum error correction
NISQ devices
IBM Quantum
Heron processor
genomic optimization
hardware-native circuits
inZOR-ND
7-qubit encoding
Steane code
evolutionary algorithms
biologically inspired computing
circuit depth optimization
CZ gates
noise-aware optimization
Full Pauli correction
hardware-aware QEC
NISQ-QEC
transpiled circuit depth
```

### 6. Subject / Domain
```
Computer Science → Artificial Intelligence
Physics → Quantum Physics
```

### 7. Related identifiers
```
Type: Is supplement to
Identifier: https://dumitrunovic-svg.github.io/inZOR-MD/tests/qec_zor/
Resource type: Software

Type: Is related to
Identifier: 10.5281/zenodo.18716837
Resource type: Publication / Preprint
Description: inZORi-PFΔ Phase 1 (companion paper)
```

### 8. Additional notes
```
Web report with figures (8 figures, v1+v2 data):
  https://dumitrunovic-svg.github.io/inZOR-MD/tests/qec_zor/

IBM Quantum hardware runs (7 total):
  v1 runs (4): ibm_fez × 2, ibm_marrakesh × 2
  v2 runs (3): ibm_fez × 1, ibm_marrakesh × 2

Code:
  problems/qec_zor/env_qec_7hw.py          (v1 environment)
  problems/qec_zor/env_qec_7hw_v2.py       (v2 environment)
  problems/qec_zor/run_qec_7hw.py          (v1 optimization + LUPA)
  problems/qec_zor/run_seed1_save.py        (v2 optimization)
  problems/qec_zor/validate_qiskit_hw_v2.py (v2 cross-validation)
  problems/qec_zor/run_ibm_hardware_hw_v2.py (v2 hardware runner)

Best angles:
  results_7hw/best_angles_hw.json      (v1: 21 params)
  results_7hw_v2/best_angles_hw_v2.json (v2: 42 params)

Research conducted without institutional affiliation or external funding.
Experiments: local 12-core CPU + IBM Quantum Open Plan. March 2026.
```

---

## Pași de urmat pe Zenodo

1. Mergi la: https://zenodo.org/uploads/new (sau editează versiunea existentă cu **New version**)
2. Upload fișierul: `inZORi_QEC_Zenodo.pdf`
3. Completează câmpurile de mai sus
4. Click **Save draft** — verifică preview
5. Click **Publish** — primești DOI instant
6. Copiază DOI-ul și adaugă-l în:
   - `tests/manifest.json` (câmpul `links` în entry-ul `qec-zor-ibm`)
   - `tests/qec_zor/index.html` (link în secțiunea Reproducibility)

---

## Linkuri utile

- Upload: https://zenodo.org/uploads/new
- inZOR-ND web: https://dumitrunovic-svg.github.io/inZOR-MD/
- Phase 1 Zenodo: https://doi.org/10.5281/zenodo.18716837
