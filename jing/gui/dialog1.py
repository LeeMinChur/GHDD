# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\jjy\storejjy\file1\dialogtest\dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(578, 178)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 140, 541, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.menuname_input = QtWidgets.QLineEdit(Dialog)
        self.menuname_input.setGeometry(QtCore.QRect(90, 30, 113, 20))
        self.menuname_input.setObjectName("menuname_input")
        self.menuname_label = QtWidgets.QLabel(Dialog)
        self.menuname_label.setGeometry(QtCore.QRect(10, 30, 61, 21))
        self.menuname_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.menuname_label.setObjectName("menuname_label")
        self.menu_price = QtWidgets.QLabel(Dialog)
        self.menu_price.setGeometry(QtCore.QRect(10, 60, 61, 21))
        self.menu_price.setScaledContents(True)
        self.menu_price.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.menu_price.setObjectName("menu_price")
        self.menuprice_input = QtWidgets.QLineEdit(Dialog)
        self.menuprice_input.setGeometry(QtCore.QRect(90, 70, 113, 20))
        self.menuprice_input.setObjectName("menuprice_input")
        self.menurecipe1_label = QtWidgets.QLabel(Dialog)
        self.menurecipe1_label.setGeometry(QtCore.QRect(240, 30, 81, 21))
        self.menurecipe1_label.setScaledContents(True)
        self.menurecipe1_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.menurecipe1_label.setObjectName("menurecipe1_label")
        self.menurecipe1_label_2 = QtWidgets.QLabel(Dialog)
        self.menurecipe1_label_2.setGeometry(QtCore.QRect(240, 70, 81, 21))
        self.menurecipe1_label_2.setScaledContents(True)
        self.menurecipe1_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.menurecipe1_label_2.setObjectName("menurecipe1_label_2")
        self.menurecipe1_label_3 = QtWidgets.QLabel(Dialog)
        self.menurecipe1_label_3.setGeometry(QtCore.QRect(240, 110, 81, 21))
        self.menurecipe1_label_3.setScaledContents(True)
        self.menurecipe1_label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.menurecipe1_label_3.setObjectName("menurecipe1_label_3")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.menuname_label.setText(_translate("Dialog", "메뉴 명"))
        self.menu_price.setText(_translate("Dialog", "가격"))
        self.menurecipe1_label.setText(_translate("Dialog", "메뉴레시피1"))
        self.menurecipe1_label_2.setText(_translate("Dialog", "메뉴레시피2"))
        self.menurecipe1_label_3.setText(_translate("Dialog", "메뉴레시피3"))

class startdia1():
    def startdialog(self):
        if __name__ == "__main__":
            import sys
            self.app3 = QtWidgets.QApplication(sys.argv)
            Dialog = QtWidgets.QDialog()
            ui3 = Ui_Dialog()
            ui3.setupUi(Dialog)
            Dialog.show()
            sys.exit(self.app3.exec_())

class start():
    def start1(self):
        startdia1().startdialog()

start().start1()
