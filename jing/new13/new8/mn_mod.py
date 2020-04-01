from new8.server_ms import subthread
from new8.sql_and_query import *
from PyQt5.QtWidgets import QDialog, QLabel, QComboBox, QLineEdit, QPushButton, QGridLayout, QMessageBox


class mn_mod(QDialog):

    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        pysql.sqlConnect(self)

        sql1 = "select 메뉴이름 from 메뉴;"
        self.cursor.execute(sql1)
        res = self.cursor.fetchall()
        rec = [""] + [x[0] for x in res]

        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle("가격수정")

        label1 = QLabel("메뉴이름")
        label2 = QLabel("가격수정")

        self.lineEdit1 = QLineEdit()
        self.qc = QComboBox(self)
        self.qc.addItems(rec)
        self.qc.currentTextChanged.connect(self.selec)
        self.pushButton1 = QPushButton("가격수정")
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
        self.b = self.qc.currentText()

    def ing_mod_ok(self):
        pysql.sqlConnect(self)

        ing_mod_sql = "update 메뉴 set 메뉴가격 = %s  where 메뉴이름 = %s"

        if self.lineEdit1.text()!="":
            try:
                a = int(self.lineEdit1.text())
                if a <= 0:
                    QMessageBox.information(self, "입력오류", "0원 미만으로 입력될 수 없습니다.", QMessageBox.Ok, QMessageBox.Ok)
                    return

                else:
                    pass
                # input으로 받아온 값이 INT형이 아닐 때 나타내는 에러
            except:
                QMessageBox.information(self, "입력오류", "숫자를 입력하세요.", QMessageBox.Ok, QMessageBox.Ok)
                return

            try:
                b = self.b
            except:
                QMessageBox.information(self, "입력오류", "삭제할 메뉴를 선택하세요.", QMessageBox.Ok, QMessageBox.Ok)
                return


            data = (a, b)
            try:
                self.cursor.execute(ing_mod_sql, data)
                self.conn.commit()
                self.conn.close()
            except:
                QMessageBox.information(self, "입력오류", "올바른 가격을 입력하세요.", QMessageBox.Ok, QMessageBox.Ok)
                return

            o = str("메뉴세팅")
            subthread(o)
            QMessageBox.information(self, "수정완료", "가격수정이 완료되었습니다.", QMessageBox.Ok, QMessageBox.Ok)

            self.close()

        else:
            QMessageBox.information(self, "입력오류", "빈칸 없이 입력하세요.", QMessageBox.Ok, QMessageBox.Ok)

    def ing_mod_cancel(self):
        self.close()
