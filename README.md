

Some helper functions for creating slightly better looking plots (based on seaborn)


```python

import betterplots as bp
bp.set_style()

# use seaborn or maptlotlib to create plots

```

![Default light-mode plots](demo/demo_light.png)


## Installation

`pip install git+https://github.com/maweigert/betterplots`

Requires Python 3.9 or newer and uses  `tol-colors` ([Paul Tols](https://sronpersonalpages.nl/~pault/) nice colour schemes)

### Styling

Call `set_style()` before creating Matplotlib or Seaborn figures.

- Default appearance with sans-serif text without LaTeX, white backgrounds, no grid, no top/right spines, frameless legends
- Default palette `tol_light`; choose `colors="tol_muted"`, other `tol_` palettes, `"tab10"`, or `"mw"`
- `boxstripplot()` inherits the active palette; pass `palette=` to override it
- `darkmode=True` for dark backgrounds; call `set_style()` to restore light defaults for new figures
- Independent font sizes with `font_size=12`, `label_size=10`, `tick_size=10`, and `legend_font_size=10`
- `serif=True` for serif text; `usetex=True` for LaTeX rendering
- `rc={"lines.linewidth": 2}` for arbitrary Matplotlib settings, applied last; explicit plot arguments take precedence

LaTeX requires a TeX installation with `newpx`, `opensans`, `mathtools`, and `bm`.



## Examples


### Dark mode with LaTeX

```python
set_style(darkmode=True, usetex=True, serif=True)
```

![Dark-mode plots with LaTeX and serif fonts](demo/demo_dark.png)

### `boxstripplot`

Provides a boxplot overlayed with a stripplot:


```python
import matplotlib.pyplot as plt
import seaborn as sns
from betterplots import boxstripplot, set_style


set_style()

df = sns.load_dataset("penguins")


plt.figure(figsize=(5, 4))
boxstripplot(data=df, x='species', y='flipper_length_mm', hue='sex', width=.3)
plt.title('Flipper Length', fontweight="bold")
plt.legend(loc=(1,.8))
plt.tight_layout()
plt.show()


```

![Image](images/example.png)
