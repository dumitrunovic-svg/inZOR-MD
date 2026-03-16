# Zenodo Upload — Metadata QEC
## inZORi QEC: Hardware-Native Quantum Error Correction on IBM Quantum

## ⏳ ÎN AȘTEPTARE — de publicat pe Zenodo
**Fișier PDF:** `inZORi_QEC_Zenodo.pdf`
**Web report:** https://dumitrunovic-svg.github.io/inZORi/tests/qec_zor/

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
inZORi QEC: Hardware-Native Quantum Error Correction Discovered by Genomic Evolution on IBM Quantum (7-qubit, Heron Processor)
```

**Authors:**
```
Novic, Dumitru
  Affiliation: Independent Researcher
  Email: dumitru.novic@gmail.com
```

**Description / Abstract:**
```
We apply the inZORi genomic discovery engine to the problem of quantum error
correction (QEC) on real IBM Quantum hardware, without any prior knowledge of
QEC theory. Rather than implementing a known code, ZOR autonomously discovers
a 7-qubit encoding circuit optimized for the IBM Heron processor's native gate
set (Ry rotations + CZ gates) and tree-topology connectivity. The discovered
ansatz uses 21 continuous parameters, 12 CZ gates, and circuit depth 10,
evolved under a calibrated gate-error depolarizing noise model.

On real IBM Marrakesh hardware in a noisy operating regime (no-code fidelity
0.632), the ZOR code achieves fidelity 0.698 versus the Steane [[7,1,3]] code
at 0.647, a gain of +5.1 percentage points. Both codes outperform the
unprotected qubit, confirming genuine quantum error correction.

The key advantage is hardware-awareness: ZOR's native CZ circuit transpiles to
depth ~53 on Heron processors, while the Steane circuit (CNOT-based) transpiles
to depth ~110. The LUPA precision zoom mechanism refines simulation fidelity
from ~0.99 to 0.999843 in 3 rounds of 20 cycles each.

Validated across 3 IBM Quantum hardware runs (ibm_fez × 2, ibm_marrakesh × 1).
This is the first demonstration of inZORi discovering a competitive QEC code
without quantum error correction domain knowledge.

Key results:
  - ZOR simulation fidelity: 0.999843
  - ZOR HW fidelity (noisy regime, ibm_marrakesh): 0.698
  - Steane [[7,1,3]] HW fidelity: 0.647
  - No-code HW fidelity: 0.632
  - Gain vs Steane: +5.1 percentage points
  - Transpiled depth ZOR: ~53 vs Steane: ~110 (Heron processor)
```

**Publication date:**
```
2026-03-16
```

**Version:**
```
1.0.0
```

### 4. License
```
Creative Commons Attribution 4.0 International (CC BY 4.0)
```

### 5. Keywords (una pe rand)
```
quantum error correction
quantum computing
IBM Quantum
Heron processor
genomic optimization
hardware-native circuits
inZORi
7-qubit code
Steane code
evolutionary algorithms
biologically inspired computing
circuit optimization
CZ gates
noise-aware optimization
```

### 6. Subject / Domain
```
Computer Science → Artificial Intelligence
Physics → Quantum Physics
```

### 7. Related identifiers
```
Type: Is supplement to
Identifier: https://dumitrunovic-svg.github.io/inZORi/tests/qec_zor/
Resource type: Software

Type: Is related to
Identifier: 10.5281/zenodo.18716837
Resource type: Publication / Preprint
Description: inZORi-PFΔ Phase 1 (companion paper)
```

### 8. Additional notes
```
Web demo and full figures:
  https://dumitrunovic-svg.github.io/inZORi/tests/qec_zor/

IBM Quantum hardware job IDs:
  ibm_fez run 1:  d6rlc1ku243c73a1igj0
  ibm_marrakesh:  (job ID in results JSON)
  ibm_fez run 2:  d6rlfgku243c73a1ijt0

Code repository:
  /opt/projects/zor_task_solver/problems/qec_zor/

This research was conducted without institutional affiliation or external
funding. Experiments: local 12-core CPU + IBM Quantum Open Plan account.
March 2026.
```

---

## Pași de urmat pe Zenodo

1. Mergi la: https://zenodo.org/uploads/new
2. Upload fișierul: `inZORi_QEC_Zenodo.pdf`
3. Completează câmpurile de mai sus
4. Click **Save draft** — verifică preview
5. Click **Publish** — primești DOI instant
6. Copiază DOI-ul și adaugă-l în:
   - `web/brochure/tests/manifest.json` (câmpul `zenodo_doi` în entry-ul `qec_zor`)
   - `web/brochure/tests/qec_zor/index.html` (link în secțiunea Reproducibility)

---

## Linkuri utile

- Upload: https://zenodo.org/uploads/new
- inZORi web: https://dumitrunovic-svg.github.io/inZORi/
- Phase 1 Zenodo: https://doi.org/10.5281/zenodo.18716837
