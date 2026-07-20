from typing import Literal
from .fonts import load_fonts


load_fonts()

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
}


def set_style(
    usetex=False,
    serif=True,
    font_size=12,
    legend_font_size=10,
    label_size=10,
    tick_size=10,
    colors: Literal["mw", "tab10", None] = "tab10",
):
    import matplotlib as mpl

    mpl.rc("text", usetex=usetex)
    # mpl.rc('font',family='serif')
    # mpl.rc('font',serif=['Palatino'])
    mpl.rcParams["font.family"] = "serif" if serif else "sans-serif"
    mpl.rcParams["font.serif"] = ["Palatino"]
    mpl.rcParams["font.sans-serif"] = [
        "Inter 18pt",
        "Myriad Pro",
        "Neue Haas Grotesk Display Pro",
    ]
    mpl.rc("font", size=font_size)
    mpl.rc("legend", fontsize=legend_font_size)
    mpl.rc("axes", labelsize=label_size)
    mpl.rc("xtick", labelsize=tick_size)
    mpl.rc("ytick", labelsize=tick_size)
    mpl.rcParams["axes.titleweight"] = "semibold"

    if colors is None:
        colors = "tab10"
    if colors not in PALETTES:
        raise ValueError(
            f"colors must be one of {list(PALETTES)} or None, got {colors!r}"
        )
    mpl.rcParams["axes.prop_cycle"] = mpl.cycler(color=PALETTES[colors])

    if usetex:
        mpl.rcParams["text.latex.preamble"] = r"\usepackage{mathtools,amssymb,bm}"
        print(
            "in case latex is not working, make sue that the following packages are installed:"
        )
        print(
            "sudo apt-get install dvipng texlive-latex-extra texlive-fonts-recommended cm-super"
        )

    # xtick.major.size : 5
    # xtick.minor.size : 3
    # ytick.major.size : 5
    # ytick.minor.size : 3
    # axes.linewidth : 0.8
    # legend.handlelength : 2.0
