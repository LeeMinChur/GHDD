from PyQt5 import QtCore

from new8.sql_and_query import *
# from new8.ui_and_function2 import *
from PyQt5.QtWidgets import QDialog, QLabel, QComboBox, QLineEdit, QPushButton, QGridLayout, QMessageBox

# ---------------재료추가 버튼기능구현함수입니다-------------#
class ing_add(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):



        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle("재료추가")

        label1= QLabel("재료이름")
        label2=QLabel("재료개수")

        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setGeometry((QtCore.QRect(80,25,240,30)))
        self.lineEdit2 = QLineEdit()
        self.pushButton1=QPushButton("재료추가")
        self.pushButton1.clicked.connect(self.ing_ins_ok)
        self.pushButton2 = QPushButton("취소")
        self.pushButton2.clicked.connect(self.ing_ins_cancel)

        layout = QGridLayout()
        layout.addWidget(label1, 0,0)
        layout.addWidget(self.lineEdit1,0,1)
        layout.addWidget(self.pushButton1,0,2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)
        layout.addWidget(self.pushButton2, 1,2)

        self.setLayout(layout)

    def ing_ins_ok(self):
        pysql.sqlConnect(self)

        sql1 = "select 재료 from 재료재고;"
        self.cursor.execute(sql1)
        res = self.cursor.fetchall()
        rec = [x[0] for x in res]
        for i in rec:
            print(i)

        if (self.lineEdit1.text() != "") and (self.lineEdit2 != ""):

            ing_ins_sql = "insert into 재료재고 values (%s,%s);"

            for i in rec:
                if self.lineEdit1.text()!=i:
                    txt_ins_ing_name = self.lineEdit1.text()
                else:
                    QMessageBox.information(self, "입력오류", "이미 있는 재료입니다.", QMessageBox.Ok, QMessageBox.Ok)
                    return

            try:
                txt_ins_ing_stock = int(self.lineEdit2.text())
                if txt_ins_ing_stock <= 0:
                    QMessageBox.information(self, "입력오류", "0개 미만으로 입력될 수 없습니다.", QMessageBox.Ok, QMessageBox.Ok)
                    return

                else:
                    pass

            except:
                QMessageBox.information(self, "입력오류", "재료개수를 입력하세요.(숫자만)", QMessageBox.Ok, QMessageBox.Ok)
                return
            try:
                data = (txt_ins_ing_name, txt_ins_ing_stock)
                self.cursor.execute(ing_ins_sql, data)
                self.conn.commit()
                self.conn.close()

            except:
                QMessageBox.information(self, "입력오류", "재료개수가 너무 많습니다.", QMessageBox.Ok, QMessageBox.Ok)
                return

            QMessageBox.information(self, "추가완료", "재료추가가 완료되었습니다.", QMessageBox.Ok, QMessageBox.Ok)
            self.close()
        else:
            QMessageBox.information(self, "입력오류", "빈칸없이 입력하세요.", QMessageBox.Ok, QMessageBox.Ok)


    def ing_ins_cancel(self):
        self.close()

