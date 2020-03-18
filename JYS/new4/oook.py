import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from new4.sql_and_query import pysql
import pymysql

class LogInDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.setupUI()



    def setupUI(self):
        pysql.sqlConnect(self)
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle("Sign In")
        self.push1=QPushButton("삭제")
        sql1="select ingredient_name from ingredient;"
        self.cursor.execute(sql1)
        res=self.cursor.fetchall()
        rec=[x[0] for x in res]
        print(rec)






        self.qcombo1=QComboBox(self)
        self.qcombo1.addItems(rec)

        layout = QGridLayout()
        layout.addWidget(self.qcombo1, 0, 0)
        layout.addWidget(self.push1, 1, 0)
        self.push1.clicked.connect(self.dele)
        self.qcombo1.currentIndexChanged.connect(self.selec)
        self.setLayout(layout)

    def selec(self):
        self.txt=self.qcombo1.currentText()

    def dele(self):
        pysql.sqlConnect(self)
        sql = "delete from ingredient where ingredient_name=%s;"
        self.txt
        self.cursor.execute(sql, self.txt)
        self.conn.commit()
        self.conn.close()

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)
        self.setWindowTitle("PyStock v0.1")
        self.setWindowIcon(QIcon('icon.png'))

        self.pushButton = QPushButton("Sign In")
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def pushButtonClicked(self):
        dlg = LogInDialog()
        dlg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()