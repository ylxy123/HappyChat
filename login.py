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
        icon.addPixmap(QtGui.QPixmap("用户 .png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        login.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(login)
        self.label.setGeometry(QtCore.QRect(40, 50, 81, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.username_lineEdit = QtWidgets.QLineEdit(login)
        self.username_lineEdit.setGeometry(QtCore.QRect(140, 50, 141, 21))
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.btn_login = QtWidgets.QPushButton(login)
        self.btn_login.setGeometry(QtCore.QRect(80, 150, 171, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.btn_login.setFont(font)
        self.btn_login.setObjectName("btn_login")
        self.label_2 = QtWidgets.QLabel(login)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 72, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.password_lineEdit = QtWidgets.QLineEdit(login)
        self.password_lineEdit.setGeometry(QtCore.QRect(140, 90, 141, 21))
        self.password_lineEdit.setObjectName("password_lineEdit")

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)
        login.setTabOrder(self.username_lineEdit, self.password_lineEdit)
        login.setTabOrder(self.password_lineEdit, self.btn_login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "UserLogin"))
        self.label.setText(_translate("login", "用户名："))
        self.btn_login.setText(_translate("login", "登录"))
        self.label_2.setText(_translate("login", "密码："))
import icon_rc_rc
