import threading

import pymysql
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer


class pysql(QTimer):

    # ------------------------mysql에 연결시도----------------------#
    def sqlConnect(self):
        try:
            #
            self.conn = pymysql.connect \
                (host='192.168.0.7'
                 , port=3306, user='root'
                 , password='5284'
                 , db='project'
                 , charset='utf8')

            # 주서버가 작동하지 않을때 임시서버
            # self.conn = pymysql.connect \
            #     (host='127.0.0.10'
            #      , port=3306, user='root'
            #      , password='1234'
            #      , db='project'
            #      , charset='utf8')

        except:
            print("연결에 문제가있습니다.")
            exit(1)
        print("연결성공!")
        self.cursor = self.conn.cursor()

    # sql 데이터 셋 계산 - 열 갯수, 행 갯수, 데이터 값 불러오기
    def sqldata(self):
        pysql.sqlConnect(self)

        # ------------------------음식테이블 재료추출----------------------#
        # 열 개수
        메뉴테이블열갯수sql = """SELECT count(COLUMN_NAME)
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = SCHEMA()
        AND TABLE_NAME = 'menu' ORDER BY ORDINAL_POSITION;"""
        self.cursor.execute(메뉴테이블열갯수sql)
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

        # 데이터 모두 하나씩 출력

        self.sql5 = ''' select *from menu'''
        self.cursor.execute(self.sql5)

        self.res5 = self.cursor.fetchall()
        self.res6 = self.cursor.fetchone()
        for i in range(0, len(self.res5)):
            for j in range(0, self.data_int1):
                print(self.res5[i][j])

        self.menu_column_print = """SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = SCHEMA()
        AND TABLE_NAME = 'menu' ORDER BY ORDINAL_POSITION;"""

        self.cursor.execute(self.menu_column_print)

        menu_col = self.cursor.fetchall()
        self.menu_list = [x[0] for x in menu_col]

        for i in range(0, len(self.menu_list)):
            print(self.menu_list[i])

        # ---------------------------재료테이블 데이터 추출 2번째 테이블------------------------#
        # 열 개수
        self.재료테이블열개수sql = """SELECT count(COLUMN_NAME)
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = SCHEMA()
        AND TABLE_NAME = 'ingredient' ORDER BY ORDINAL_POSITION;"""
        self.cursor.execute(self.재료테이블열개수sql)
        res = self.cursor.fetchall()

        for data in res:
            data_list = (list(data))
            data_int = data_list[0]
            self.ingrecol = int(data_int)

        print(self.ingrecol)

        # 재료테이블 행 개수
        self.재료테이블행개수sql = """select count(*) from ingredient;"""
        self.cursor.execute(self.재료테이블행개수sql)
        self.res7 = self.cursor.fetchall()

        for i in self.res7:
            data_list = (list(i))
            data_int = data_list[0]
            self.foodrow = int(data_int)

        print(self.foodrow)

        # 데이터 모두 하나씩 출력
        self.재료테이블하나씩출력하는sql문 = ''' select *from ingredient'''
        self.cursor.execute(self.재료테이블하나씩출력하는sql문)

        self.foodtableall = self.cursor.fetchall()
        for i in range(0, len(self.foodtableall)):
            for j in range(0, self.ingrecol):
                print(self.foodtableall[i][j])

        self.재료열만출력하는sql문 = """SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = SCHEMA()
        AND TABLE_NAME = 'ingredient' ORDER BY ORDINAL_POSITION;"""

        self.cursor.execute(self.재료열만출력하는sql문)

        ingre_col = self.cursor.fetchall()
        self.ingredient_list = [x[0] for x in ingre_col]

        for i in range(0, len(self.ingredient_list)):
            print(self.ingredient_list[i])

        # ---------------------------주문내역 테이블-----------------------------#
        # 열 개수 --일단안됨

        self.주문내역테이블열개수 = """SELECT count(COLUMN_NAME)
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = SCHEMA()
        AND TABLE_NAME = 'sales' ORDER BY ORDINAL_POSITION;"""
        self.cursor.execute(self.주문내역테이블열개수)
        self.res10 = self.cursor.fetchall()

        for data in self.res10:
            data_list = (list(data))
            data_int = data_list[0]
            self.salecol = int(data_int)

        print(self.salecol)

        # 주문내역테이블 행 개수
        self.주문내역테이블행개수 = """select count(*) from sales;"""
        self.cursor.execute(self.주문내역테이블행개수)
        self.res11 = self.cursor.fetchall()

        for data1 in self.res11:
            data_list = (list(data1))
            data_int = data_list[0]
            self.salerow = int(data_int)

        print(self.salerow)
        # 열이 salecol, 행이 salerow

        # 데이터 모두 하나씩 출력

        self.데이터모두하나씩출력 = ''' select * from sales;'''
        self.cursor.execute(self.데이터모두하나씩출력)

        self.saletableall = self.cursor.fetchall()
        for i in range(0, len(self.saletableall)):
            for j in range(0, self.salecol):
                print(self.saletableall[i][j])

        # 일단 임의로 지정한 열갯수

        self.column_print = """SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = SCHEMA()
        AND TABLE_NAME = 'sales' ORDER BY ORDINAL_POSITION;"""

        self.cursor.execute(self.column_print)

        sales = self.cursor.fetchall()
        self.sale_list = [x[0] for x in sales]

        for i in range(0, len(self.sale_list)):
            print(self.sale_list[i])

        #----------------일일매출----------------------#
        일일매출 = """select sum(sales_price) from sales;"""
        self.cursor.execute(일일매출)
        todaysell = self.cursor.fetchall()


        for i in todaysell:
            data_list= list(i)
            data_int = data_list[0]
            self.todaysellm = int(data_int)

        print(self.todaysellm)


    def sqlloop(self):
        self.timersql = QtCore.QTimer()
        self.timersql.timeout.connect(self.sqldata())
        self.timersql.start(3000)
#
#         timer3 = threading.Thread(1.0, self.printit1)
#         self.i +=1
#         print(self.i)
#         timer3.start()
#
#


# x = threading.Thread(pysql().sqldata())
# x.start()
