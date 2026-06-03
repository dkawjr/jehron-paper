"""
nature_style.py
---------------
Shared styling for publication-quality (Nature-style) figures.

Design choices follow Nature's figure guidelines:
  * Sans-serif type (Arial/Helvetica), ~7-8 pt.
  * Thin axes (0.75 pt), outward ticks, no top/right spines.
  * No chart titles (journals use captions); no heavy gridlines.
  * Colour-blind-safe palette (Okabe-Ito derived).
  * Single-column = 89 mm, double-column = 183 mm widths.
  * Vector PDF + 600-dpi PNG output.
"""

from pathlib import Path
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
FIGS = ROOT / "figures"
FIGS.mkdir(exist_ok=True)

# ---- canvas sizes (inches) ------------------------------------------------
MM = 1 / 25.4
COL1 = 89 * MM     # single column
COL15 = 120 * MM   # 1.5 column
COL2 = 183 * MM    # double column

# ---- colour palette (Okabe-Ito, colour-blind safe) ------------------------
CATEGORY_COLORS = {
    "Bacteria": "#0072B2",   # blue
    "Virus":    "#D55E00",   # vermillion
    "Parasite": "#009E73",   # bluish green
    "Other":    "#999999",   # grey
}

# Pathogen colours: shaded WITHIN each category so type is readable at a glance.
PATHOGEN_COLORS = {
    # Bacteria (blues)
    "E. coli":         "#0072B2",
    "C. difficile":    "#4FA3D1",
    "Salmonella":      "#7FC0E0",
    "Yersinia":        "#A9D6EC",
    # Viruses (oranges/reds)
    "Norovirus":       "#D55E00",
    "Adenovirus":      "#E8833B",
    "Rotavirus":       "#F0A875",
    "Sapovirus":       "#F6C9A8",
    # Parasites (greens)
    "Cryptosporidium": "#009E73",
    "Giardia":         "#5FC2A4",
    # Other
    "Other":           "#999999",
}

# Plot order (category-grouped, descending overall frequency within category)
PATHOGEN_ORDER = [
    "E. coli", "C. difficile", "Yersinia", "Salmonella",
    "Norovirus", "Adenovirus", "Rotavirus", "Sapovirus",
    "Cryptosporidium", "Giardia", "Other",
]
CATEGORY_ORDER = ["Bacteria", "Virus", "Parasite", "Other"]

# ---- standardized time bins (300-day, collapsed tail) ---------------------
# Decision: 100-400, 400-700, 700-1000, >1000  (later bins have only 1-2 events)
TIME_BINS = [100, 400, 700, 1000, 10000]
TIME_LABELS = ["100–400", "400–700", "700–1000", ">1000"]


def _pick_font():
    """Prefer Arial/Helvetica; fall back gracefully if unavailable."""
    available = {f.name for f in fm.fontManager.ttflist}
    for cand in ("Arial", "Helvetica", "Helvetica Neue", "Liberation Sans",
                 "DejaVu Sans"):
        if cand in available:
            return cand
    return "sans-serif"


def set_style():
    font = _pick_font()
    mpl.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": [font, "DejaVu Sans"],
        "font.size": 8,
        "axes.titlesize": 8,
        "axes.labelsize": 8,
        "xtick.labelsize": 7,
        "ytick.labelsize": 7,
        "legend.fontsize": 7,
        "legend.title_fontsize": 7,
        # thin, clean axes
        "axes.linewidth": 0.75,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.edgecolor": "#333333",
        "axes.labelcolor": "#000000",
        "text.color": "#000000",
        "xtick.color": "#333333",
        "ytick.color": "#333333",
        "xtick.major.width": 0.75,
        "ytick.major.width": 0.75,
        "xtick.major.size": 3,
        "ytick.major.size": 3,
        "xtick.direction": "out",
        "ytick.direction": "out",
        # no heavy grid by default
        "axes.grid": False,
        "grid.color": "#E6E6E6",
        "grid.linewidth": 0.5,
        # figure
        "figure.dpi": 150,
        "savefig.dpi": 600,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.02,
        "pdf.fonttype": 42,    # embed TrueType (editable text in Illustrator)
        "ps.fonttype": 42,
        "svg.fonttype": "none",  # keep SVG text as editable <text>, not paths
        "legend.frameon": False,
    })
    return font


def panel_label(ax, letter, x=-0.16, y=1.04):
    """Add a bold panel letter (a, b, c ...) in Nature style."""
    ax.text(x, y, letter, transform=ax.transAxes,
            fontsize=10, fontweight="bold", va="bottom", ha="right")


def save(fig, name):
    """Save vector SVG + PDF and 600-dpi PNG."""
    for ext in ("svg", "pdf", "png"):
        fig.savefig(FIGS / f"{name}.{ext}")
    plt.close(fig)
    print(f"  saved figures/{name}.svg + .pdf + .png")
