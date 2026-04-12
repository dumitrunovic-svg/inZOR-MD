#!/usr/bin/env python3
"""Generate a short looping GIF for LinkedIn — photochem benchmark infographic animation.

Requires: matplotlib, pillow (Pillow writes GIF frames).

Run:
  python3 zenodo_publish/photochem_multigeom/generate_linkedin_animation.py

Output:
  zenodo_publish/photochem_multigeom/photochem_linkedin_anim.gif
"""
from __future__ import annotations

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import FancyBboxPatch, Polygon

HERE = Path(__file__).resolve().parent
OUT = HERE / "photochem_linkedin_anim.gif"

# Canvas — LinkedIn-friendly aspect (roughly 1.91:1 wide, or 4:5 portrait; we use 9:16-ish vertical for feed)
FIG_W, FIG_H = 6, 10
DPI = 100
N_FRAMES = 48
FPS = 12


def ease_out_cubic(t: float) -> float:
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3


def setup_ax(ax):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    fig = ax.figure
    fig.patch.set_facecolor("#0f1419")
    ax.set_facecolor("#0f1419")


def draw_frame(ax, frame: int):
    ax.clear()
    setup_ax(ax)
    t = frame / (N_FRAMES - 1)
    loop = (math.sin(t * 2 * math.pi) + 1) / 2  # 0..1 smooth loop

    # Animated diagonal gradient band (subtle motion)
    shift = 0.15 * math.sin(t * 2 * math.pi)
    verts = [
        (0.0 + shift, 1.0),
        (0.35 + shift, 0.55),
        (0.5 + shift, 0.62),
        (0.15 + shift, 1.0),
    ]
    poly = Polygon(verts, closed=True, facecolor="#00b4a0", alpha=0.35 + 0.15 * loop)
    ax.add_patch(poly)
    verts2 = [
        (0.55 - shift, 0.0),
        (1.1 - shift, 0.4),
        (1.0 - shift, 0.52),
        (0.4 - shift, 0.08),
    ]
    poly2 = Polygon(verts2, closed=True, facecolor="#7c3aed", alpha=0.22 + 0.1 * loop)
    ax.add_patch(poly2)

    # Staggered fade-in phases (loop segment)
    phase = (t * 2) % 1.0
    title_alpha = ease_out_cubic(min(1.0, phase * 4))
    sub_alpha = ease_out_cubic(max(0, min(1, (phase - 0.12) * 4)))
    card_alpha = ease_out_cubic(max(0, min(1, (phase - 0.28) * 3)))
    big_alpha = ease_out_cubic(max(0, min(1, (phase - 0.45) * 4)))
    foot_alpha = ease_out_cubic(max(0, min(1, (phase - 0.62) * 4)))

    # Title
    ax.text(
        0.5,
        0.88,
        "Photochemical\nactive-space benchmark",
        ha="center",
        va="center",
        fontsize=16,
        fontweight="700",
        color="#f8fafc",
        alpha=title_alpha,
        linespacing=1.15,
    )
    ax.text(
        0.5,
        0.74,
        "inZOR-ND  vs  NOON-MP2  ·  SA-CASSCF  ·  cc-pVDZ",
        ha="center",
        va="center",
        fontsize=9,
        color="#94a3b8",
        alpha=sub_alpha,
    )

    # Bento card — primary result
    card = FancyBboxPatch(
        (0.08, 0.38),
        0.84,
        0.28,
        boxstyle="round,pad=0.02,rounding_size=0.03",
        facecolor="#1e293b",
        edgecolor="#00d9b8",
        linewidth=2,
        alpha=0.92 * card_alpha,
    )
    ax.add_patch(card)
    ax.text(
        0.5,
        0.62,
        "PRIMARY RESULT",
        ha="center",
        va="center",
        fontsize=8,
        fontweight="600",
        color="#5eead4",
        alpha=card_alpha,
    )
    ax.text(
        0.5,
        0.54,
        "Fulvene  CAS(10,10)",
        ha="center",
        va="center",
        fontsize=13,
        fontweight="700",
        color="#f1f5f9",
        alpha=card_alpha,
    )

    # Pulsing 12/12
    pulse = 0.85 + 0.15 * (math.sin(t * 4 * math.pi) ** 2)
    ax.text(
        0.5,
        0.445,
        "12 / 12  geometries",
        ha="center",
        va="center",
        fontsize=22,
        fontweight="800",
        color="#2dd4bf",
        alpha=big_alpha * pulse,
    )
    ax.text(
        0.5,
        0.36,
        "~5 kcal/mol mean vs NOON  (cluster-refined)",
        ha="center",
        va="center",
        fontsize=9,
        color="#cbd5e1",
        alpha=big_alpha * 0.95,
    )

    # Footer stats — slide up feel via alpha
    ax.text(
        0.5,
        0.22,
        "3 molecules   ·   52 geometries   ·   cluster of solutions",
        ha="center",
        va="center",
        fontsize=10,
        fontweight="600",
        color="#e2e8f0",
        alpha=foot_alpha,
    )
    ax.text(
        0.5,
        0.12,
        "dumitrunovic-svg.github.io/inZOR-ND",
        ha="center",
        va="center",
        fontsize=8,
        color="#64748b",
        alpha=foot_alpha * 0.9,
    )


def main() -> None:
    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H), dpi=DPI)
    setup_ax(ax)

    def _update(i):
        draw_frame(ax, i)
        return []

    anim = FuncAnimation(
        fig,
        _update,
        frames=N_FRAMES,
        interval=1000 / FPS,
        blit=False,
    )
    anim.save(
        str(OUT),
        writer="pillow",
        fps=FPS,
    )
    plt.close(fig)
    kb = OUT.stat().st_size / 1024
    print(f"Wrote {OUT} ({kb:.0f} KB)")


if __name__ == "__main__":
    main()
