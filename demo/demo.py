"""Showcase betterplots styling and color palette across plot types."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import argparse
from betterplots import boxstripplot, set_style


def main(out: Path = Path(__file__).parent / "demo.png", **style_kwargs):
    set_style(**style_kwargs)

    rng = np.random.default_rng(0)
    fig, axes = plt.subplots(1, 3, figsize=(12, 3.5), num=1, clear=True)

    # line plot: phase-shifted sinusoids cycle through the palette
    ax = axes[0]
    x = np.linspace(0, 2 * np.pi, 200)
    for i in range(6):
        ax.plot(x, np.sin(x + i * np.pi / 6), label=rf"$\phi={i}\pi/6$")
    ax.set(xlabel="x", ylabel=r"sin(x + $\phi$)", title="lines")
    ax.set_ylim(-3, 2)
    ax.legend(loc="lower left", ncol=2)

    # bar plot: grouped categories
    ax = axes[1]
    cats = ["A", "B", "C", "D"]
    groups = ["ctrl", "treat1", "treat2"]
    data = {
        "category": np.tile(cats, len(groups)),
        "group": np.repeat(groups, len(cats)),
        "value": rng.uniform(0.3, 1.0, size=len(cats) * len(groups)),
    }
    sns.barplot(data=data, x="category", y="value", hue="group", ax=ax, width=0.4)
    ax.set_title("bars")
    ax.set_ylim(0, 1.8)

    # boxstripplot on the penguins dataset
    ax = axes[2]
    df = sns.load_dataset("penguins")
    boxstripplot(data=df, x="species", y="body_mass_g", hue="sex", width=0.3, ax=ax)
    ax.set_title("boxstripplot")
    ax.legend(loc="upper left")

    fig.tight_layout()

    if out is not None:
        fig.savefig(out, dpi=200, bbox_inches="tight")
        print(f"wrote {out}")
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--out", type=str, default=None)
    parser.add_argument("--darkmode", action="store_true")
    parser.add_argument("--usetex", action="store_true")
    parser.add_argument("--serif", action="store_true")
    parser.add_argument("--colors", type=str, default="tol_light")
    args = parser.parse_args()
    main(
        out=args.out,
        darkmode=args.darkmode,
        colors=args.colors,
        usetex=args.usetex,
        serif=args.serif,
    )
