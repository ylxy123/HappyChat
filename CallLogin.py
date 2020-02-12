# @Time : 2020/2/11 15:59
# @Author : YLXY
# @File : CallMain.py.py
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLineEdit, QMessageBox
from PyQt5.Qt import *
import sys
from login import Ui_login
from FirstMainWin import *
from CallMain import CallMain

class CallLogin(QWidget, Ui_login):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setupUi(self)
        self.connecter()

        # 设置密码不可见
        self.password_lineEdit.setEchoMode(QLineEdit.Password)

    def click_login(self):
        # 获取用户输入
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        if username =='' or password == '':
            reply = QMessageBox.warning(self, "警告", "请输入用户名和密码")
            return
        # 查询数据库
        # ...
        # 查询数据库

        if username == 'ylxy' and password == '225252':
            Ui_main.show()
            self.close()

        else:
            reply = QMessageBox.warning(self, "警告", "用户名或密码错误，请重新输入！")


    def keyPressEvent(self, evt):
        if evt.key() == Qt.Key_Enter:
            self.click_login()



    def connecter(self):
        self.btn_login.clicked.connect(self.click_login)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Lg = CallLogin()
    Ui_main = CallMain()
    Lg.show()
    sys.exit(app.exec())