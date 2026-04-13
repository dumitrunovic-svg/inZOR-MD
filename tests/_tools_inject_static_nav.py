#!/usr/bin/env python3
"""Inject static Home/Tests (+ optional QC / PFΔ peer rows) into test HTML."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

QC_PEERS = [
    ("photochem", "photochem_multi_geom_active_space/index.html", "Photochemistry (multi-geometry)"),
    ("ethylene3d", "qc_gaps_h2_ethylene_unified/ethylene_3d_zor.html", "Ethylene 3D (quasi-degenerate regions)"),
    ("qcgaps", "qc_gaps_h2_ethylene_unified/index.html", "QC gaps (H₂ & ethylene)"),
    ("comparative", "active_space_comparative/index.html", "8-benchmark comparative"),
    ("cr2", "active_space_cr2/index.html", "Cr₂ active space"),
    ("n2", "active_space_n2/index.html", "N₂ active space"),
]

POWER_PEERS = [
    ("p1", "pfdelta_phase1_118/index.html", "PFΔ Phase 1 (118 + N-1)"),
    ("p2", "pfdelta_phase2_real/index.html", "PFΔ Phase 2 — real AC PF"),
    ("p3", "pfdelta_phase3_n2/index.html", "PFΔ Phase 3 — N-2 robustness"),
    ("p4", "pfdelta_phase4_real/index.html", "PFΔ Phase 4 — real load (UA/DE/FR)"),
    ("p5", "pfdelta_phase5_entsoe/index.html", "PFΔ Phase 5 — ENTSO-E"),
    ("p6", "pfdelta_phase6_capacity/index.html", "PFΔ Phase 6 — capacity boundary"),
]

TOP_START = "<!-- iz-static-nav:top:start -->"
TOP_END = "<!-- iz-static-nav:top:end -->"
BOT_START = "<!-- iz-static-nav:bot:start -->"
BOT_END = "<!-- iz-static-nav:bot:end -->"

SITE_STYLE = (
    "font-family:system-ui,-apple-system,sans-serif;font-size:0.9rem;"
    "background:#0f172a;color:#e5e7eb;padding:0.55rem 1rem;border-bottom:1px solid #334155;"
    "display:flex;flex-wrap:wrap;gap:0.5rem 1.25rem;align-items:center;"
)
LINK_STYLE = "color:#7dd3fc;font-weight:600;text-decoration:none;"
QC_STYLE = (
    "font-family:system-ui,-apple-system,sans-serif;font-size:0.86rem;"
    "background:#1e293b;color:#cbd5e1;padding:0.45rem 1rem;border-bottom:1px solid #475569;"
    "display:flex;flex-wrap:wrap;gap:0.35rem 0.75rem;align-items:center;"
)
PF_STYLE = (
    "font-family:system-ui,-apple-system,sans-serif;font-size:0.86rem;"
    "background:#1a1530;color:#e9d5ff;padding:0.45rem 1rem;border-bottom:1px solid #4c3a69;"
    "display:flex;flex-wrap:wrap;gap:0.35rem 0.75rem;align-items:center;"
)
BOT_WRAPPER = "margin-top:2rem;border-top:1px solid #334155;border-bottom:none;"


def chem_key(rel: Path) -> str | None:
    s = rel.as_posix()
    if s.startswith("photochem_multi_geom_active_space/") and s.endswith("index.html"):
        return "photochem"
    if "qc_gaps_h2_ethylene_unified/" in s and "ethylene_3d_zor" in s:
        return "ethylene3d"
    if s.startswith("qc_gaps_h2_ethylene_unified/") and s.endswith("index.html"):
        return "qcgaps"
    if s.startswith("active_space_comparative/") and s.endswith("index.html"):
        return "comparative"
    if s.startswith("active_space_cr2/") and s.endswith("index.html"):
        return "cr2"
    if s.startswith("active_space_n2/") and s.endswith("index.html"):
        return "n2"
    return None


def power_key(rel: Path) -> str | None:
    s = rel.as_posix()
    for key, path, _label in POWER_PEERS:
        if s == path:
            return key
    return None


def strip_markers(html: str) -> str:
    for a, b in (
        (TOP_START, TOP_END),
        (BOT_START, BOT_END),
    ):
        pat = re.escape(a) + r"[\s\S]*?" + re.escape(b)
        html = re.sub(pat, "", html, count=1)
    return html


def strip_script(html: str) -> str:
    return re.sub(
        r"\n?<script[^>]*test-page-nav\.js[^>]*>\s*</script>\s*",
        "\n",
        html,
        flags=re.I,
    )


def up_to_repo_root(rel: Path) -> str:
    n = len(rel.parent.parts)
    return "../" * (n + 1)


def up_to_tests_dir(rel: Path) -> str:
    n = len(rel.parent.parts)
    return "../" * n if n else "./"


def site_row(up_root: str) -> str:
    return (
        f'<div class="iz-static-site" style="{SITE_STYLE}">'
        f'<a href="{up_root}index.html" style="{LINK_STYLE}">Home</a>'
        f'<span style="opacity:.45">·</span>'
        f'<a href="{up_root}tests.html" style="{LINK_STYLE}">Research Tests</a>'
        f"</div>"
    )


def qc_row(me: str, up_tests: str) -> str:
    parts = []
    for key, path, label in QC_PEERS:
        if key == me:
            continue
        parts.append(f'<a href="{up_tests}{path}" style="color:#93c5fd;font-weight:500;text-decoration:none;">{label}</a>')
    sep = '<span style="opacity:.35"> · </span>'
    return (
        f'<div class="iz-static-qc" style="{QC_STYLE}">'
        f'<span style="color:#94a3b8;font-weight:600;">Other quantum chemistry studies:</span>'
        f"{sep.join(parts)}"
        f"</div>"
    )


def power_row(me: str, up_tests: str) -> str:
    parts = []
    for key, path, label in POWER_PEERS:
        if key == me:
            continue
        parts.append(f'<a href="{up_tests}{path}" style="color:#d8b4fe;font-weight:500;text-decoration:none;">{label}</a>')
    sep = '<span style="opacity:.35"> · </span>'
    return (
        f'<div class="iz-static-pf" style="{PF_STYLE}">'
        f'<span style="color:#c4b5fd;font-weight:600;">Other PFΔ / power-grid studies:</span>'
        f"{sep.join(parts)}"
        f"</div>"
    )


def build_top_block(rel: Path) -> str:
    up_root = up_to_repo_root(rel)
    up_tests = up_to_tests_dir(rel)
    inner = site_row(up_root)
    ck = chem_key(rel)
    if ck:
        inner += qc_row(ck, up_tests)
    pk = power_key(rel)
    if pk:
        inner += power_row(pk, up_tests)
    return f"{TOP_START}\n{inner}\n{TOP_END}\n"


def build_bot_block(rel: Path) -> str:
    up_root = up_to_repo_root(rel)
    up_tests = up_to_tests_dir(rel)
    inner = f'<div class="iz-static-site iz-static-site--bot" style="{SITE_STYLE}{BOT_WRAPPER}">' + (
        f'<a href="{up_root}index.html" style="{LINK_STYLE}">Home</a>'
        f'<span style="opacity:.45">·</span>'
        f'<a href="{up_root}tests.html" style="{LINK_STYLE}">Research Tests</a>'
        "</div>"
    )
    ck = chem_key(rel)
    if ck:
        inner += qc_row(ck, up_tests)
    pk = power_key(rel)
    if pk:
        inner += power_row(pk, up_tests)
    return f"{BOT_START}\n{inner}\n{BOT_END}\n"


def insert_blocks(html: str, top: str, bot: str) -> str:
    html = strip_markers(html)
    m = re.search(r"<body([^>]*)>", html, re.I)
    if not m:
        return html
    pos = m.end()
    html = html[:pos] + "\n" + top + html[pos:]
    lb = html.lower().rfind("</body>")
    if lb == -1:
        return html
    html = html[:lb] + bot + html[lb:]
    return html


def process_file(path: Path, tests_root: Path) -> bool:
    if path.suffix.lower() != ".html":
        return False
    if "_tools" in path.parts:
        return False
    try:
        rel = path.relative_to(tests_root)
    except ValueError:
        return False
    raw = path.read_text(encoding="utf-8")
    new = strip_script(raw)
    new = strip_markers(new)
    top = build_top_block(rel)
    bot = build_bot_block(rel)
    new = insert_blocks(new, top, bot)
    if new != raw:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def scrub_tests_listing(path: Path) -> bool:
    if not path.is_file():
        return False
    raw = path.read_text(encoding="utf-8")
    new = re.sub(
        r"\n\s*// #region agent log[\s\S]*?// #endregion\s*\n",
        "\n",
        raw,
    )
    if new != raw:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def sync_pfdelta_to_deploy(root: Path) -> None:
    """Copy PFΔ phase folders from tests/ into deploy so peer links resolve on GitHub Pages."""
    src_base = root / "tests"
    dst_base = root / "web/inzori-web-deploy/tests"
    if not src_base.is_dir() or not dst_base.is_dir():
        return
    for _key, rel_path, _label in POWER_PEERS:
        folder = rel_path.split("/")[0]
        src = src_base / folder
        dst = dst_base / folder
        if not src.is_dir():
            continue
        if dst.exists():
            continue
        shutil.copytree(src, dst)
        print("copied to deploy", folder)


def main() -> None:
    root = Path("/opt/projects/zor_task_solver")
    sync_pfdelta_to_deploy(root)
    trees = [root / "tests", root / "web/inzori-web-deploy/tests"]
    n = 0
    for tests_root in trees:
        if not tests_root.is_dir():
            continue
        for path in sorted(tests_root.rglob("*.html")):
            if process_file(path, tests_root):
                n += 1
                print("patched", path.relative_to(root))
    for p in (
        root / "tests.html",
        root / "web/inzori-web-deploy/tests.html",
        root / "web/brochure/tests.html",
    ):
        if scrub_tests_listing(p):
            print("scrubbed", p.relative_to(root))
    for js in (root / "tests/js/test-page-nav.js", root / "web/inzori-web-deploy/tests/js/test-page-nav.js"):
        if js.is_file():
            js.write_text(
                "/* Deprecated: navigation is inlined in each test HTML (Home / Research Tests + hub rows). */\n",
                encoding="utf-8",
            )
    print("done, html files touched:", n)


if __name__ == "__main__":
    main()
