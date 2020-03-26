    # ---------------재료수정 버튼기능구현함수입니다-------------#
from new8.sql_and_query import *
from PyQt5.QtWidgets import QDialog, QLabel, QComboBox, QLineEdit, QPushButton, QGridLayout, QMessageBox


class ing_mod(QDialog):

    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        pysql.sqlConnect(self)

        sql1 = "select 재료 from 재료재고;"
        self.cursor.execute(sql1)
        res = self.cursor.fetchall()
        rec = [""]+[x[0] for x in res]

        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle("재료발주")

        label1 = QLabel("재료이름")
        label2 = QLabel("재료개수")

        self.lineEdit1 = QLineEdit()
        self.qc = QComboBox(self)
        self.qc.addItems(rec)
        self.qc.currentTextChanged.connect(self.selec)
        self.pushButton1 = QPushButton("재료발주")
        self.pushButton1.clicked.connect(self.ing_mod_ok)
        self.pushButton2 = QPushButton("취소")
        self.pushButton2.clicked.connect(self.ing_mod_cancel)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 1, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.qc, 0, 1)
        layout.addWidget(self.pushButton2, 1, 2)

        self.setLayout(layout)

    def selec(self):
        self.b=self.qc.currentText()

    def ing_mod_ok(self):
        pysql.sqlConnect(self)

        self.ing_mod_sql = "update 재료재고 set 재료재고=재료재고+%s where 재료=%s;"
        try:
            a = int(self.lineEdit1.text())
            # input으로 받아온 값이 INT형이 아닐 때 나타내는 에러
        except:
            QMessageBox.information(self, "삽입 오류", "숫자를 입력하세요.", QMessageBox.Yes, QMessageBox.Yes)
            return
        b = self.b

        data=(a,b)
        self.cursor.execute(self.ing_mod_sql,data)
        self.conn.commit()
        self.conn.close()
        QMessageBox.information(self, "입력완료", "재료발주가 완료되었습니다.", QMessageBox.Ok, QMessageBox.Ok)
        self.close()


    def ing_mod_cancel(self):
        self.close()



