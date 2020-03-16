# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\jjy\storejjy\prototype\proto.ui'

import time
import sys
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QLCDNumber, QHBoxLayout


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.recievecustomer_label = QtWidgets.QLabel(self.centralwidget)
        self.recievecustomer_label.setGeometry(QtCore.QRect(30, 20, 250, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.recievecustomer_label.setFont(font)
        self.recievecustomer_label.setObjectName("recievecustomer_label")

        # ----------------------------------------------------------------------
        self.customertext = QtWidgets.QTextEdit(self.centralwidget)
        self.customertext.setGeometry(QtCore.QRect(30, 60, 471, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.customertext.setFont(font)
        self.customertext.setObjectName("customertext")

        self.receivecounterlabel = QtWidgets.QLabel(self.centralwidget)
        self.receivecounterlabel.setGeometry(QtCore.QRect(30, 210, 250, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.receivecounterlabel.setFont(font)
        self.receivecounterlabel.setObjectName("receivecounterlabel")

        self.countertext = QtWidgets.QLineEdit(self.centralwidget)
        self.countertext.setGeometry(QtCore.QRect(30, 260, 461, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.countertext.setFont(font)
        self.countertext.setObjectName("countertext")

        self.customerbutton = QtWidgets.QPushButton(self.centralwidget)
        self.customerbutton.setGeometry(QtCore.QRect(30, 130, 201, 51))
        self.customerbutton.setObjectName("customerbutton")
        self.customerbutton.clicked.connect(self.pushcustomer)
        self.counterbutton = QtWidgets.QPushButton(self.centralwidget)
        self.counterbutton.setGeometry(QtCore.QRect(30, 330, 201, 51))
        self.counterbutton.setObjectName("counterbutton")
        self.counterbutton.clicked.connect(self.pushcounter)
        # --------------------------timer---------------------------------------#

        # ------------------------------timerend----------------------------------#
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        # -------------------------------타이머---------------------------#
        self.i = 0
        self.j = 0
        self.k = 0
        self.l = 0

        self.timer1 = QtCore.QTimer()
        self.timer1.timeout.connect(self.guit1)
        self.timer1.start(100)

        self.timer2 = QtCore.QTimer()
        self.timer2.timeout.connect(self.guit2)
        self.timer2.start(100)

        self.timer3 = QtCore.QTimer()
        self.timer3.timeout.connect(self.guit3)
        self.timer3.start(100)

        self.timer4 = QtCore.QTimer()
        self.timer4.timeout.connect(self.guit4)
        self.timer4.start(100)

        # ----------------------------타이머--------------------------#
        self.countertext.setText(str(1))
        self.receivecounterlabel.setText(_translate("MainWindow", "카운터에서 받기"))
        self.customerbutton.setText(_translate("MainWindow", "메뉴세팅과 메뉴보내기"))
        self.counterbutton.setText(_translate("MainWindow", "카운터로 메시지보내기"))

    def guit1(self):
        test1 = threading.Timer(0.3, self.guit1, args=[self.i])
        self.i += 1
        self.receivecounterlabel.setText(str(self.i))
        self.receivecounterlabel.repaint()
        test1.start()

    def guit2(self):
        test2 = threading.Timer(0.3, self.guit2, args=[self.j])
        self.j += 10
        self.customertext.setText(str(self.j))
        self.customertext.repaint()
        test2.start()

    def guit3(self):
        test3 = threading.Timer(0.3, self.guit3, args=[self.k])
        self.k += 30
        self.recievecustomer_label.setText(str(self.k))
        self.recievecustomer_label.repaint()
        test3.start()

    def guit4(self):
        test4 = threading.Timer(0.3, self.guit4, args=[self.l])
        self.l += 100
        self.countertext.setText(str(self.l))
        self.countertext.repaint()
        test4.start()

    def pushcustomer(self):
        print("1")

    def pushcounter(self):
        print("1")


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())

