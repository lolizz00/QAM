# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\QAM\zoom.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 548)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 30, 402, 408))
        self.layoutWidget.setObjectName("layoutWidget")
        self.cw = QtWidgets.QGridLayout(self.layoutWidget)
        self.cw.setContentsMargins(0, 0, 0, 0)
        self.cw.setObjectName("cw")
        self.zoom = MPL_Zoom(self.layoutWidget)
        self.zoom.setMinimumSize(QtCore.QSize(400, 300))
        self.zoom.setObjectName("zoom")
        self.cw.addWidget(self.zoom, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

from MPL_zoom import MPL_Zoom
