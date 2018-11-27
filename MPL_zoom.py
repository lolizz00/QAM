from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import *
import matplotlib
import matplotlib as mpl
import numpy as np
from matplotlib import ticker, cm
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import scipy as sp
from matplotlib.pyplot import Figure
import matplotlib.mlab as mlab
import random
from matplotlib import ticker, cm
from matplotlib import colors
from PyQt5.QtWidgets import *
from matplotlib.ticker import PercentFormatter
import math
from matplotlib.ticker import MaxNLocator
#from zoom import Ui_Form
from fractional_polar_axes import fractional_polar_axes
import matplotlib.cm as cm
from structs import ZoomData
import matplotlib.patches as mpatches


class MPL_Zoom(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MPL_Zoom, self).__init__(parent)


        self.one = False


        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        #layout.addWidget(self.colorbar)
        self.setLayout(layout)
        self.figure.tight_layout()
        self.diag_data = []
        self.diag = None

        self.cmap = matplotlib.cm.get_cmap('hsv')

        self.colorbars = []

    def init(self, x=None, y=None):

        if self.diag:
           # print('Removed')
            self.diag.remove()
            self.diag = None

        self.figure.clear()

        self.diag = fractional_polar_axes(
                     self.figure,
                     thlim=(np.degrees(x) - 5, np.degrees(x) + 5),
                     rlim=(y - 3, y + 3),
                     thlabel='Фаза',
                     step=(1, 1),
                     rlabel=''

        )



    def plot(self, data):

        self.clear()


        sch = 0
        for vals in data:
            self.diag_data.append(self.diag.scatter(np.degrees(vals.x), vals.y, c=vals.colors,s=25))

            sch = sch + 1
            if sch == 1:
                tmp = [mpl.colors.to_hex(val) for val in vals.colors ]
                tmp = np.array(tmp)
                x, y = np.unique(tmp, return_counts=True)
                patchs = []
                for i in range(len(x)):
                    patchs.append(mpatches.Patch(color=x[i], label='cnt: ' + str(y[i])))
                    self.one = True
                    self.figure.legend(handles=patchs)

            #print(vals.colors)

           # cmap = mpl.colors.ListedColormap(['red', 'green', 'blue', 'cyan'])



        self.figure.canvas.draw()

    def clear(self):

        if len(self.colorbars):
            for val in self.colorbars:
                val.remove()

            self.colorbars = []

        if len(self.diag_data):

            for val in self.diag_data:
                val.remove()

            self.diag_data = []

#        self.figure.legend.remove()


        if  self.diag.get_legend():
         self.diag.get_legend().remove()