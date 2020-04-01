from new8.server_ms import subthread
from new8.sql_and_query import *
from PyQt5.QtWidgets import QDialog, QLabel, QComboBox, QPushButton, QGridLayout, QMessageBox

#메뉴 삭제함수
class mn_del(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        pysql.sqlConnect(self)
        self.setGeometry(300, 300, 400, 500)
        self.setWindowTitle("메뉴 삭제")
        self.pushButton1 = QPushButton("메뉴삭제")
        sql1 = "select 메뉴이름 from 메뉴;"
        self.cursor.execute(sql1)
        res = self.cursor.fetchall()
        rec = [""] + [x[0] for x in res]

        label1 = QLabel("메뉴이름")
        self.qcombo1 = QComboBox(self)
        self.qcombo1.addItems(rec)

        self.pushButton1.clicked.connect(self.ing_del_ok)
        self.qcombo1.currentTextChanged.connect(self.selec)

        self.pushButton2 = QPushButton("취소")
        self.pushButton2.clicked.connect(self.ing_del_cancel)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.qcombo1, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2 )
        layout.addWidget(self.pushButton2, 1, 2)
        self.setLayout(layout)

    def selec(self):
        self.a = self.qcombo1.currentText()

    def mn_del_ok(self):
        try:
            pysql.sqlConnect(self)
            ing_del_sql = "delete from 메뉴 where 메뉴이름=%s;"
            self.a
            self.cursor.execute(ing_del_sql, self.a)
            self.conn.commit()
            self.conn.close()
            o = str("메뉴세팅")
            subthread(o)
            QMessageBox.information(self, "입력완료", "재료삭제가 완료되었습니다.", QMessageBox.Ok, QMessageBox.Ok)
            self.close()

        except:
            QMessageBox.information(self, "선택오류", "삭제할 메뉴를 선택해주세요.", QMessageBox.Ok, QMessageBox.Ok)

    def mn_del_cancel(self):
        self.close()











