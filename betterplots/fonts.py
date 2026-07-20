import dataclasses

import matplotlib.font_manager as font_manager
from pathlib import Path


def load_fonts():
    root = Path(__file__).parent.resolve() / "fonts"
    bundled = {str(p) for p in root.glob("*.ttf")}
    for fname in bundled:
        font_manager.fontManager.addfont(fname)
    # some bundled TTFs carry bogus weight metadata (e.g. Palatino.ttf reports
    # weight=5), which makes them lose the findfont scoring against system
    # fonts with the same family name. Rebuild the entries with sane weights.
    ttflist = font_manager.fontManager.ttflist
    fixed = []
    for e in ttflist:
        if e.fname in bundled:
            name = Path(e.fname).name.lower()
            if "semibold" in name:
                w = 600
            elif "bold" in name:
                w = 700
            else:
                w = 400
            e = dataclasses.replace(e, weight=w)
        fixed.append(e)
    # prepend bundled entries so they win ties against system fonts
    ours = [e for e in fixed if e.fname in bundled]
    rest = [e for e in fixed if e.fname not in bundled]
    font_manager.fontManager.ttflist = ours + rest
