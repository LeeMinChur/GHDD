# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\jjy\storejjy\file1\untiwwtled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


import sys, pymysql

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    conn = pymysql.connect(host='127.0.0.3', port=3306, user='root', password='1234', db='project', charset='utf8')
    cursor = conn.cursor()


    # 열 개수
    sql = """SELECT COUNT(*)
    FROM information_schema.columns WHERE table_name='menu';"""
    cursor.execute(sql)
    res = cursor.fetchall()

    for data in res:
        data_list = (list(data))
        data_int = data_list[0]
        data_int1 = int(data_int)

    print(data_int1)

    # 행 개수
    sql2 = """select count(*) from menu;"""
    cursor.execute(sql2)
    res2 = cursor.fetchall()

    for data in res2:
        data_list = (list(data))
        data_int = data_list[0]
        data_int2 = int(data_int)

    print(data_int2)
    # 행이 data_int2, 열이 data_int1

    # 총 데이터베이스 출력
    sql3 = """select * from menu;"""
    cursor.execute(sql3)
    res3 = cursor.fetchall()

    for data in res3:
        print(data)

    # 데이터 하나씩 출력
    sql4 = ''' select *from menu limit 0, 1;'''
    cursor.execute(sql4)

    res = cursor.fetchone()
    print(res[0])

    result = cursor.fetchone()

    def __init__(self):
        super().__init__()

    # 기본 ui구성
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 500, 400))
        self.tableWidget.setObjectName("tableWidget")


        # 열값
        self.tableWidget.setColumnCount(self.data_int1)

        # 행값
        self.tableWidget.setRowCount(self.data_int2)


        # 행 갯수 칸 구성
        for i in range(0, self.data_int2):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)

        # 열 갯수 칸 구성
        for j in range(0, self.data_int1):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(j, item)




        # 안에 들어갈 데이터값 ui 구성
        for i in range(0, self.data_int2):
            for j in range(0, self.data_int1):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(i, j, item)


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))



        #데이터베이스 행값 열값 집어넣기




        # 행 번호 값 반복문
        for i in range(0, self.data_int2):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(str(i+1))

        # 열 값 반복문
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "번호"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "음식이름"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "가격"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "주문량"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)



        # 데이터베이스 데이터 집어넣기
        for i in range(0, self.data_int1):
            item = self.tableWidget.item(0, i)
            item.setText(str(self.res[i]))
            print(self.res[i])

        self.tableWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
