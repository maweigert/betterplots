import matplotlib.font_manager as font_manager
from pathlib import Path

def load_fonts():
    root = Path(__file__).parent.resolve()/'fonts'
    for fname in root.glob('*.ttf'):
        print(f'adding font {fname} to matplotlib font_manager')
        font_manager.fontManager.addfont(str(fname))
