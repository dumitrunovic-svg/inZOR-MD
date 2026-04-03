# inZORi Web Publishing Workflow

## Structure

- **`brochure/`** — Master source for all site content (HTML, images, tests, papers)
- **`inzori-web-deploy/`** — Separate Git repo pointing to https://github.com/dumitrunovic-svg/inZORi
- **`pack_for_github_pages.sh`** — Script to sync brochure → inzori-web-deploy

## What actually gets published (inZOR-ND repo, GitHub Pages)

- **GitHub Actions** builds a folder **`_site/`**: repo-root **`index.html`**, **`tests.html`**, **`de.html`**, **`fr.html`**, **`ro.html`**, plus the **entire repo-root `tests/`** tree (all benchmark HTML, figures, JSON — everything the manifest links to).
- **Not** `web/inzori-web-deploy/` alone: `web/brochure/tests/` is only a **subset** of `tests/`. Publishing only the brochure copy **breaks** most manifest URLs (404).
- CI runs **`./web/pack_for_github_pages.sh`** first so **`tests/qc_gaps_h2_ethylene_unified/`** and **`tests/manifest.json`** stay aligned with **`web/brochure/tests/`**.
- **Nothing goes live until you `git push`** to `main`. Local edits alone do not update `github.io`.

**Altă cale (repo separat inZORi):** folderul **`web/inzori-web-deploy/`** poate fi folosit pentru `git push` manual către alt remote (vezi mai jos). Asta **nu** este același lucru cu artifact-ul Pages din **inZOR-ND**.

## Publishing Workflow

### 1. Edit content in `brochure/` folder (and repo root for landing pages)

```bash
cd /opt/projects/zor_task_solver/web/brochure
# Edit files: index.html, tests.html, add images, etc.
```

### 2. Run pack script to sync to deploy folder

```bash
cd /opt/projects/zor_task_solver
./web/pack_for_github_pages.sh
```

This copies all content from `brochure/` to `inzori-web-deploy/`.

### 3. Commit and push from deploy folder

```bash
cd /opt/projects/zor_task_solver/web/inzori-web-deploy
git add .
git commit -m "Update site content"
git push inzori-site main
```

GitHub Actions will automatically deploy to https://dumitrunovic-svg.github.io/inZORi/

## Important Notes

- **Always edit in `brochure/`**, not directly in `inzori-web-deploy/`
- **`inzori-web-deploy/` is a separate Git repo** — don't commit it to zor_task_solver repo
- **GitHub Pages (inZOR-ND)** uses `.github/workflows/static.yml`: assembles **`_site`** from root HTML + full **`tests/`** (see above). Optional: commit `web/inzori-web-deploy/` for mirroring to another repo only.
- **Site updates take ~60 seconds** after push to appear live

## Structure Details

```
web/
├── brochure/                    # Master source
│   ├── index.html              # Main page (EN, with nav to Tests)
│   ├── de.html, fr.html, ro.html  # Language versions
│   ├── tests.html              # Dynamic test catalog (reads manifest.json)
│   ├── DEMO_ZOR_EN.html        # Interactive demo
│   ├── demo_images/            # Images for demo scenarios
│   ├── tests/
│   │   ├── manifest.json       # Test metadata (10 tests)
│   │   ├── pfdelta_phase1_118/ # Phase 1 detailed report
│   │   ├── social_density/     # Images + GIFs + summary.json
│   │   └── refract/            # Images + GIFs + summary.json
│   └── papers/
│       └── pfdelta_phase1_118_arxiv/  # LaTeX paper
├── inzori-web-deploy/          # Separate Git repo (synced from brochure/)
└── pack_for_github_pages.sh   # Sync script
```

## Adding New Tests

1. Add test entry to `brochure/tests/manifest.json`
2. Add test artifacts (images, JSONs) to `brochure/tests/<test-id>/`
3. Run pack script and push

The `tests.html` page dynamically renders all tests from `manifest.json`.
