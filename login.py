# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(319, 254)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Title_Icon/E:/Desktop/python脚本/畅聊/HappyChat/用户 .png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        login.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(login)
        self.label.setGeometry(QtCore.QRect(40, 50, 81, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(login)
        self.lineEdit.setGeometry(QtCore.QRect(140, 50, 141, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(login)
        self.pushButton.setGeometry(QtCore.QRect(80, 150, 171, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(login)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 72, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(login)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 90, 141, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)
        login.setTabOrder(self.lineEdit, self.lineEdit_2)
        login.setTabOrder(self.lineEdit_2, self.pushButton)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "UserLogin"))
        self.label.setText(_translate("login", "用户名："))
        self.pushButton.setText(_translate("login", "登录"))
        self.label_2.setText(_translate("login", "密码："))
import icon_rc_rc
