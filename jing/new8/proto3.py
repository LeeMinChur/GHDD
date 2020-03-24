# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\jjy\storejjy\prototype\proto.ui'

import time
import sys
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QLCDNumber, QHBoxLayout

from new8.server_ms import *




class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.recievecustomer_label = QtWidgets.QLabel(self.centralwidget)
        self.recievecustomer_label.setGeometry(QtCore.QRect(30, 20, 250, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.recievecustomer_label.setFont(font)
        self.recievecustomer_label.setObjectName("recievecustomer_label")

        # ----------------------------------------------------------------------
        self.customertext = QtWidgets.QTextEdit(self.centralwidget)
        self.customertext.setGeometry(QtCore.QRect(30, 60, 700, 250))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        # self.customertext.moveCursor(QTextCursor.End)
        self.customertext.setFont(font)
        self.customertext.setObjectName("customertext")

        self.receivecounterlabel = QtWidgets.QLabel(self.centralwidget)
        self.receivecounterlabel.setGeometry(QtCore.QRect(30, 400, 250, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.receivecounterlabel.setFont(font)
        self.receivecounterlabel.setObjectName("receivecounterlabel")

        self.sendtext_label = QtWidgets.QLabel(self.centralwidget)
        self.sendtext_label.setGeometry(QtCore.QRect(760, 20, 400, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.sendtext_label.setFont(font)
        self.sendtext_label.setObjectName("텍스트보내는 레이블")


        self.countertext = QtWidgets.QTextEdit(self.centralwidget)
        self.countertext.setGeometry(QtCore.QRect(30, 455, 700, 250))
        font = QtGui.QFont()
        font.setPointSize(19)

        self.countertext.setFont(font)
        self.countertext.setObjectName("카운터에서 오는 텍스트")

        self.sendtext = QtWidgets.QLineEdit(self.centralwidget)
        self.sendtext.setGeometry(QtCore.QRect(760, 60, 400, 645))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.sendtext.setFont(font)
        self.sendtext.setObjectName("텍스트보내는텍스트라인")

        self.sendtext_button = QtWidgets.QPushButton(self.centralwidget)
        self.sendtext_button.setGeometry(QtCore.QRect(760, 710, 201, 51))
        self.sendtext_button.setObjectName("customerbutton")
        self.sendtext_button.clicked.connect(self.sendtextbtn)

        self.customerbutton = QtWidgets.QPushButton(self.centralwidget)
        self.customerbutton.setGeometry(QtCore.QRect(30, 325, 201, 51))
        self.customerbutton.setObjectName("customerbutton")
        self.customerbutton.clicked.connect(self.pushcustomer)

        self.counterbutton = QtWidgets.QPushButton(self.centralwidget)
        self.counterbutton.setGeometry(QtCore.QRect(30, 720, 201, 51))
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
        self.sendtext_label.setText(str("카운터와 고객에게 보내기"))


        self.timer2 = QtCore.QTimer()
        self.timer2.timeout.connect(self.guit1)
        self.timer2.start(100)


        self.timer4 = QtCore.QTimer()
        self.timer4.timeout.connect(self.guit2)
        self.timer4.start(100)

        # ----------------------------타이머--------------------------#
        self.countertext.setText(str(1))
        self.receivecounterlabel.setText(_translate("MainWindow", "카운터에서 받기"))
        self.customerbutton.setText(_translate("MainWindow", "메뉴세팅"))
        self.counterbutton.setText(_translate("MainWindow", "주문완료"))
        self.sendtext_button.setText(_translate("MainWindow", "라즈베리파이에 텍스트보내기"))



    def guit1(self):

        self.j = put_data
        self.customertext.append(str(self.j))
        self.customertext.moveCursor(QTextCursor.End)
        if self.j =="주문취소":
            self.customertext.clear()

        if self.j =="주문완료":
            self.customertext.clear()

        # self.customertext.setText(str(self.j))
        # self.customertext.moveCursor(QTextCursor.StartOfWord)
        self.customertext.repaint()



    def guit2(self):
        self.l += 100

        self.countertext.append(str(self.l))
        self.countertext.moveCursor(QTextCursor.End)
        self.countertext.repaint()

    def pushcustomer(self):

        o = str("메뉴세팅")
        subthread(o)


    def pushcounter(self):

        o = str("주문완료")
        subthread(o)

    def sendtextbtn(self):
        print("이곳은 텍스트를 보내는 버튼입니다")



app2 = QtWidgets.QApplication(sys.argv)
MainWindow2 = QtWidgets.QMainWindow()
ui2 = Ui_MainWindow()
ui2.setupUi(MainWindow2)
MainWindow2.show()
sys.exit(app2.exec_())
