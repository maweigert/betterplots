"""
"""

import matplotlib.pyplot as plt
from seaborn.categorical import _CategoricalPlotter
import seaborn as sns

from seaborn.utils import _default_color
import warnings


# patched version including `width`` parameter
class _MyCategoricalPlotter(_CategoricalPlotter):
    def __init__(self, width, **kwargs):
        super().__init__(**kwargs)
        self._width = width

    @property
    def _native_width(self):
        return self._width / 0.8


# patched version to allow for hue offset
def mystripplot(
    width=0.1,
    data=None,
    *,
    x=None,
    y=None,
    hue=None,
    order=None,
    hue_order=None,
    dodge=False,
    orient=None,
    color=None,
    palette=None,
    size=5,
    edgecolor="none",
    linewidth=0,
    hue_norm=None,
    log_scale=None,
    native_scale=False,
    formatter=None,
    legend="auto",
    ax=None,
    **kwargs
):

    p = _MyCategoricalPlotter(
        width=width,
        data=data,
        variables=dict(x=x, y=y, hue=hue),
        order=order,
        orient=orient,
        color=color,
        legend=legend,
    )

    if ax is None:
        ax = plt.gca()

    if p.plot_data.empty:
        return ax

    if p.var_types.get(p.orient) == "categorical" or not native_scale:
        p.scale_categorical(p.orient, order=order, formatter=formatter)

    p._attach(ax, log_scale=log_scale)

    # Deprecations to remove in v0.14.0.
    hue_order = p._palette_without_hue_backcompat(palette, hue_order)
    palette, hue_order = p._hue_backcompat(color, palette, hue_order)

    p.map_hue(palette=palette, order=hue_order, norm=hue_norm)
    color = _default_color(ax.scatter, hue, color, kwargs)

    if edgecolor is None:
        edgecolor = p._complement_color(edgecolor, color, p._hue_map)

    kwargs.setdefault("zorder", 3)
    size = kwargs.get("s", size)

    kwargs.update(
        s=size**2,
        edgecolor=edgecolor,
        linewidth=linewidth,
    )

    p.plot_strips(
        jitter=0.5 * width,
        dodge=dodge,
        color=color,
        plot_kws=kwargs,
    )

    # XXX this happens inside a plotting method in the distribution plots
    # but maybe it's better out here? Alternatively, we have an open issue
    # suggesting that _attach could add default axes labels, which seems smart.
    p._add_axis_labels(ax)
    p._adjust_cat_axis(ax, axis=p.orient)


def boxstripplot(
    x=None,
    y=None,
    data=None,
    width=0.2,
    size=2,
    box_alpha=0.9,
    strip_alpha=0.5,
    linewidth=0.5,
    fliersize=0,
    showmeans=False,
    hue=None,
    order=None,
    hue_order=None,
    orient=None,
    color=None,
    palette=None,
    ax=None,
    box_kwargs=None,
    strip_kwargs=None,
    violin=False,
    saturation=None,
):
    """
    plots a half-box plot with a regular boxplot and a stripplot next to each other

    parameters are like seaborn.boxplot

    Example:
    ========

        import numpy as np
        import pandas as pd

        x = np.random.uniform(0, 1, 100)
        y = np.random.uniform(.5, 1.2, 100)

        df =  pd.DataFrame(dict(x=x, y=y))

        halfboxstripplot(data=df, width=.5,
                         strip_kwargs=dict(alpha=0.5))

    """
    if ax is None:
        ax = plt.gca()

    if palette is None:
        palette = sns.color_palette("tab10")

    if box_kwargs is None:
        box_kwargs = {}

    if strip_kwargs is None:
        strip_kwargs = {}

    box_kwargs.setdefault("boxprops", dict())
    box_kwargs.setdefault("whiskerprops", dict())
    box_kwargs.setdefault("capprops", dict())
    box_kwargs.setdefault(
        "meanprops",
        {
            "marker": "o",
            "markerfacecolor": "none",
            "markeredgecolor": "black",
            "markersize": "5",
        },
    )
    box_kwargs.setdefault(
        "medianprops",
        {
            "color": "black",
            "alpha": 0.35,
        },
    )

    box_kwargs["boxprops"].setdefault("alpha", box_alpha)
    box_kwargs["whiskerprops"].setdefault("alpha", box_alpha)
    box_kwargs["capprops"].setdefault("alpha", box_alpha)
    if saturation is not None:
        box_kwargs["saturation"] = saturation

    strip_kwargs.setdefault("alpha", strip_alpha)

    with warnings.catch_warnings():
        warnings.filterwarnings("ignore")
        if not violin:
            ax = sns.boxplot(
                data=data,
                x=x,
                y=y,
                width=width,
                hue=hue,
                order=order,
                showmeans=showmeans,
                hue_order=hue_order,
                orient=orient,
                color=color,
                palette=palette,
                fliersize=fliersize,
                ax=ax,
                **box_kwargs
            )
        else:
            ax = sns.violinplot(
                data=data,
                x=x,
                y=y,
                width=width,
                hue=hue,
                order=order,
                showmeans=showmeans,
                hue_order=hue_order,
                orient=orient,
                color=color,
                palette=palette,
                fliersize=fliersize,
                ax=ax,
                **box_kwargs
            )
        ax = mystripplot(
            data=data,
            x=x,
            y=y,
            width=width,
            size=size,
            hue=hue,
            dodge=False if hue is None else True,
            order=order,
            hue_order=hue_order,
            orient=orient,
            color=color,
            palette=palette,
            linewidth=linewidth,
            ax=ax,
            legend=None,
            **strip_kwargs
        )
    return ax
