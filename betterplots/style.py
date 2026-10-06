from typing import Optional

import tol_colors as tc

PALETTES = {
    "mw": ["#4B6584", "#7A6FAF", "#B99B52", "#5F8F7A", "#A45A6A", "#5B8FA8"],
    "tab10": [
        "#1f77b4",
        "#ff7f0e",
        "#2ca02c",
        "#d62728",
        "#9467bd",
        "#8c564b",
        "#e377c2",
        "#7f7f7f",
        "#bcbd22",
        "#17becf",
    ],
    **{f"tol_{name}": list(palette) for name, palette in tc.colorsets.items()},
}


def set_style(
    usetex=False,
    serif=False,
    font_size=12,
    legend_font_size=10,
    label_size=10,
    tick_size=10,
    colors: Optional[str] = "tol_light",
    darkmode=False,
    rc=None,
):
    """Set global plot defaults for figures created with Matplotlib and Seaborn.

    Font sizes for legends, labels, and ticks are independent of font_size.
    Use darkmode for dark backgrounds and light text. Apply rc overrides last.
    """
    import matplotlib as mpl

    background = "#202020" if darkmode else "white"
    foreground = "#eeeeee" if darkmode else "black"
    mpl.rcParams.update(
        {
            "axes.facecolor": background,
            "figure.facecolor": background,
            "savefig.facecolor": "auto",
            "savefig.edgecolor": "auto",
            "text.color": foreground,
            "axes.labelcolor": foreground,
            "axes.edgecolor": foreground,
            "axes.titlecolor": "auto",
            "xtick.color": foreground,
            "ytick.color": foreground,
            "xtick.labelcolor": "inherit",
            "ytick.labelcolor": "inherit",
            "patch.edgecolor": foreground,
            "grid.color": "#555555" if darkmode else "#b0b0b0",
            "axes.grid": False,
            "axes.spines.left": True,
            "axes.spines.bottom": True,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.linewidth": 0.8,
            "xtick.direction": "out",
            "ytick.direction": "out",
            "xtick.top": False,
            "ytick.right": False,
            "legend.frameon": False,
            "legend.labelcolor": None,
            "legend.facecolor": "inherit",
        }
    )
    mpl.rc("text", usetex=usetex)
    mpl.rcParams["font.family"] = "serif" if serif else "sans-serif"
    mpl.rcParams["font.serif"] = ["DejaVu Serif"]
    mpl.rcParams["font.sans-serif"] = ["Open Sans", "DejaVu Sans"]
    mpl.rc("font", size=font_size)
    mpl.rc("legend", fontsize=legend_font_size)
    mpl.rc("axes", labelsize=label_size)
    mpl.rc("xtick", labelsize=tick_size)
    mpl.rc("ytick", labelsize=tick_size)
    mpl.rcParams["axes.titleweight"] = "semibold"

    if colors is None:
        colors = "tol_light"
    if colors not in PALETTES:
        raise ValueError(
            f"colors must be one of {list(PALETTES)} or None, got {colors!r}"
        )
    mpl.rcParams["axes.prop_cycle"] = mpl.cycler(color=PALETTES[colors])

    if usetex:
        mpl.rcParams["text.latex.preamble"] = "".join(
            (
                r"\usepackage[nohelv]{newpxtext}",
                r"\usepackage{newpxmath}",
                r"\usepackage[defaultsans]{opensans}",
                r"\usepackage{mathtools,bm}",
            )
        )
    else:
        mpl.rcParams["text.latex.preamble"] = ""

    if rc is not None:
        mpl.rcParams.update(rc)
