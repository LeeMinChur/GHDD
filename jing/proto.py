# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\jjy\storejjy\prototype\proto.ui'

import time
import sys
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 410)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.recievecustomer_label = QtWidgets.QLabel(self.centralwidget)
        self.recievecustomer_label.setGeometry(QtCore.QRect(30, 20, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.recievecustomer_label.setFont(font)
        self.recievecustomer_label.setObjectName("recievecustomer_label")
        self.customertext = QtWidgets.QLineEdit(self.centralwidget)
        self.customertext.setGeometry(QtCore.QRect(30, 60, 471, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.customertext.setFont(font)
        self.customertext.setObjectName("customertext")
        self.receivecounterlabel = QtWidgets.QLabel(self.centralwidget)
        self.receivecounterlabel.setGeometry(QtCore.QRect(30, 210, 231, 51))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.recievecustomer_label.setText(_translate("MainWindow", "고객에게 받기"))

        self.receivecount_text()
        self.customertext.setText(str(self.test))



        self.receivecounterlabel.setText(_translate("MainWindow", "카운터에서 받기"))

        self.receivecustom_text()
        self.countertext.setText(str(self.test1))


        self.customerbutton.setText(_translate("MainWindow", "메뉴세팅과 메뉴보내기"))
        self.counterbutton.setText(_translate("MainWindow", "카운터로 메시지보내기"))

    def receivecount_text(self):


        self.test =1

    def receivecustom_text(self):

        self.test1 =1
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
