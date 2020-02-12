# @Time : 2020/2/12 16:04
# @Author : YLXY
# @File : CallMain.py
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLineEdit, QMessageBox
import sys
from FirstMainWin import Ui_MainWin

class CallMain(QWidget, Ui_MainWin):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setupUi(self)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    Ui_main = CallMain()
    Ui_main.show()
    sys.exit(app.exec())