# @Time : 2020/2/11 15:59
# @Author : YLXY
# @File : CallMain.py.py
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
import sys
from login import Ui_login
from FirstMainWin import Ui_firstMainWin

class CallLogin(QWidget, Ui_login):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setupUi(self)
        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    Lg = CallLogin()
    sys.exit(app.exec())