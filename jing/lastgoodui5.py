# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'D:\jjy\storejjy\file1\ui1\lastgoodui.ui'



import sys, pymysql

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    # ------------------------mysql에 연결시도----------------------#
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

        self.foodcolnum = 5; #음식테이블의 열 갯수
        self.ingrecolnum = 2; #재료테이블의 열 갯수
        self.salecol = 4; #주문내역
        Ui_MainWindow.sqlConnect(self)

        #------------------------음식테이블 재료추출----------------------#
        # 열 개수
        sql = """SELECT COUNT(*)
        FROM information_schema.columns WHERE table_name='menu';"""
        self.cursor.execute(sql)
        res = self.cursor.fetchall()

        for data in res:
            data_list = (list(data))
            data_int = data_list[0]
            self.data_int1 = int(data_int)

        print(self.data_int1)

        # 행 개수
        sql2 = """select count(*) from menu;"""
        self.cursor.execute(sql2)
        res2 = self.cursor.fetchall()

        for i in res2:
            data_list = (list(i))
            data_int = data_list[0]
            self.data_int2 = int(data_int)

        print(self.data_int2)
        # 행이 data_int2, 열이 data_int1

        # 총 데이터베이스 출력
        sql3 = """select * from menu;"""
        self.cursor.execute(sql3)
        res3 = self.cursor.fetchall()

        for i in res3:
            print(i)

        # 데이터 하나씩 출력
        sql4 = """select *from menu limit 0, 1;"""
        self.cursor.execute(sql4)

        self.res4 = self.cursor.fetchone()
        for i in self.res4:
            print(i)


        # 데이터 모두 하나씩 출력

        self.sql5 = ''' select *from menu'''
        self.cursor.execute(self.sql5)

        self.res5 = self.cursor.fetchall()
        self.res6 = self.cursor.fetchone()
        for i in range(0, len(self.res5)):
            for j in range(0, self.foodcolnum):
                print(self.res5[i][j])

        #---------------------------재료테이블 데이터 추출 2번째 테이블------------------------#
        # 재료테이블 행 개수
        self.재료테이블행개수sql = """select count(*) from ingredient;"""
        self.cursor.execute(self.재료테이블행개수sql)
        self.res7 = self.cursor.fetchall()

        for i in self.res7:
            data_list = (list(i))
            data_int = data_list[0]
            self.foodrow = int(data_int)

        print(self.foodrow)


        #재료테이블 데이터 하나씩출력
        #데이터 모두 하나씩 출력
        self.재료테이블하나씩출력하는sql문 = ''' select *from ingredient'''
        self.cursor.execute(self.재료테이블하나씩출력하는sql문)

        self.foodtableall = self.cursor.fetchall()
        for i in range(0, len(self.foodtableall)):
            for j in range(0, self.ingrecolnum):
                print(self.foodtableall[i][j])


        #---------------------------주문내역 테이블-----------------------------#
        # 열 개수 --일단안됨


        self.주문내역테이블열개수 = """SELECT COUNT(*)
                FROM information_schema.columns WHERE table_name='sales';"""
        self.cursor.execute(self.주문내역테이블열개수)
        self.res10 = self.cursor.fetchall()

        for data in self.res10:
            data_list = (list(data))
            data_int = data_list[0]
            self.salecols = int(data_int)

        print(self.salecols)

        # 주문내역테이블 행 개수
        self.주문내역테이블행개수 = """select count(*) from sales;"""
        self.cursor.execute(self.주문내역테이블행개수)
        self.res11 = self.cursor.fetchall()

        for data1 in self.res11:
            data_list = (list(data1))
            data_int = data_list[0]
            self.salerow = int(data_int)

        print(self.salerow)
        # 열이 salecols, 행이 salerow




        #데이터 모두 하나씩 출력

        self.데이터모두하나씩출력 = ''' select * from sales;'''
        self.cursor.execute(self.데이터모두하나씩출력)

        self.saletableall = self.cursor.fetchall()
        for i in range(0, len(self.saletableall)):
            for j in range(0, self.salecols):
                print(self.saletableall[i][j])


    #----------------------------UI 구성요소----------------------------------#
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1350, 900)
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #---------------------추가 수정 삭제 버튼ui와 함수연동부분-----------------------#
        #메인메뉴 추가버튼 함수 연동
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 830, 91, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.menu_add) #함수연동문


        #메인메뉴 수정버튼 함수 연동
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 830, 91, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.menu_mod) #함수연동문

        #메인메뉴 삭제버튼 함수 연동
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 830, 91, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.menu_del) #함수연동문

        #재료 추가버튼 함수 연동
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 510, 91, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.ingre_add) #함수연동문

        #재료 수정버튼 함수 연동
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(180, 510, 91, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.ingre_mod) #함수연동문

        #재료 삭제버튼 함수연동
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(290, 510, 91, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.ingre_del) #함수연동문
        #----------------------추가삭제수정버튼은 끝--------------------------#

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

        #---------------------------월간, 연간, 미래예측버튼 ui와 연동부분----------------#
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(220, 120, 121, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.one_month_sales) #함수연동문

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(370, 120, 121, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.one_year_sales) #함수연동문

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(70, 120, 121, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.future_predict) #함수연동문

        #-------------------------나머지 버튼 기능연동끝-------------------------#

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

        # --------------------------1번째 테이블 음식리스트---------------------------#
        Ui_MainWindow.sqldata(self)
        self.tableWidget.setColumnCount(self.data_int1)  # 음식리스트 테이블의 열 갯수 설정

        self.tableWidget.setColumnWidth(0, 209)  # 1번테이블 셀의 길이조절
        self.tableWidget.setColumnWidth(1, 100)  # 1번 테이블 셀의 길이조절
        self.tableWidget.setColumnWidth(2, 135)  # 1번 테이블 셀의 길이조절
        self.tableWidget.setColumnWidth(3, 135)  # 1번 테이블 셀의 길이조절
        self.tableWidget.setColumnWidth(4, 135)  # 1번 테이블 셀의 길이조절

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
            for j in range(0, self.foodcolnum):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(i, j, item)



        #----------------------2번째 재료 테이블 구성-------------------------#
        # 2번째 테이블 구성
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(70, 240, 381, 261))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(self.ingrecolnum)


        self.tableWidget_2.setColumnWidth(0, 244)  # 2번 재료테이블 2번 열의 길이조절
        self.tableWidget_2.setColumnWidth(1, 120)  # 2번 재료테이블 3번 열의 길이조절

        self.tableWidget_2.setRowCount(self.foodrow)

        # 만든 ui만큼 값을 집어넣을수 있는 2번 테이블 행 칸 생성
        for i in range(0, self.foodrow):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setVerticalHeaderItem(i, item)

        # 만든 ui만큼 값을 집어넣을수 있는 2번 테이블 열 칸 생성 1~5
        for i in range(0, self.ingrecolnum):
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
            for j in range(0,self.ingrecolnum):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget_2.setItem(i, j, item)



        #---------------------------세번째 주문내역 UI테이블 구성-------------------------#
        # 세번째 주문내역 테이블
        self.tableWidget_3 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_3.setGeometry(QtCore.QRect(830, 110, 450, 741))
        self.tableWidget_3.setObjectName("tableWidget_3")



        #행의 갯수 생성
        self.tableWidget_3.setColumnCount(self.salecols)

        #열의 갯수 생성
        self.tableWidget_3.setRowCount(self.salerow)

        self.tableWidget_3.setColumnWidth(0, 150)  # 2번 재료테이블 2번 열의 길이조절
        self.tableWidget_3.setColumnWidth(1, 160)  # 2번 재료테이블 3번 열의 길이조절
        self.tableWidget_3.setColumnWidth(2, 160)  # 2번 재료테이블 3번 열의 길이조절
        self.tableWidget_3.setColumnWidth(3, 100)  # 2번 재료테이블 3번 열의 길이조절

        #주문내역 테이블 열값 내부 폰트 및 설정값 생성
        for i in range(0, self.salecols):
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            self.tableWidget_3.setHorizontalHeaderItem(i, item)

        #주문내역 행값 생성
        for i in range(0, self.salerow):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_3.setVerticalHeaderItem(i, item)

        # 주문내역테이블 안에 칸 구성
        for i in range(0, self.salerow):
            for j in range(0, self.salecols):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget_3.setItem(i, j, item)

        #------------------------------일일 판매량 UI 구성----------------------------#
        self.todaysell = QtWidgets.QLCDNumber(self.centralwidget)
        self.todaysell.setGeometry(QtCore.QRect(580, 510, 211, 41))
        self.todaysell.setObjectName("todaysell")

        #-----------------------------달력위젯 UI구성--------------------------------#
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(480, 240, 321, 261))
        self.calendarWidget.setObjectName("calendarWidget")

        #----------------------------시계위젯 UI구성---------------------------------#
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(980, 0, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")

        #--------------------------주문테이블표시 UI 레이블-----------------------------#
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(830, 70, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        font.setStrikeOut(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        #--------------------------닫기 버튼----------------------------------#
        # closebtn = self.QPushButton("close window", self)
        # closebtn.resize(# closebtn.sizeHint())
        # closebtn.move(100,300)
        # closebtn.clicked.connect(QCoreApplication.instance().quit)



        #-----------------------retranslateUi 인스턴스에서 설정을 불러온다------------------------#
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #self.MainWindow.explain1(1) #툴팁생성
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
        #------------------------------버튼들 이름 설정----------------------------#
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


        # 1번테이블 열에 값 넣기 음식리스트
        # 행 번호 값 반복문
        for i in range(0, self.data_int2):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(str(i + 1))


        # 음식테이블 열 값

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "메뉴 명"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "가격"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "메뉴 레시피1"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "메뉴 레시피2"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "메뉴 레시피3"))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)



        # 음식테이블에 데이터 집어넣기

        for i in range(0, len(self.res5)):
            for j in range(0, self.foodcolnum):
                item = self.tableWidget.item(i, j)
                item.setText(str(self.res5[i][j]))
                print(self.res5[i][j])

        self.tableWidget.setSortingEnabled(__sortingEnabled)


        #------------------------2번 재료테이블 값 구성------------------------#
        # 재료테이블에 행값 집어넣기

        for i in range(0, self.foodrow):
            item = self.tableWidget_2.verticalHeaderItem(i)
            item.setText(str(i + 1))

        # 재료테이블 열값 집어넣기

        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "재료 명"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "재료 가격"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)

        # 재료테이블 셀에 데이터값 집어넣기
        for i in range(0, len(self.foodtableall)):
            for j in range(0, self.ingrecolnum):
                item = self.tableWidget_2.item(i, j)
                item.setText(str(self.foodtableall[i][j]))
                print(self.foodtableall[i][j])



        self.tableWidget_2.setSortingEnabled(__sortingEnabled)


        #--------------------------3번테이블 주문내역 테이블 값-------------------#
        # 3번테이블인 주문내역테이블의 열값 입력

        for i in range(0, self.salerow):
            item = self.tableWidget_3.verticalHeaderItem(i)
            item.setText(str(i + 1))


        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "주문내역"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "주문완료시간"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "주문처리시간"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "가격"))

        for i in range(0, len(self.saletableall)):
            for j in range(0, self.salecol):
                item = self.tableWidget_3.item(i, j)
                item.setText(str(self.saletableall[i][j]))
                print(self.saletableall[i][j])



        self.tableWidget_2.setSortingEnabled(__sortingEnabled)

        # 3번테이블이 주문내역임을 나타낼수있는 레이블 네임
        self.label_4.setText(_translate("MainWindow", "주문내역"))

    def explain1(self, MainWindow):
        self.pushButton.setToolTip('메뉴추가툴팁')  # 발주 추가버튼 툴팁
        self.pushButton_2.setToolTip('메뉴수정툴팁')  # 발주 수정툴팁 버튼
        self.pushButton_3.setToolTip('메뉴삭제툴팁')  # 발주 삭제버튼 툴팁
        self.pushButton_4.setToolTip('재료추가')
        self.pushButton_5.setToolTip('재료수정')
        self.pushButton_6.setToolTip('재료삭제')
        self.pushButton_7.setToolTip('한달매출')
        self.pushButton_8.setToolTip('연간매출')
        self.pushButton_9.setToolTip('예측')

    #---------------메뉴추가 버튼기능구현함수입니다-------------#
    def menu_add(self):
        print("메뉴추가버튼기능입니다")
        items = ("선택1", "선택2")
        self.QInputDialog.getItem(self, "과목 선택", "과목을 선택하세요.", items, 0, False)

            #self.lineEdit.setText()

    #---------------메뉴수정 버튼기능구현함수입니다-------------#
    def menu_mod(self):
        print("메뉴수정버튼기능입니다.")

    #---------------메뉴삭제 버튼기능구현함수입니다-------------#
    def menu_del(self):
        print("메뉴삭제버튼기능입니다.")

    #---------------재료추가 버튼기능구현함수입니다-------------#
    def ingre_add(self):
        print("재료추가버튼기능입니다.")

    #---------------재료수정 버튼기능구현함수입니다-------------#
    def ingre_mod(self):
        print("재료수정버튼기능입니다.")

    #---------------재료삭제 버튼기능구현함수입니다-------------#
    def ingre_del(self):
        print("재료삭제버튼기능입니다.")
    #---------------월간판매량 버튼기능구현함수입니다-------------#
    def one_month_sales(self):
        print("월간판매량입니다.")

    #---------------연간판매량 버튼기능구현함수입니다-------------#
    def one_year_sales(self):
        print("연간판매량입니다.")


    #---------------미래예측 버튼기능구현함수입니다-------------#
    def future_predict(self):
        print("미래예측입니다?")




#--------------------------------실행------------------------------#
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
