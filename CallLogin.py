# @Time : 2020/2/11 15:59
# @Author : YLXY
# @File : CallMain.py.py
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLineEdit, QMessageBox
import sys
from login import Ui_login
from FirstMainWin import *

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
            print(1)
            reply = QMessageBox.warning(self, "警告", "请输入用户名和密码")
            return
        # 查询数据库
        # ...
        # 查询数据库

        if username == 'ylxy' and password == '225252':
            self.close()
            Ui_main.show()

        else:
            reply = QMessageBox.warning(self, "警告", "用户名或密码错误，请重新输入！")

    def connecter(self):
        self.btn_login.clicked.connect(self.click_login)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Lg = CallLogin()
    Ui_main = Ui_MainWin
    Lg.show()
    sys.exit(app.exec())