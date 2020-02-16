# @Time : 2020/2/12 16:04
# @Author : YLXY
# @File : CallMain.py
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLineEdit, QMessageBox
import sys
from FirstMainWin import Ui_MainWin
from PyQt5.Qt import *
from PyQt5.QtCore import QDateTime, QTimer

class CallMain(QWidget, Ui_MainWin):
    def __init__(self):
        self.today_things = ''
        self.done_things = ''
        super(QWidget, self).__init__()
        self.setupUi(self)
        self.connecter()

        # 显示动态时间
        timer = QTimer(self)
        timer1 = QTimer(self)
        timer2 = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer1.timeout.connect(self.showtime1)
        timer2.timeout.connect(self.showtime2)
        timer.start()
        timer1.start()
        timer2.start()

    def showtime(self):
        datetime = QDateTime.currentDateTime()
        text = datetime.toString()
        self.time_label.setText(text)

    def showtime1(self):
        datetime1 = QDateTime.currentDateTime()
        text1 = datetime1.toString()
        self.time_label_2.setText(text1)

    def showtime2(self):
        datetime2 = QDateTime.currentDateTime()
        text2 = datetime2.toString()
        self.time_label_3.setText(text2)

    def show_today_browser(self):
        today_things = self.lineEdit_2.text()
        done_things = self.lineEdit.text()
        self.lineEdit_2.clear()
        self.textBrowser_2.append(today_things)
        self.cursor = self.textBrowser_2.textCursor()
        self.textBrowser_2.moveCursor(self.cursor.End)

    def set_opacity(self):
        op = (self.set_opacity_bar.value()+1)/100

        self.setWindowOpacity(op)


    def keyPressEvent(self, evt):
        if evt.key() == Qt.Key_Enter or evt.key() == Qt.Key_Return:
            self.show_today_browser()




    def connecter(self):
        self.apply_button.clicked.connect(self.set_opacity)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    Ui_main = CallMain()
    Ui_main.show()
    sys.exit(app.exec())