# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FirstMainWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_firstMainWin(object):
    def setupUi(self, firstMainWin):
        firstMainWin.setObjectName("firstMainWin")
        firstMainWin.resize(400, 300)

        self.retranslateUi(firstMainWin)
        QtCore.QMetaObject.connectSlotsByName(firstMainWin)

    def retranslateUi(self, firstMainWin):
        _translate = QtCore.QCoreApplication.translate
        firstMainWin.setWindowTitle(_translate("firstMainWin", "欢迎"))
