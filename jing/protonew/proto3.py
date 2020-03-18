# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\jjy\storejjy\prototype\proto.ui'

import time
import sys
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QLCDNumber, QHBoxLayout

from protonew.proto1 import *




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
        font.setPointSize(16)
        font.setBold(True)
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


        self.receivecounterlabel.setText(str("카운터 쪽"))
        self.recievecustomer_label.setText(str("고객 쪽"))


        self.timer2 = QtCore.QTimer()
        self.timer2.timeout.connect(self.guit1)
        self.timer2.start(100)


        self.timer4 = QtCore.QTimer()
        self.timer4.timeout.connect(self.guit2)
        self.timer4.start(100)

        # ----------------------------타이머--------------------------#
        self.countertext.setText(str(1))
        self.receivecounterlabel.setText(_translate("MainWindow", "카운터에서 받기"))
        self.customerbutton.setText(_translate("MainWindow", "텍스트입력"))
        self.counterbutton.setText(_translate("MainWindow", "긴하진순"))


    def guit1(self):


        from protonew.proto1 import put_data
        self.j = put_data
        self.customertext.setText(str(self.j))


    def guit2(self):

        self.l += 100
        self.countertext.setText(str(self.l))
        self.countertext.repaint()


    def pushcustomer(self):

        o = input("입력하세요")
        subthread(o)


    def pushcounter(self):

        o = str("긴하진순")
        subthread(o)




app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
