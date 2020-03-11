# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\jjy\storejjy\file1\ui1\lastgoodui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import sys, pymysql
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    # mysql에 연결시도
    def sqlConnect(self):
        try:
            self.conn = pymysql.connect \
                (host='192.168.0.7'
                 , port=3306, user='root'
                 , password='5284'
                 , db='project'
                 , charset='utf8')
        except:
            print("연결에 문제가있습니다.")
            exit(1)
        print("연결성공!")
        self.cursor = self.conn.cursor()

    # sql 데이터 셋 계산 - 열 갯수, 행 갯수, 데이터 값 불러오기
    def sqldata(self):
        Ui_MainWindow.sqlConnect(self)
        # 열 개수
        self.sql = """SELECT COUNT(*)
        FROM information_schema.columns WHERE table_name='menu';"""
        self.cursor.execute(self.sql)
        print(self.sql)
        self.res = self.cursor.fetchall()

        for self.data in self.res:
            self.data_list = (list(self.data))
            self.data_int = self.data_list[0]
            self.data_int1 = int(self.data_int)

        print(self.data_int1)

        # 행 개수
        self.sql2 = """select count(*) from menu;"""
        self.cursor.execute(self.sql2)
        self.res2 = self.cursor.fetchall()

        for self.data in self.res2:
            self.data_list = (list(self.data))
            self.data_int = self.data_list[0]
            self.data_int2 = int(self.data_int)

        print(self.data_int2)
        # 행이 data_int2, 열이 data_int1

        # 총 데이터베이스 출력
        self.sql3 = """select * from menu;"""
        self.cursor.execute(self.sql3)
        self.res3 = self.cursor.fetchall()

        for self.data in self.res3:
            print(self.data)

        # 데이터 하나씩 출력
        self.sql4 = """select *from menu limit 0, 1;"""
        self.cursor.execute(self.sql4)

        self.res = self.cursor.fetchone()
        print(self.res[0])
        self.result = self.cursor.fetchone()

        for self.data in self.res3:
            print(self.data)

        # 데이터 모두 하나씩 출력

        self.sql5 = ''' select *from menu'''
        self.cursor.execute(self.sql5)

        self.res5 = self.cursor.fetchall()
        self.res6 = self.cursor.fetchone()
        for i in range(0, len(self.res5)):
            for j in range(0, 4):
                print(self.res5[i][j])

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1171, 892)
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 830, 91, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 830, 91, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 830, 91, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 510, 91, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(180, 510, 91, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(290, 510, 91, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(480, 500, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(220, 120, 121, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(370, 120, 121, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(70, 120, 121, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 550, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setUnderline(True)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 200, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setUnderline(True)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(70, 590, 731, 231))
        self.tableWidget.setObjectName("tableWidget")

        # --1번째 테이블 음식리스트
        Ui_MainWindow.sqldata(self)
        self.tableWidget.setColumnCount(self.data_int1)  # 음식리스트 테이블의 열 갯수 설정
        self.tableWidget.setColumnWidth(0, 30)  # 1번테이블 셀의 길이조절
        self.tableWidget.setColumnWidth(1, 200)  # 1번테이블 셀의 길이조절
        self.tableWidget.setColumnWidth(2, 100)  # 1번 테이블 셀의 길이조절
        self.tableWidget.setColumnWidth(3, 126)  # 1번 테이블 셀의 길이조절
        self.tableWidget.setColumnWidth(4, 127)  # 1번 테이블 셀의 길이조절
        self.tableWidget.setColumnWidth(5, 127)  # 1번 테이블 셀의 길이조절

        self.tableWidget.setRowCount(self.data_int2)  # 음식리스트의 행 설정

        # 행의 갯수 칸 생성
        for i in range(0, self.data_int2):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)

        # 열 갯수 칸 구성
        for j in range(0, self.data_int1):
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            self.tableWidget.setHorizontalHeaderItem(j, item)

        # 안에 들어갈 데이터값 ui 구성
        for i in range(0, self.data_int2):
            for j in range(0, self.data_int1):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(i, j, item)

        # 2번째 테이블 구성
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(70, 240, 381, 261))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(2)

        # 만든 ui만큼 값을 집어넣을수 있는 2번 테이블 행 칸 생성
        for i in range(0, 2):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setVerticalHeaderItem(i, item)

        # 만든 ui만큼 값을 집어넣을수 있는 2번 테이블 열 칸 생성 1~5
        for i in range(0, 3):
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            self.tableWidget_2.setHorizontalHeaderItem(i, item)

        # 테이블 안에 칸 구성
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 0, item)

        # 세번째 주문내역 테이블
        self.tableWidget_3 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_3.setGeometry(QtCore.QRect(830, 110, 311, 741))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(3)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        self.todaysell = QtWidgets.QLCDNumber(self.centralwidget)
        self.todaysell.setGeometry(QtCore.QRect(580, 510, 211, 41))
        self.todaysell.setObjectName("todaysell")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(480, 240, 321, 261))
        self.calendarWidget.setObjectName("calendarWidget")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(980, 0, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(830, 70, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        font.setStrikeOut(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "추가"))
        self.pushButton_2.setText(_translate("MainWindow", "수정"))
        self.pushButton_3.setText(_translate("MainWindow", "삭제"))
        self.pushButton_4.setText(_translate("MainWindow", "추가"))
        self.pushButton_5.setText(_translate("MainWindow", "수정"))
        self.pushButton_6.setText(_translate("MainWindow", "삭제"))
        self.label.setText(_translate("MainWindow", "일일 매출:"))
        self.pushButton_7.setText(_translate("MainWindow", "한달 매출 그래프"))
        self.pushButton_8.setText(_translate("MainWindow", "연간 총 매출액"))
        self.pushButton_9.setText(_translate("MainWindow", "예측"))
        self.label_2.setText(_translate("MainWindow", "메뉴리스트"))
        self.label_3.setText(_translate("MainWindow", "재료리스트"))

        # 1번테이블 열에 값 넣기 음식리스트

        # 행 번호 값 반복문
        for i in range(0, self.data_int2):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(str(i + 1))

        # 음식테이블 열 값
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "번호"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "메뉴 명"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "가격"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "메뉴 레시피1"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "메뉴 레시피2"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "메뉴 레시피3"))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        # 음식테이블에 데이터 집어넣기

        for i in range(0, len(self.res5)):
            for j in range(0, len(self.res)):
                item = self.tableWidget.item(i, j)
                item.setText(str(self.res5[i][j]))
                print(self.res5[i][j])

        self.tableWidget.setSortingEnabled(__sortingEnabled)

        # 재료테이블에 행값 집어넣기
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))

        # 재료테이블 열값 집어넣기
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "번호"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "재료 명"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "재료 가격"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)

        # 재료테이블 셀에 데이터값 집어넣기
        item = self.tableWidget_2.item(0, 0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_2.item(0, 1)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_2.item(1, 0)
        item.setText(_translate("MainWindow", "1"))
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)

        # 3번테이블인 주문내역테이블의 열값 입력
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "주문시간"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "음식이름"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "가격"))

        # 3번테이블이 주문내역임을 나타낼수있는 레이블 네임
        self.label_4.setText(_translate("MainWindow", "주문내역"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
