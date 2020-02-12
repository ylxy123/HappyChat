# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLineEdit, QMessageBox

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")

        login.setEnabled(True)
        login.resize(632, 253)
        login.setMinimumSize(QtCore.QSize(609, 233))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/TitleIcon/rc/用户 .png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        login.setWindowIcon(icon)
        login.setAutoFillBackground(False)
        login.setStyleSheet("")
        self.label = QtWidgets.QLabel(login)
        self.label.setGeometry(QtCore.QRect(340, 60, 81, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.username_lineEdit = QtWidgets.QLineEdit(login)
        self.username_lineEdit.setGeometry(QtCore.QRect(440, 60, 141, 21))
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.btn_login = QtWidgets.QPushButton(login)
        self.btn_login.setGeometry(QtCore.QRect(380, 140, 171, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.btn_login.setFont(font)
        self.btn_login.setObjectName("btn_login")
        self.label_2 = QtWidgets.QLabel(login)
        self.label_2.setGeometry(QtCore.QRect(350, 100, 72, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.password_lineEdit = QtWidgets.QLineEdit(login)
        self.password_lineEdit.setGeometry(QtCore.QRect(440, 100, 141, 21))
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.line = QtWidgets.QFrame(login)
        self.line.setGeometry(QtCore.QRect(300, 30, 41, 191))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pic_label = QtWidgets.QLabel(login)
        self.pic_label.setGeometry(QtCore.QRect(20, 20, 271, 211))
        self.pic_label.setAutoFillBackground(False)
        self.pic_label.setStyleSheet("image: url(:/TitleIcon/rc/happytalk.jpg);")
        self.pic_label.setText("")
        self.pic_label.setObjectName("pic_label")

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
