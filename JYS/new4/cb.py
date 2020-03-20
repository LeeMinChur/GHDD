from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import *
import pymysql
from new4.sql_and_query import pysql
from PyQt5 import QtCore, QtGui, QtWidgets
global w
global ip,pt,name,pwd,dbname,char_type

class a(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle("재료추가")



        self.setLayout(layout)