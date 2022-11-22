"""
"""

import numpy as np
import matplotlib.pyplot as plt
from seaborn.categorical import _CategoricalPlotterNew
import seaborn as sns

from seaborn.utils import remove_na, _default_color
import warnings


class _MyCategoricalPlotterNew(_CategoricalPlotterNew):
    def __init__(self, width, **kwargs):
        super().__init__(**kwargs)
        self._width = width 

    @property
    def _native_width(self):
        return self._width / 0.8



def mystripplot(
    width=.1, 
    data=None, *, x=None, y=None, hue=None, order=None, hue_order=None,
    jitter=True, dodge=False, orient=None, color=None, palette=None,
    size=5, edgecolor="gray", linewidth=0,
    hue_norm=None, native_scale=False, formatter=None, legend="auto",
    ax=None, **kwargs
):

    p = _MyCategoricalPlotterNew(
        width,
        data=data,
        variables=_MyCategoricalPlotterNew.get_semantics(locals()),
        order=order,
        orient=orient,
        require_numeric=False,
        legend=False,
    )

    if ax is None:
        ax = plt.gca()

    if p.var_types.get(p.cat_axis) == "categorical" or not native_scale:
        p.scale_categorical(p.cat_axis, order=order, formatter=formatter)


    p._attach(ax)

    hue_order = p._palette_without_hue_backcompat(palette, hue_order)
    palette, hue_order = p._hue_backcompat(color, palette, hue_order)

    color = _default_color(ax.scatter, hue, color, kwargs)

    p.map_hue(palette=palette, order=hue_order, norm=hue_norm)

    
    # XXX Copying possibly bad default decisions from original code for now
    kwargs.setdefault("zorder", 3)
    size = kwargs.get("s", size)

    kwargs.update(dict(
        s=size ** 2,
        edgecolor=edgecolor,
        linewidth=linewidth)
    )


    p.plot_strips(
        jitter=0.3,
        dodge=dodge,
        color=color,
        edgecolor=edgecolor,
        plot_kws=kwargs,
    )

    # XXX this happens inside a plotting method in the distribution plots
    # but maybe it's better out here? Alternatively, we have an open issue
    # suggesting that _attach could add default axes labels, which seems smart.
    p._add_axis_labels(ax)
    p._adjust_cat_axis(ax, axis=p.cat_axis)

    return ax


def boxstripplot(x=None, y=None, data=None,
                    width=0.2, size=2, 
                    box_alpha = 0.9,  
                    strip_alpha = 0.5,
                    linewidth=0.5, 
                    fliersize=0,
                     hue=None, order=None, hue_order=None, orient=None, color=None, palette=None,
                     ax=None,
                     box_kwargs=None, strip_kwargs=None):
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
        
    box_kwargs.setdefault('boxprops', dict())
    box_kwargs.setdefault('whiskerprops', dict())
    box_kwargs.setdefault('capprops', dict())

    box_kwargs['boxprops'].setdefault('alpha', box_alpha)
    box_kwargs['whiskerprops'].setdefault('alpha', box_alpha)
    box_kwargs['capprops'].setdefault('alpha', box_alpha)
    strip_kwargs.setdefault('alpha', strip_alpha)


    with warnings.catch_warnings():
        warnings.filterwarnings('ignore')
        ax = sns.boxplot(data=data, x=x, y=y, width=width, hue=hue, order=order, hue_order=hue_order, orient=orient, color=color, palette=palette, fliersize=fliersize, ax=ax, **box_kwargs)
        ax = mystripplot(data=data, x=x, y=y, width=width, size=size, hue=hue, dodge=False if hue is None else True, order=order, hue_order=hue_order, orient=orient, color=color, palette=palette, linewidth=linewidth, ax=ax, **strip_kwargs)
    
    return ax

