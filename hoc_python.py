import time
import webbrowser

from chuongtrinhmo import Ui_MainWindow1
from thunghiem import Ui_MainWindow2
import sys
from PyQt5 import QtWidgets
from  selenium import webdriver

gui=""
app1 = QtWidgets.QApplication(sys.argv)
Mw = QtWidgets.QMainWindow()

def main_pro():
    global gui
    gui = Ui_MainWindow1()
    gui.setupUi1(Mw)
    #.................
    gui.pushButton_2.clicked.connect(screen_2)
    #---------------------------------

    Mw.show()
def screen_2():
    print("aaaa")
    global gui

    gui = Ui_MainWindow2
    gui.setupU2(Mw)

    Mw.show()
    sys.exit(app.exec_())
main_pro()
sys.exit(app1.exec_())

