from new8.sql_and_query import *

from PyQt5.QtWidgets import QDialog, QLabel, QComboBox, QLineEdit, QPushButton, QGridLayout, QMessageBox

#메뉴 추가 함수
class mn_add(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        pysql.sqlConnect(self)
        sql1 = "select 재료 from 재료재고;"
        self.cursor.execute(sql1)
        res = self.cursor.fetchall()
        rec = [""] + [x[0] for x in res]

        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle("재료추가")

        label1 = QLabel("메뉴이름")
        label2 = QLabel("메뉴가격")
        label3 = QLabel("메뉴레시피1")
        label4 = QLabel("메뉴레시피2")
        label5 = QLabel("메뉴레시피3")

        self.lineEdit1 = QLineEdit()

        self.lineEdit2 = QLineEdit()

        self.qc1 = QComboBox(self)
        self.qc1.addItems(rec)
        self.qc1.currentIndexChanged.connect(self.selec)

        self.qc2 = QComboBox(self)
        self.qc2.addItems(rec)
        self.qc2.currentIndexChanged.connect(self.selec)

        self.qc3 = QComboBox(self)
        self.qc3.addItems(rec)
        self.qc3.currentIndexChanged.connect(self.selec)

        self.pushButton1 = QPushButton("메뉴추가")
        self.pushButton1.clicked.connect(self.mn_ins_ok)

        self.pushButton2 = QPushButton("취소")
        self.pushButton2.clicked.connect(self.mn_ins_cancel)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)

        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)

        layout.addWidget(label3,2,0)
        layout.addWidget(self.qc1,2,1)

        layout.addWidget(label4, 3, 0)
        layout.addWidget(self.qc2, 3, 1)

        layout.addWidget(label5, 4, 0)
        layout.addWidget(self.qc3, 4, 1)

        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(self.pushButton2, 1, 2)

        self.setLayout(layout)

    def selec(self):
        self.a = self.qc1.currentText()
        self.b = self.qc2.currentText()
        self.c = self.qc3.currentText()

    def mn_ins_ok(self):
        pysql.sqlConnect(self)
        mn_ins_sql = "insert into 메뉴 values (%s,%s,%s,NULL,%s,NULL,%s,NULL);"
        txt_menu_name = self.lineEdit1.text()
        try:
            txt_menu_price = int(self.lineEdit2.text())
            # input으로 받아온 값이 INT형이 아닐 때 나타내는 에러
        except:
            QMessageBox.information(self, "삽입 오류", "메뉴가격을 입력하세요.(숫자만)", QMessageBox.Yes, QMessageBox.Yes)
            return

        a = self.a
        b = self.b
        if b == "":
            b = None
        c = self.c
        if c == "":
            c = None
        data=(txt_menu_name,txt_menu_price,a,b,c)
        self.cursor.execute(mn_ins_sql,data)

        list_test = [
            "update 메뉴,재료재고 set 레시피1_재료재고= 재료재고.재료재고 where 메뉴.레시피1=재료재고.재료",
            "update 메뉴,재료재고 set 레시피2_재료재고= 재료재고.재료재고 where 메뉴.레시피2=재료재고.재료",
            "update 메뉴,재료재고 set 레시피3_재료재고= 재료재고.재료재고 where 메뉴.레시피3=재료재고.재료"]

        # 쿼리문에서 실행된 내용을 변수에 삽입
        for i in list_test:
            # 쿼리문 실행
            self.cursor.execute(i)

        self.conn.commit()
        self.conn.close()
        QMessageBox.information(self, "입력완료", "메뉴추가가 완료되었습니다.", QMessageBox.Ok, QMessageBox.Ok)
        self.close()


    def mn_ins_cancel(self):
        self.close()