# inZORi Web Publishing Workflow

## Structure

- **`brochure/`** — Master source for all site content (HTML, images, tests, papers)
- **`inzori-web-deploy/`** — Separate Git repo pointing to https://github.com/dumitrunovic-svg/inZORi
- **`pack_for_github_pages.sh`** — Script to sync brochure → inzori-web-deploy

## What actually gets published

- **GitHub Actions** (`.github/workflows/static.yml`) uploads **`web/inzori-web-deploy/`** only — not the whole monorepo.
- **Nothing goes live until you `git push`** to `main` on the repo that has that workflow (e.g. **inZOR-ND**). Editing files locally or in Cursor does not update `github.io` by itself.
- **`./web/pack_for_github_pages.sh`** must run before commit (or is run in CI) so `inzori-web-deploy` contains:
  - **`index.html`, `de.html`, `fr.html`, `ro.html`** copied from the **repo root**
  - **`tests.html`** + **`tests/**`** from **`web/brochure/tests/`**

If you skip push, or skip pack so `inzori-web-deploy` is stale, the site will not show your latest changes.

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
- **GitHub Pages auto-deploys** from main branch via `.github/workflows/static.yml` — **only** `web/inzori-web-deploy` is uploaded (not the full repo). The workflow runs `pack_for_github_pages.sh` first so the bundle matches `web/brochure/`.
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
