
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore
from zoom import Ui_Form


class ZoomWid(QtWidgets.QWidget, Ui_Form):

    def __init__(self, parent=None):
        super(ZoomWid, self).__init__(parent)

        self.setupUi(self)
        self.setLayout(self.cw)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

    def dataSlot(self, data):
        if self.isHidden():
            return

        self.zoom.plot(data)

    def showSlot(self, state, x=None, y=None):

        if state:
            self.zoom.init(x, y)
            self.show()
        else:
            self.hide()