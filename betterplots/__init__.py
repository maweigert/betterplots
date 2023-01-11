
from .boxstripplot import boxstripplot



def set_style(usetex=False, font_size=12, legend_font_size=12):
    import matplotlib as mpl 
    mpl.rc('text',usetex=usetex)
    mpl.rc('font',family='serif')
    mpl.rc('font',serif=['Palatino'])
    mpl.rc('font',size=font_size)
    mpl.rc('legend',fontsize=legend_font_size)

    if usetex:
        print('in case latex is not working, make sue that the following packages are installed:')
        print('sudo apt-get install dvipng texlive-latex-extra texlive-fonts-recommended cm-super')

    # xtick.major.size : 5
    # xtick.minor.size : 3
    # ytick.major.size : 5
    # ytick.minor.size : 3
    # axes.linewidth : 0.8
    # legend.handlelength : 2.0

