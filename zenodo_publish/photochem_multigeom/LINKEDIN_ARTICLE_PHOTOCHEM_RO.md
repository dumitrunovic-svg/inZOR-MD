# LinkedIn — articol / post lung (copy-paste)

**Fișier de lucru:** textul de mai jos poate fi publicat ca **Articol LinkedIn** sau împărțit în 2–3 postări consecutive. Ton: profesional, fără hype gol, date verificabile.

---

## Titlu (variantă „bombă” — alege una)

1. **12 din 12. Fără excepții. Un benchmark fotochemical unde selecția spațiului activ depășește NOON-MP2 la fiecare geometrie.**

2. **Fulvene CAS(10,10): nu e o singură „mască norocoasă” — e un cluster de soluții care bate baseline-ul MP2 pe tot scanul.**

3. **Când heuristica rămâne bună, dar nu mai e plafonul: SA-CASSCF multi-geometrie cu inZOR-ND vs NOON-MP2.**

*Recomandare:* varianta **1** pentru impact în feed; varianta **2** pentru public tehnic.

---

## Subtitlu (opțional, prima linie după titlu)

Trei molecule. 52 de geometrii. Convergență 100%. Rezultat principal: fulvene CAS(10,10), cc-pVDZ — avantaj mediu ~5.2 kcal/mol față de NOON-MP2, la toate cele 12 unghiuri de torsiune testate.

---

## Corp (Articol LinkedIn)

În chimie cuantifică computațională, alegerea spațiului activ pentru CASSCF rămâne una dintre deciziile care fac diferența între un calcul care converge și unul care „pare” convergent dar nu descrie fizica corect.

Multe echipe folosesc **NOON-MP2** — ocupări naturale din MP2 — ca punct de plecare. E rapid, interpretabil și, în multe cazuri, solid.

Întrebarea pe care am pus-o în acest studiu este mai strânsă legată de **fotochimie**: poți găsi un **același** set de orbitali activi care rămâne rezonabil pe **întregul scan** de torsiune — acolo unde apropierea de intersecții conice și degenerările apropiate fac ca regulile „single-reference” să se rupe?

Am comparat **inZOR-ND** (căutare discretă bio-adaptivă) cu **NOON-MP2**, cu același protocol de evaluare (**SA-CASSCF**, două stări, **cc-pVDZ**, aliniere Procrustes), fără tuning specific pe moleculă.

**Rezultatul principal** merită spus clar: la **fulvene CAS(10,10)**, pe **12 unghiuri**, selecția găsită de inZOR-ND are **energie medie mai joasă** decât NOON-MP2 la **fiecare** geometrie — **12/12**. Avantajul mediu este de ordinul **5.2 kcal/mol**. Iar asta nu vine dintr-o singură combinație „magică”: există **un cluster de măști aproape degenerescente** (cinci variante raportate) care realizează același tip de victorie pe tot grid-ul.

Asta nu „anulează” NOON — îl poziționează corect: **rămâne un baseline puternic**, dar **în acest set de benchmark-uri** nu mai poate fi tratat ca limita empirică superioară pentru energia SA-CASSCF.

Pe lângă fulvene, studiul aduce și context comparativ: **etilenă**, **butadienă**, și fulvene la **CAS(6,6)** și **CAS(8,8)** — inclusiv un avantaj mare la CAS(8,8) pe un subset diagnostic. Detaliile, tabelele și figurile sunt publice.

Dacă lucrezi la dinamică non-adiabatică, scanări de torsiune sau automatizarea rutelor CASSCF, mesajul practic e simplu: ** merită să investești în selecția spațiului activ ca problemă de optimizare**, nu doar ca listă de reguli implicite.

**Link rezultate (HTML):**  
https://dumitrunovic-svg.github.io/inZOR-ND/tests/photochem_multi_geom_active_space/index.html

**PDF (Zenodo / repo):**  
`zenodo_publish/photochem_multigeom/inZOR-ND_Photochem_MultiGeom_ActiveSpace_Zenodo.pdf`

---

## Variante scurte pentru POST (dacă nu folosești Articol)

**Post A — hook + link**  
12/12. Nu e headline de marketing — e rezultat la fulvene CAS(10,10): inZOR-ND vs NOON-MP2 pe tot scanul de torsiune, același protocol SA-CASSCF. NOON rămâne baseline puternic; aici, căutarea găsește sistematic energii mai joase. Detalii și figuri → [link].

**Post B — pentru ingineri QC**  
Dacă încă tratezi NOON ca „default suficient” pentru spațiul activ pe PEC-uri fotochimice: am publicat un benchmark multi-geometrie (etilenă, butadienă, fulvene) unde merită să privești și optimizarea discretă. Fulvene CAS(10,10) e punctul cel mai dur: 12/12 unghiuri, cluster de soluții. [link]

---

## Hashtag-uri (alege 5–8)

`#QuantumChemistry` `#ComputationalChemistry` `#CASSCF` `#Photochemistry` `#ActiveSpace` `#PySCF` `#Research` `#OpenScience`

---

## Imagine (hero LinkedIn)

Fișier în repo: `zenodo_publish/photochem_multigeom/linkedin_photochem_hero.png`  
Format potrivit pentru post cu imagine mare; pentru **previzualizare link** LinkedIn folosește de obicei 1200×627 — poți decupa/resize dacă e nevoie.
