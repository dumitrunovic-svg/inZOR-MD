# Cum împachetezi și publici site-ul pe Git (format web)

Acest folder este **pachetul complet** pentru publicare: broșură multilingvă (EN, DE, FR, RO) + catalogul de teste (cu imagini/artefacte). Totul e static (HTML, CSS, JSON, PNG/GIF) – fără build, fără server.

---

## 1. Ce conține pachetul (gata de Git)

```
web/brochure/
├── index.html          # Broșură EN (implicit)
├── ro.html             # Broșură RO
├── de.html             # Broșură DE
├── fr.html             # Broșură FR
├── style.css           # Stil comun (font arXiv, responsive)
├── tests.html          # Catalog de teste (UI)
├── tests/manifest.json # Metadate teste
├── tests/**            # Artefacte (PNG/GIF/JSON/MD)
├── demo_images/**      # Imagini pentru carduri (PNG)
├── papers/**           # Articole/LaTeX (opțional)
├── README_HOSTING.md   # Ghid hosting (opțional)
└── PUBLISH_GIT.md      # Acest fișier
```

Dacă acest folder e deja complet (inclusiv imaginile), poți să îl publici direct pe Git.

---

## 2. Varianta A: Repo Git nou (doar site-ul)

Pentru un repo dedicat doar site-ului (ex. pe GitHub, ca să ai `https://user.github.io/inzori-web/`):

```bash
cd inzori//web/brochure

# Repo nou
git init
git add index.html ro.html de.html fr.html style.css tests.html
git add tests/ demo_images/ papers/
git add README_HOSTING.md PUBLISH_GIT.md
git commit -m "inZORi brochure + tests catalog (full web package)"

# Pe GitHub: creezi un repo gol (fără README), apoi:
git remote add origin https://github.com/<USER>/<REPO>.git
git branch -M main
git push -u origin main
```

Apoi în GitHub: **Settings → Pages → Source: Deploy from branch** → branch `main`, folder **/ (root)**. Site-ul va fi la `https://<USER>.github.io/<REPO>/`.

---

## 3. Varianta B: Subfolder în repo-ul existent (zor_task_solver)

Dacă vrei să rămână totul în același repo și să publici doar `web/brochure` ca site:

**Opțiune 3a – GitHub Pages din subfolder `docs/`:**

1. Copiezi conținutul din `web/brochure/` într-un folder `docs/` în root-ul repo-ului (sau redenumești `web/brochure` în `docs` și actualizezi structura).
2. În GitHub: **Settings → Pages → Source: Deploy from branch** → branch `main`, folder **/docs**.
3. URL: `https://<USER>.github.io/zor_task_solver/` (index = `docs/index.html`).

**Opțiune 3b – Păstrezi `web/brochure` și publici cu GitHub Pages + Jekyll:**

- Poți seta **Source** la branch `main`, folder **/web/brochure** dacă GitHub acceptă (unele setări permit doar `/` sau `/docs`). Verifică în Settings → Pages ce foldere sunt oferite.

**Opțiune 3c – Repo separat clonat din pachet:**

- Rulezi scriptul de mai jos, care creează un folder `inzori-web-deploy` cu tot conținutul; intri în el, `git init`, adaugi remote-ul tău și faci push. Astfel ai un repo curat doar pentru site.

---

## 4. Script: pachet pentru repo separat

Rulezi din root-ul proiectului:

```bash
cd inzori/
./web/pack_for_github_pages.sh
```

Scriptul creează `web/inzori-web-deploy/` cu toate fișierele necesare. Poți copia acest folder într-un repo nou sau îl arhivezi (zip) pentru upload manual.

---

## 5. Verificare înainte de push

- [ ] Deschizi local `index.html` sau rulezi `python3 -m http.server 8765` din `web/brochure` și verifici toate limbile (EN, DE, FR, RO).
- [ ] Click pe **Tests** – se încarcă `tests.html`, se văd filtrele și cardurile se deschid/închid (accordion).
- [ ] Linkurile dintre pagini sunt relative (`index.html`, `ro.html`, `tests.html`) – funcționează și pe GitHub Pages.

---

## 6. După publicare

- **GitHub Pages:** poate dura 1–2 minute până apare site-ul; dacă folosești folder `/docs`, URL-ul e de forma `https://<user>.github.io/<repo>/`.
- **Domeniu propriu:** în Settings → Pages poți seta un custom domain.
- **Actualizări:** modifici fișierele în `web/brochure`, commit + push; GitHub Pages se recompilează automat.
