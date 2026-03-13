# Publishing the inZORi brochure on a free host

This folder contains a **static website** (HTML + CSS only). You can publish it on any free static hosting service.

## What to upload

**Brochure only:** upload the entire `brochure` folder contents:

- `index.html`, `ro.html`, `de.html`, `fr.html`
- `style.css`

**Full package (brochure + tests catalog + images):** upload everything needed for `tests.html` (including figures and artifacts).

Resulting structure for a full deploy:

```
brochure/
  index.html, ro.html, de.html, fr.html, style.css
  tests.html
  demo_images/*.png
  tests/manifest.json
  tests/**/*
  papers/**/*
```

Optional: `README_HOSTING.md` (this file) – not required for the site to work.

---

## Free hosting options

### 1. **GitHub Pages** (recommended)

1. Create a new repository (e.g. `inZORi-brochure` or use an existing repo).
2. Upload `index.html` and `style.css` to the root of the repo (or into a folder, e.g. `docs/`).
3. In the repo: **Settings → Pages**.
4. Under **Source**, choose **Deploy from a branch**.
5. Branch: `main` (or `master`), folder: **/ (root)** or **/docs** if you put files in `docs/`.
6. Save. The site will be at `https://<username>.github.io/<repo>/` (or `.../repo/` if you used a subfolder).

If you use a **project site** and put `index.html` in a branch like `gh-pages`, the URL is the same.

### 2. **Netlify**

1. Go to [netlify.com](https://www.netlify.com) and sign up (free).
2. **Add new site → Deploy manually** (or connect a Git repo).
3. Drag and drop the folder that contains `index.html` and `style.css` into the Netlify drop zone.
4. Netlify gives you a URL like `https://random-name-123.netlify.app`. You can change the subdomain in **Site settings → Domain management**.

### 3. **Vercel**

1. Go to [vercel.com](https://vercel.com) and sign up (free).
2. **Add New → Project**; import from Git or upload.
3. If uploading: run `npx vercel` in the folder that contains `index.html` and `style.css`, or use the Vercel dashboard to upload the folder.
4. You get a URL like `https://your-project.vercel.app`.

### 4. **Cloudflare Pages**

1. Go to [pages.cloudflare.com](https://pages.cloudflare.com) and sign up (free).
2. **Create a project → Direct Upload**.
3. Upload a ZIP of the folder with `index.html` and `style.css`.
4. Your site will be at `https://<project>.pages.dev`.

### 5. **Other options**

- **GitLab Pages** – similar to GitHub Pages; push the files and enable Pages in the project.
- **Surge.sh** – from the folder: `npx surge .` (install Node if needed).
- **Neocities** – sign up at [neocities.org](https://neocities.org), create a site, upload `index.html` and `style.css`.

---

## Checklist before publishing

- [ ] Both `index.html` and `style.css` are in the same folder (or `style.css` is in the path referenced by `index.html`: `href="style.css"`).
- [ ] If you use a subfolder (e.g. `docs/` on GitHub Pages), open the site and click “Key messages” (or any nav link); if it doesn’t scroll, the anchors are correct and the base path is fine.
- [ ] Test on a phone or narrow window: the table scrolls horizontally and text is readable.

---

## Custom domain (optional)

On **Netlify**, **Vercel**, and **Cloudflare Pages** you can add your own domain (e.g. `inzori.example.com`) in the dashboard under domain settings. GitHub Pages allows a custom domain in **Settings → Pages → Custom domain**.

---

No build step or server is required; the site is static and runs entirely in the browser.
