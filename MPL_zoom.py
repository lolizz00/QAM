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


class MPL_Zoom(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MPL_Zoom, self).__init__(parent)



        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)


