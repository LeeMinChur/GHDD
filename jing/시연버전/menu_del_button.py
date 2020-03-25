from new8.sql_and_query import *
from PyQt5.QtWidgets import QDialog, QPushButton, QLabel, QComboBox, QGridLayout, QMessageBox



# ---------------재료 삭제 버튼기능구현함수입니다-------------#
class ing_del(QDialog):

    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        pysql.sqlConnect(self)
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle("재료 삭제")
        self.pushButton1 = QPushButton("재료삭제")
        sql1 = "select 재료 from 재료재고;"
        self.cursor.execute(sql1)
        res = self.cursor.fetchall()
        rec = [""]+[x[0] for x in res]

        label1 = QLabel("재료이름")
        self.qcombo1 = QComboBox(self)
        self.qcombo1.addItems(rec)

        self.pushButton1.clicked.connect(self.ing_del_ok)
        self.qcombo1.currentTextChanged.connect(self.selec)



        self.pushButton2 = QPushButton("취소")
        self.pushButton2.clicked.connect(self.ing_del_cancel)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.qcombo1, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(self.pushButton2, 1, 2)
        self.setLayout(layout)
    def selec(self):
        self.a=self.qcombo1.currentText()

    def ing_del_ok(self):
        pysql.sqlConnect(self)
        ing_del_sql = "delete from 재료재고 where 재료=%s;"
        self.a
        self.cursor.execute(ing_del_sql,self.a)
        self.conn.commit()
        self.conn.close()
        QMessageBox.information(self, "입력완료", "재료삭제가 완료되었습니다.", QMessageBox.Ok, QMessageBox.Ok)
        self.close()

    def ing_del_cancel(self):
        self.close()


    #-------------------------------------------------------------------##


