from PyQt5.QtCore import QDateTime
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtWidgets, QtCore

from new8.mn_del import mn_del
from new8.ing_add import ing_add
from new8.ing_mod import ing_mod

from new8.mn_ins import mn_add
from new8.ing_del import ing_del
# from new8.month_sale_button import month_graph
# from new8.month_sale_button import year_graph
from new8.mn_mod import mn_mod
# from new8.tensor_predict import graph_pri

global w
global ip,pt,name,pwd,dbname,char_type
from new8.server_ms import *
from new8.sql_and_query import *





class Ui_MainWindow(QMainWindow,threading.Thread):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-image: url(new8/pepe.jpg)")


    # ----------------------------UI 구성요소----------------------------------#
    def setupUi(self, MainWindow):


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1350, 900)
        font = QtGui.QFont()
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #----------------------팀명 레이블------------------------------------#


        self.team_label = QtWidgets.QLabel(self.centralwidget)
        self.team_label.setGeometry(QtCore.QRect(70, 20, 300, 150))

        font = QtGui.QFont()
        font.setFamily("Mapo꽃섬")
        font.setPointSize(60)
        font.setWeight(50)
        self.team_label.setFont(font)
        self.team_label.setObjectName("nick")

        # self.label_change_Button = QtWidgets.QPushButton(self.centralwidget)
        # self.label_change_Button.setGeometry(QtCore.QRect(70, 20, 261, 101))
        # self.label_change_Button.setText("")
        # self.label_change_Button.setFlat(True)
        # self.label_change_Button.setObjectName("pushButton")
        # self.label_change_Button.clicked.connect(self.chglabel)

        # ---------------------추가 수정 삭제 버튼ui와 함수연동부분-----------------------#
        #sql문 연동


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

        #메뉴gui설정
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
        self.pushButton_7.setGeometry(QtCore.QRect(500, 60, 121, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.one_month_sales)  # 함수연동문

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(670, 60, 121, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.one_year_sales)  # 함수연동문

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(500, 120, 121, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.future_predict)  # 함수연동문

        self.label_change_Button = QtWidgets.QPushButton(self.centralwidget)
        self.label_change_Button.setGeometry(QtCore.QRect(70, 20, 300, 150))
        self.label_change_Button.setText("")
        self.label_change_Button.setFlat(True)
        self.label_change_Button.setObjectName("pushButton")
        self.label_change_Button.clicked.connect(self.chglable)

        # self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_11.setGeometry(QtCore.QRect(520, 60, 121, 41))
        # self.pushButton_11.setObjectName("pushButton_11")
        # self.pushButton_11.clicked.connect(self.chglable)  # 함수연동문

        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(670, 120, 121, 41))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(self.thread_refresh_all)  # 함수연동문




        # -------------------------나머지 버튼 기능연동끝-------------------------#

        # 재료리스트레이블 폰트 및 레이블 형식
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 550, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        # 판매내역리스트레이블 폰트 및 레이블 형식
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 200, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")




        # --------------------------1번째 테이블 음식리스트 gui구성---------------------------#

        pysql.sqldata(self)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(70, 590, 731, 231))
        self.tableWidget.setObjectName("tableWidget")

        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(70, 240, 381, 261))
        self.tableWidget_2.setObjectName("tableWidget_2")

        self.tableWidget_3 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_3.setGeometry(QtCore.QRect(830, 110, 450, 741))
        self.tableWidget_3.setObjectName("tableWidget_3")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(70, 590, 731, 231))
        self.tableWidget.setObjectName("tableWidget")

        self.tableWidget.setColumnCount(self.data_int1)  # 음식리스트 테이블의 열 갯수 설정

        self.tableWidget.setColumnWidth(0, 209)  # 1번테이블 셀의 길이조절
        self.tableWidget.setColumnWidth(1, 100)  # 1번 테이블 셀의 길이조절
        self.tableWidget.setColumnWidth(2, 135)  # 1번 테이블 셀의 길이조절
        self.tableWidget.setColumnWidth(3, 110)  # 1번 테이블 셀의 길이조절
        self.tableWidget.setColumnWidth(4, 135)  # 1번 테이블 셀의 길이조절
        self.tableWidget.setColumnWidth(5, 110)  # 1번 테이블 셀의 길이조절
        self.tableWidget.setColumnWidth(6, 135)  # 1번 테이블 셀의 길이조절
        self.tableWidget.setColumnWidth(7, 110)  # 1번 테이블 셀의 길이조절

        self.tableWidget.setRowCount(self.data_int2)  # 음식리스트의 행 설정

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

        self.tableWidget_2.setColumnWidth(0, 240)  # 2번 재료테이블 2번 열의 길이조절
        self.tableWidget_2.setColumnWidth(1, 128)  # 2번 재료테이블 3번 열의 길이조절

        self.tableWidget_2.setRowCount(self.foodrow)


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

        #--------------------------테이블 설정-------------------------------#
        # 주문내역 테이블 열값 내부 폰트 및 설정값 생성, 정렬
        for i in range(0, self.salecol):
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            self.tableWidget_3.setHorizontalHeaderItem(i, item)


        # 주문내역테이블 안에 칸 구성
        for i in range(0, self.salerow):
            for j in range(0, self.salecol):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget_3.setItem(i, j, item)




        # ------------------------------일일 판매량 UI 구성----------------------------#
        self.todaysell = QtWidgets.QLCDNumber(self.centralwidget)
        self.todaysell.setGeometry(QtCore.QRect(580, 510, 211, 41))
        self.todaysell.setDigitCount(10)
        self.todaysell.setObjectName("todaysell")

        # -----------------------------달력위젯 UI구성--------------------------------#
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(480, 240, 321, 261))
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.clicked.connect(self.thread_click)

        # ----------------------------시계위젯 UI구성---------------------------------#
        self.timertime = QtCore.QTimer()
        self.timertime.setInterval(1000)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(980, 0, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.timertime.timeout.connect(self.Qtimewidget)
        self.timertime.start()

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


        # -----------------------retranslateUi 함수에서 설정을 불러온다------------------------#


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.explain1()  # 툴팁생성

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #-------------------Qtimer로 시간을 리프레쉬시킬수 있도록 만든 함수-----------------#
    def Qtimewidget(self):
        self.currentDateTime = QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(self.currentDateTime)
        self.dateTimeEdit.repaint()

    def retranslateUi(self, MainWindow):
        # ------------------------------버튼들 이름 설정----------------------------#
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "메뉴추가"))
        self.pushButton_2.setText(_translate("MainWindow", "가격수정"))
        self.pushButton_3.setText(_translate("MainWindow", "메뉴삭제"))
        self.pushButton_4.setText(_translate("MainWindow", "재료추가"))
        self.pushButton_5.setText(_translate("MainWindow", "재료발주"))
        self.pushButton_6.setText(_translate("MainWindow", "재료삭제"))
        self.label.setText(_translate("MainWindow", "일일 매출:"))
        self.pushButton_7.setText(_translate("MainWindow", "한달 매출 그래프"))
        self.pushButton_8.setText(_translate("MainWindow", "연간 총 매출액"))
        self.pushButton_9.setText(_translate("MainWindow", "예측"))

        # self.pushButton_11.setText(str("누르면 팀명바뀜"))
        self.pushButton_12.setText(str("새로고침"))
        self.label_2.setText(_translate("MainWindow", "메뉴리스트"))
        self.label_3.setText(_translate("MainWindow", "재료리스트"))
        self.label_4.setText(_translate("MainWindow", "주문내역리스트"))
        self.team_label.setText(str("긴하진순"))

        self.todaysell.display(self.todaysellm)

        # 음식테이블 열 값입력

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

        self.tableWidget.setSortingEnabled(__sortingEnabled)

        # ------------------------2번 재료테이블 값 구성------------------------#

        # 재료테이블 열 값
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

        self.tableWidget_2.setSortingEnabled(__sortingEnabled)

        # --------------------------3번테이블 주문내역 테이블 값-------------------#
        # 3번테이블인 주문내역테이블의 행값 입력

        # 주문내역 테이블 열값
        for i in range(0, len(self.sale_list)):
            item = self.tableWidget_3.horizontalHeaderItem(i)
            item.setText(_translate("MainWindow", self.sale_list[i]))

        for i in range(0, len(self.saletableall)):
            for j in range(0, self.salecol):
                item = self.tableWidget_3.item(i, j)
                item.setText(str(self.saletableall[i][j]))

        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        # 3번테이블이 주문내역임을 나타낼수있는 레이블 네임

    # ---------------------------마우스커서를 갖다대면 나오는 툴팁----------------------#
    def explain1(self):
        self.pushButton.setToolTip('메뉴추가툴팁')  # 발주 추가버튼 툴팁
        self.pushButton_2.setToolTip('가격수정툴팁')  # 발주 수정툴팁 버튼
        self.pushButton_3.setToolTip('메뉴삭제툴팁')  # 발주 삭제버튼 툴팁
        self.pushButton_4.setToolTip('재료추가')
        self.pushButton_5.setToolTip('재료수정')
        self.pushButton_6.setToolTip('재료삭제')
        self.pushButton_7.setToolTip('한달매출')
        self.pushButton_8.setToolTip('연간매출')
        self.pushButton_9.setToolTip('예측')


    def thread_click(self):
        a = threading.Thread(target=self.click_print)
        a.start()

    #캘린더 위젯 날짜클릭시 테이블 바뀜
    def click_print(self):
        test = self.calendarWidget.selectedDate()
        self.calendar_select=test.toPyDate()
        print(self.calendar_select)

        pysql.sqlConnect(self)
        # ---------------------------주문내역 테이블-----------------------------#
        # 열 개수 --일단안됨

        self.주문내역테이블열개수 = """SELECT count(COLUMN_NAME)
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = SCHEMA()
        AND TABLE_NAME = '판매내역' ORDER BY ORDINAL_POSITION;"""
        self.cursor.execute(self.주문내역테이블열개수)
        self.res10 = self.cursor.fetchall()

        for data in self.res10:
            data_list = (list(data))
            data_int = data_list[0]
            self.salecol = int(data_int)


        # 주문내역테이블 행 개수
        self.주문내역테이블행개수 = """select count(*) from 판매내역 where date(주문시간)=%s;"""
        self.cursor.execute(self.주문내역테이블행개수,self.calendar_select)
        self.res11 = self.cursor.fetchall()

        for data1 in self.res11:
            data_list = (list(data1))
            data_int = data_list[0]
            self.salerow = int(data_int)

        # 열이 salecol, 행이 salerow

        # 데이터 모두 하나씩 출력

        self.데이터모두하나씩출력 = ''' select * from 판매내역 where date(주문시간)=%s;'''
        self.cursor.execute(self.데이터모두하나씩출력,self.calendar_select)

        self.saletableall = self.cursor.fetchall()
        # 일단 임의로 지정한 열갯수


        self.column_print = """SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = SCHEMA()
        AND TABLE_NAME = '판매내역' ORDER BY ORDINAL_POSITION;"""

        self.cursor.execute(self.column_print)

        sales = self.cursor.fetchall()
        self.sale_list = [x[0] for x in sales]

        #----------------일일매출----------------------#
        일일매출 = """select sum(메뉴가격) from 판매내역 where date(주문시간)=%s;"""
        self.cursor.execute(일일매출, self.calendar_select)
        todaysell = self.cursor.fetchone()

        print(todaysell)

        if todaysell == (None,):
            self.todaysellm = 0
        else:
            data_list=list(todaysell)
            data_int=data_list[0]
            self.todaysellm=int(data_int)


        self.tableWidget_3.clearContents()
        self.tableWidget_3.setRowCount(self.salerow)

        for i in range(0, len(self.saletableall)):
            for j in range(0, self.salecol):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget_3.setItem(i, j, item)
                item = self.tableWidget_3.item(i, j)
                item.setText(str(self.saletableall[i][j]))


        self.todaysell.display(self.todaysellm)




    #-----------------메뉴추가 버튼기능함수입니다----------------#
    def menu_add(self):
        dmn_add = mn_add()
        dmn_add.exec_()
        self.thread_refresh_some()
        # self.refresh_some()


    # ---------------가격수정 버튼기능구현함수입니다-------------#
    def menu_mod(self):
        dmn_mod = mn_mod()
        dmn_mod.exec_()
        self.thread_refresh_some()
    # ---------------메뉴삭제 버튼기능구현함수입니다-------------#
    def menu_del(self):
        dmn_mod=mn_del()
        dmn_mod.exec_()
        self.thread_refresh_some()
    # ---------------재료추가 창 띄우는 함수입니다. -------------#
    def ingre_add(self):
        dlg_add = ing_add()
        dlg_add.exec_()
        self.thread_refresh_some()
    # ---------------재료발주 창 띄우는 함수입니다.-------------#
    def ingre_mod(self):
        dlg_mod = ing_mod()
        dlg_mod.exec_()
        self.thread_refresh_some()

    # ---------------재료삭제 창 띄우는 함수입니다.-------------#
    def ingre_del(self):
        dlg_del = ing_del()
        dlg_del.exec_()
        self.thread_refresh_some()
    # ---------------월간판매량 버튼기능구현함수입니다-------------#
    def one_month_sales(self):
        from new8.month_sale_button import month_graph
        month_graph()
    # ---------------연간판매량 버튼기능구현함수입니다-------------#
    def one_year_sales(self):
        from new8.month_sale_button import year_graph
        year_graph()
    # ---------------미래예측 버튼기능구현함수입니다-------------#
    def future_predict(self):
        from new8.tensor_predict import graph_pri
        graph_pri()
    #-----------------------강사님이 말씀하신 레이블바꾸기----------------------------#
    def chglable(self):
        if self.team_label.text() == str("순진하긴"):
            self.team_label.setText(str("긴하진순"))
        elif self.team_label.text() == str("긴하진순"):
            self.team_label.setText(str("순진하긴"))
        self.team_label.repaint()

    def send_end(self):
        print("주문완료를 보냅니다.")
        o = str("주문완료")
        subthread(o)


    #----------------------데이터베이스 테이블 리프레쉬------------------------------#

    def send_customer(self):
        print("메뉴세팅을 보냅니다.")
        o = str("메뉴세팅")
        subthread(o)

    def thread_refresh_all(self):
        a = threading.Thread(target=self.refresh_all)
        a.start()



    def thread_refresh_some(self):
        a = threading.Thread(target=self.refresh_some)
        a.start()


    def refresh_all(self):

        pysql.sqldata(self)



        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(self.data_int2)

        for i in range(0, len(self.res5)):
            for j in range(0, self.data_int1):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(i, j, item)
                item = self.tableWidget.item(i, j)
                item.setText(str(self.res5[i][j]))


        self.tableWidget_2.clearContents()
        self.tableWidget_2.setRowCount(self.foodrow)

        for i in range(0, len(self.foodtableall)):
            for j in range(0, self.ingrecol):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget_2.setItem(i, j, item)
                item = self.tableWidget_2.item(i, j)
                item.setText(str(self.foodtableall[i][j]))


        self.tableWidget_3.clearContents()
        self.tableWidget_3.setRowCount(self.salerow)

        for i in range(0, len(self.saletableall)):
            for j in range(0, self.salecol):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget_3.setItem(i, j, item)
                item = self.tableWidget_3.item(i, j)
                item.setText(str(self.saletableall[i][j]))


        self.todaysell.display(self.todaysellm)



    def refresh_some(self):
        # a = threading.Thread(target=self.refresh_some)
        pysql.refresh_button(self)

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(self.data_int2)

        for i in range(0, len(self.res5)):
            for j in range(0, self.data_int1):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(i, j, item)
                item = self.tableWidget.item(i, j)
                item.setText(str(self.res5[i][j]))


        self.tableWidget_2.clearContents()
        self.tableWidget_2.setRowCount(self.foodrow)

        for i in range(0, len(self.foodtableall)):
            for j in range(0, self.ingrecol):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget_2.setItem(i, j, item)
                item = self.tableWidget_2.item(i, j)
                item.setText(str(self.foodtableall[i][j]))

        # a.start()




