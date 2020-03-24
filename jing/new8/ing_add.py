from PyQt5 import QtCore
from new7.sql_and_query import pysql
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QGridLayout, QMessageBox
from new8.ui_and_function2 import *

# ---------------재료추가 버튼기능구현함수입니다-------------#
class ing_add(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        pysql.sqlConnect(self)
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

        if (self.lineEdit1.text() != "") and (self.lineEdit2 != ""):
            try:
                ing_ins_sql = "insert into 재료재고(재료,재료재고) values (%s,%s);"
                txt_ins_ing_name = self.lineEdit1.text()

                try:
                    txt_ins_ing_stock = int(self.lineEdit2.text())
                    # input으로 받아온 값이 INT형이 아닐 때 나타내는 에러
                except:
                    QMessageBox.information(self, "삽입 오류", "숫자를 입력하세요.", QMessageBox.Yes, QMessageBox.Yes)
                data = (txt_ins_ing_name, txt_ins_ing_stock)
                self.cursor.execute(ing_ins_sql, data)
                self.conn.commit()
                QMessageBox.information(self, "입력완료", "재료가 추가되었습니다.", QMessageBox.Ok, QMessageBox.Ok)

                self.close()



            except:
                QMessageBox.information(self, "삽입 오류", "올바른 형식으로 입력하세요.", QMessageBox.Yes, QMessageBox.Yes)

            return
        elif (self.lineEdit1.text() == "") and (self.lineEdit2 == ""):
            QMessageBox.information(self, "입력 오류", "빈칸 없이 입력하세요.", QMessageBox.Yes, QMessageBox.Yes)


    def ing_ins_cancel(self):
        pysql.sqlConnect(self)
        self.close()

