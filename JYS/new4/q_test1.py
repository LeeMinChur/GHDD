import sys,pymysql
from PyQt5.QtWidgets import QApplication, QWidget

class sql(QWidget):
    def __init__(self):
        super().__init__()
        self.sqlConnect()
        self.initUI()
        self.run()

        def sqlConnect(self):
            try:
                self.conn = pymysql.connect(host='192.168.0.7', port=3306, user='root', passwd='5284', db='Project', charset='utf8')

            except:
                print("문제가 있네")
                exit(1)

        print("성공")
        self.cur=self.conn.
