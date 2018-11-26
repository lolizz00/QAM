from MPL_zoom import MPL_Zoom
from PyQt5 import QtCore, QtGui, QtWidgets

from zoom import Ui_Form


class ZoomWid(QtWidgets.QWidget, Ui_Form):

    def __init__(self, parent=None):
        super(ZoomWid, self).__init__(parent)

        self.setupUi(self)
        self.setLayout(self.cw)
