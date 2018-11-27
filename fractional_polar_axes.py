import numpy as np
import matplotlib.pyplot as plt

from matplotlib.transforms import Affine2D
from matplotlib.projections import PolarAxes
from mpl_toolkits.axisartist import angle_helper
from mpl_toolkits.axisartist.grid_finder import MaxNLocator
from mpl_toolkits.axisartist.floating_axes import GridHelperCurveLinear, FloatingSubplot



class MyPolarAxes:

    def setTheLim(self, _min, _max):
        self.the_max = _max
        self.the_min = _min

        # ----

    def setRlim(self, _min, _max):
        self.r_min = _min
        self.r_max = _max

        # ---

    def setLabels(self, the_label, r_label):
        self.the_label = the_label
        self.r_label = r_label

        # ---

    def __init__(self, figure):
        self.figure = figure

        self.the_min = 0
        self.the_max = 360

        self.r_min = 0
        self.r_max = 20

        self.the_label = 'The'
        self.r_label = 'R'

        # ---

        tr_scale = Affine2D().scale(np.pi / 180., 1.)
        tr = tr_scale + PolarAxes.PolarTransform()
        grid_helper = GridHelperCurveLinear(tr)

        a = FloatingSubplot(self.figure, 111, grid_helper=grid_helper)
        self.figure.add_subplot(a)


        # ---

        # adjust x axis (theta):
        a["bottom"].set_visible(False)
        a.axis["top"].set_axis_direction("bottom")  # tick direction
        a.axis["top"].major_ticklabels.set_axis_direction("top")
        a.axis["top"].label.set_axis_direction("top")

        # adjust y axis (r):
        a.axis["left"].set_axis_direction("bottom")  # tick direction
        a.axis["right"].set_axis_direction("top")  # tick direction

        # ---
        # create a parasite axes whose transData is theta, r:
        self.plt = a.get_aux_axes(tr)
        # make aux_ax to have a clip path as in a?:
        self.patch = a.patch
        # this has a side effect that the patch is drawn twice, and possibly over some other
        # artists. So, we decrease the zorder a bit to prevent this:
        a.patch.zorder = -2

        self.plt.add_artist(plt.Circle([0, 0]))

def fractional_polar_axes(f, thlim=(0, 180), rlim=(0, 1), step=(30, 0.2),
                          thlabel='theta', rlabel='r', ticklabels=True):
    """Return polar axes that adhere to desired theta (in deg) and r limits. steps for theta
    and r are really just hints for the locators. Using negative values for rlim causes
    problems for GridHelperCurveLinear for some reason"""
    th0, th1 = thlim # deg
    r0, r1 = rlim
    thstep, rstep = step

    # scale degrees to radians:
    tr_scale = Affine2D().scale(np.pi/180., 1.)
    tr = tr_scale + PolarAxes.PolarTransform()
    theta_grid_locator = angle_helper.LocatorDMS((th1-th0) // thstep)
    r_grid_locator = MaxNLocator((r1-r0) // rstep)
    theta_tick_formatter = angle_helper.FormatterDMS()
    grid_helper = GridHelperCurveLinear(tr,
                                        extremes=(th0, th1, r0, r1),
                                        grid_locator1=theta_grid_locator,
                                        grid_locator2=r_grid_locator,
                                        tick_formatter1=theta_tick_formatter,
                                        tick_formatter2=None)

    a = FloatingSubplot(f, 111, grid_helper=grid_helper)
    f.add_subplot(a)

    # adjust x axis (theta):
    a.axis["bottom"].set_visible(False)
    a.axis["top"].set_axis_direction("bottom") # tick direction
    a.axis["top"].toggle(ticklabels=ticklabels, label=bool(thlabel))
    a.axis["top"].major_ticklabels.set_axis_direction("top")
    a.axis["top"].label.set_axis_direction("top")

    # adjust y axis (r):
    a.axis["left"].set_axis_direction("bottom") # tick direction
    a.axis["right"].set_axis_direction("top") # tick direction
    a.axis["left"].toggle(ticklabels=ticklabels, label=bool(rlabel))

    # add labels:
    a.axis["top"].label.set_text(thlabel)
    a.axis["left"].label.set_text(rlabel)

    # create a parasite axes whose transData is theta, r:
    auxa = a.get_aux_axes(tr)
    # make aux_ax to have a clip path as in a?:
    auxa.patch = a.patch
    # this has a side effect that the patch is drawn twice, and possibly over some other
    # artists. So, we decrease the zorder a bit to prevent this:
    a.patch.zorder = -2

    # add sector lines for both dimensions:
    thticks = grid_helper.grid_info['lon_info'][0]
    rticks = grid_helper.grid_info['lat_info'][0]
    for th in thticks[1:-1]: # all but the first and last
        auxa.plot([th, th], [r0, r1], '--', c='grey', zorder=-1)
    for ri, r in enumerate(rticks):
        # plot first r line as axes border in solid black only if it isn't at r=0
        if ri == 0 and r != 0:
            ls, lw, color = 'solid', 2, 'black'
        else:
            ls, lw, color = 'dashed', 1, 'grey'
        # From http://stackoverflow.com/a/19828753/2020363
        auxa.add_artist(plt.Circle([0, 0], radius=r, ls=ls, lw=lw, color=color, fill=False,
                        transform=auxa.transData._b, zorder=-1))
    return auxa