# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\RF_Test_Tool\QAM\zoom.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 548)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(100, 30, 402, 408))
        self.widget.setObjectName("widget")
        self.cw = QtWidgets.QGridLayout(self.widget)
        self.cw.setContentsMargins(0, 0, 0, 0)
        self.cw.setObjectName("cw")
        self.zoom = MPL_Zoom(self.widget)
        self.zoom.setMinimumSize(QtCore.QSize(400, 300))
        self.zoom.setObjectName("zoom")
        self.cw.addWidget(self.zoom, 0, 0, 1, 1)
        self._cw = QtWidgets.QGroupBox(self.widget)
        self._cw.setMinimumSize(QtCore.QSize(300, 100))
        self._cw.setMaximumSize(QtCore.QSize(16777215, 100))
        self._cw.setObjectName("_cw")
        self.widget1 = QtWidgets.QWidget(self._cw)
        self.widget1.setGeometry(QtCore.QRect(40, 30, 261, 52))
        self.widget1.setObjectName("widget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.zoomXHorizontalSlider = QtWidgets.QSlider(self.widget1)
        self.zoomXHorizontalSlider.setMaximum(100)
        self.zoomXHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.zoomXHorizontalSlider.setObjectName("zoomXHorizontalSlider")
        self.gridLayout_2.addWidget(self.zoomXHorizontalSlider, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.zoomYHorizontalSlider = QtWidgets.QSlider(self.widget1)
        self.zoomYHorizontalSlider.setMaximum(100)
        self.zoomYHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.zoomYHorizontalSlider.setObjectName("zoomYHorizontalSlider")
        self.gridLayout_2.addWidget(self.zoomYHorizontalSlider, 1, 1, 1, 1)
        self.cw.addWidget(self._cw, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self._cw.setTitle(_translate("Form", "Управление"))
        self.label.setText(_translate("Form", "Увеличение X:"))
        self.label_2.setText(_translate("Form", "Увеличение Y:"))

from MPL_zoom import MPL_Zoom
