# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'D:\jjy\storejjy\file1\ui1\lastgoodui.ui'
from PyQt5.QtWidgets import QLabel

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from new3.sql_and_query import pysql
from new3.dialog1 import startdia1


class Ui_MainWindow():

    # ----------------------------UI 구성요소----------------------------------#
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1350, 900)
        font = QtGui.QFont()
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ---------------------추가 수정 삭제 버튼ui와 함수연동부분-----------------------#
        # 메인메뉴 추가버튼 함수 연동
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 830, 91, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.menu_add)  # 함수연동문

        # 메인메뉴 수정버튼 함수 연동
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 830, 91, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.menu_mod)  # 함수연동문

        # 메인메뉴 삭제버튼 함수 연동
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 830, 91, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.menu_del)  # 함수연동문

        # 재료 추가버튼 함수 연동
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 510, 91, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.ingre_add)  # 함수연동문

        # 재료 수정버튼 함수 연동
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(180, 510, 91, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.ingre_mod)  # 함수연동문

        # 재료 삭제버튼 함수연동
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(290, 510, 91, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.ingre_del)  # 함수연동문
        # ----------------------추가삭제수정버튼은 끝--------------------------#

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(480, 500, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # ---------------------------월간, 연간, 미래예측버튼 ui와 연동부분----------------#
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(220, 120, 121, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.one_month_sales)  # 함수연동문

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(370, 120, 121, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.one_year_sales)  # 함수연동문

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(70, 120, 121, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.future_predict)  # 함수연동문

        # -------------------------나머지 버튼 기능연동끝-------------------------#

        # 메뉴리스트레이블 폰트 및 레이블 형식
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 550, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        # 재료리스트레이블 폰트 및 레이블 형식
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 200, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(70, 590, 731, 231))
        self.tableWidget.setObjectName("tableWidget")

        # --------------------------1번째 테이블 음식리스트 gui구성---------------------------#

        # -----------------mysql 데이터베이스 값 불러오기-----------#
        pysql.sqldata(self)
        ##############################################

        self.tableWidget.setColumnCount(self.data_int1)  # 음식리스트 테이블의 열 갯수 설정

        self.tableWidget.setColumnWidth(0, 209)  # 1번테이블 셀의 길이조절
        self.tableWidget.setColumnWidth(1, 100)  # 1번 테이블 셀의 길이조절
        self.tableWidget.setColumnWidth(2, 135)  # 1번 테이블 셀의 길이조절
        self.tableWidget.setColumnWidth(3, 135)  # 1번 테이블 셀의 길이조절
        self.tableWidget.setColumnWidth(4, 135)  # 1번 테이블 셀의 길이조절

        self.tableWidget.setRowCount(self.data_int2)  # 음식리스트의 행 설정

        # 행의 갯수 gui칸 생성
        for i in range(0, self.data_int2):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)

        # 열 갯수 gui칸 구성
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

        # ----------------------2번째 재료 테이블 구성-------------------------#
        # 2번째 테이블 구성
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(70, 240, 381, 261))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(self.ingrecol)

        self.tableWidget_2.setColumnWidth(0, 244)  # 2번 재료테이블 2번 열의 길이조절
        self.tableWidget_2.setColumnWidth(1, 120)  # 2번 재료테이블 3번 열의 길이조절

        self.tableWidget_2.setRowCount(self.foodrow)

        # 만든 ui만큼 값을 집어넣을수 있는 2번 테이블 행 칸 생성
        for i in range(0, self.foodrow):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setVerticalHeaderItem(i, item)

        # 만든 ui만큼 값을 집어넣을수 있는 2번 테이블 열 칸 생성 1~5
        for i in range(0, self.ingrecol):
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            self.tableWidget_2.setHorizontalHeaderItem(i, item)

        # 테이블 안에 칸 구성
        for i in range(0, self.foodrow):
            for j in range(0, self.ingrecol):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget_2.setItem(i, j, item)

        # ---------------------------세번째 주문내역 UI테이블 구성-------------------------#
        # 세번째 주문내역 테이블
        self.tableWidget_3 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_3.setGeometry(QtCore.QRect(830, 110, 450, 741))
        self.tableWidget_3.setObjectName("tableWidget_3")

        # 행의 갯수 생성
        self.tableWidget_3.setColumnCount(self.salecol)

        # 열의 갯수 생성
        self.tableWidget_3.setRowCount(self.salerow)

        self.tableWidget_3.setColumnWidth(0, 150)  # 2번 재료테이블 2번 열의 길이조절
        self.tableWidget_3.setColumnWidth(1, 160)  # 2번 재료테이블 3번 열의 길이조절
        self.tableWidget_3.setColumnWidth(2, 160)  # 2번 재료테이블 3번 열의 길이조절
        self.tableWidget_3.setColumnWidth(3, 100)  # 2번 재료테이블 3번 열의 길이조절

        # 주문내역 테이블 열값 내부 폰트 및 설정값 생성
        for i in range(0, self.salecol):
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            self.tableWidget_3.setHorizontalHeaderItem(i, item)

        # 주문내역 행값 생성
        for i in range(0, self.salerow):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_3.setVerticalHeaderItem(i, item)

        # 주문내역테이블 안에 칸 구성
        for i in range(0, self.salerow):
            for j in range(0, self.salecol):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget_3.setItem(i, j, item)

        # ------------------------------일일 판매량 UI 구성----------------------------#
        self.todaysell = QtWidgets.QLCDNumber(self.centralwidget)
        self.todaysell.setGeometry(QtCore.QRect(580, 510, 211, 41))
        self.todaysell.setObjectName("todaysell")

        # -----------------------------달력위젯 UI구성--------------------------------#
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(480, 240, 321, 261))
        self.calendarWidget.setObjectName("calendarWidget")

        # ----------------------------시계위젯 UI구성---------------------------------#
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(980, 0, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")

        # --------------------------주문테이블표시 UI 레이블-----------------------------#
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(830, 70, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        # --------------------------닫기 버튼----------------------------------#
        # closebtn = self.QPushButton("close window", self)
        # closebtn.resize(# closebtn.sizeHint())
        # closebtn.move(100,300)
        # closebtn.clicked.connect(QCoreApplication.instance().quit)

        # -----------------------retranslateUi 인스턴스에서 설정을 불러온다------------------------#
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.explain1()  # 툴팁생성
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # def closeEvent(self,QCloseEvent):
    #     ans = QMessageBox.question(self,"종료확인", "종료 하시겠습니까?",
    #                                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    #     if ans == QMessageBox.Yes:
    #         QCloseEvent.accept()
    #     else:
    #         QCloseEvent.ignore()

    def retranslateUi(self, MainWindow):
        # ------------------------------버튼들 이름 설정----------------------------#
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "메뉴추가"))
        self.pushButton_2.setText(_translate("MainWindow", "메뉴수정"))
        self.pushButton_3.setText(_translate("MainWindow", "메뉴삭제"))
        self.pushButton_4.setText(_translate("MainWindow", "재료추가"))
        self.pushButton_5.setText(_translate("MainWindow", "재료수정"))
        self.pushButton_6.setText(_translate("MainWindow", "재료삭제"))
        self.label.setText(_translate("MainWindow", "일일 매출:"))
        self.pushButton_7.setText(_translate("MainWindow", "한달 매출 그래프"))
        self.pushButton_8.setText(_translate("MainWindow", "연간 총 매출액"))
        self.pushButton_9.setText(_translate("MainWindow", "예측"))
        self.label_2.setText(_translate("MainWindow", "메뉴리스트"))
        self.label_3.setText(_translate("MainWindow", "재료리스트"))
        self.label_4.setText(_translate("MainWindow", "주문내역리스트"))

        # 1번테이블 열에 값 넣기 음식리스트
        # 행 번호 값 반복문
        for i in range(0, self.data_int2):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(str(i + 1))

        # 음식테이블 열 값

        for i in range(0, len(self.menu_list)):
            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(_translate("MainWindow", self.menu_list[i]))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        # 음식테이블에 데이터 집어넣기

        for i in range(0, len(self.res5)):
            for j in range(0, self.data_int1):
                item = self.tableWidget.item(i, j)
                item.setText(str(self.res5[i][j]))
                print(self.res5[i][j])

        self.tableWidget.setSortingEnabled(__sortingEnabled)

        # ------------------------2번 재료테이블 값 구성------------------------#
        # 재료테이블에 행값 집어넣기

        for i in range(0, self.foodrow):
            item = self.tableWidget_2.verticalHeaderItem(i)
            item.setText(str(i + 1))

        # 재료테이블 열값 집어넣기
        for i in range(0, len(self.ingredient_list)):
            item = self.tableWidget_2.horizontalHeaderItem(i)
            item.setText(_translate("MainWindow", self.ingredient_list[i]))

        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)

        # 재료테이블 셀에 데이터값 집어넣기
        for i in range(0, len(self.foodtableall)):
            for j in range(0, self.ingrecol):
                item = self.tableWidget_2.item(i, j)
                item.setText(str(self.foodtableall[i][j]))
                print(self.foodtableall[i][j])

        self.tableWidget_2.setSortingEnabled(__sortingEnabled)

        # --------------------------3번테이블 주문내역 테이블 값-------------------#
        # 3번테이블인 주문내역테이블의 행값 입력

        for i in range(0, self.salerow):
            item = self.tableWidget_3.verticalHeaderItem(i)
            item.setText(str(i + 1))

        # 주문내역 테이블 열값입력
        for i in range(0, len(self.sale_list)):
            item = self.tableWidget_3.horizontalHeaderItem(i)
            item.setText(_translate("MainWindow", self.sale_list[i]))

        for i in range(0, len(self.saletableall)):
            for j in range(0, self.salecol):
                item = self.tableWidget_3.item(i, j)
                item.setText(str(self.saletableall[i][j]))
                print(self.saletableall[i][j])

        self.tableWidget_2.setSortingEnabled(__sortingEnabled)

        # 3번테이블이 주문내역임을 나타낼수있는 레이블 네임

    # ---------------------------마우스커서를 갖다대면 나오는 툴팁----------------------#
    def explain1(self):
        self.pushButton.setToolTip('메뉴추가툴팁')  # 발주 추가버튼 툴팁
        self.pushButton_2.setToolTip('메뉴수정툴팁')  # 발주 수정툴팁 버튼
        self.pushButton_3.setToolTip('메뉴삭제툴팁')  # 발주 삭제버튼 툴팁
        self.pushButton_4.setToolTip('재료추가')
        self.pushButton_5.setToolTip('재료수정')
        self.pushButton_6.setToolTip('재료삭제')
        self.pushButton_7.setToolTip('한달매출')
        self.pushButton_8.setToolTip('연간매출')
        self.pushButton_9.setToolTip('예측')

    def menu_add(self):
        print("1")

        startdia1().startdialog
        print("2")
        # self.app = QtWidgets.QApplication(sys.argv)
        #
        # self.setWindowTitle("window name")
        # self.setGeometry(300, 300, 300, 300)
        #
        # label = QLabel("Hello PyQt")
        # label.show()
        # self.app.exec_()

    #     print("메뉴추가버튼기능입니다")
    #     app = QtWidgets.QApplication(sys.argv)
    #     Dialog = QtWidgets.QDialog()
    #
    #     Dialog.setObjectName("Dialog")
    #     Dialog.resize(480, 640)
    #
    #     self.dialogs(Dialog)
    #
    #     QtCore.QMetaObject.connectSlotsByName(Dialog)
    #
    #     Dialog.show()
    #     sys.exit(app.exec_())
    #
    # def dialogs(self, Dialog):
    #     _translate = QtCore.QCoreApplication.translate
    #     Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

    # ---------------메뉴수정 버튼기능구현함수입니다-------------#
    def menu_mod(self):
        print("메뉴수정버튼기능입니다.")

    # ---------------메뉴삭제 버튼기능구현함수입니다-------------#
    def menu_del(self):
        print("메뉴삭제버튼기능입니다.")

    # ---------------재료추가 버튼기능구현함수입니다-------------#
    def ingre_add(self):
        print("재료추가버튼기능입니다.")

    # ---------------재료수정 버튼기능구현함수입니다-------------#
    def ingre_mod(self):
        print("재료수정버튼기능입니다.")

    # ---------------재료삭제 버튼기능구현함수입니다-------------#
    def ingre_del(self):
        print("재료삭제버튼기능입니다.")

    # ---------------월간판매량 버튼기능구현함수입니다-------------#
    def one_month_sales(self):
        print("월간판매량입니다.")

    # ---------------연간판매량 버튼기능구현함수입니다-------------#
    def one_year_sales(self):
        print("연간판매량입니다.")

    # ---------------미래예측 버튼기능구현함수입니다-------------#
    def future_predict(self):
        print("미래예측입니다?")
