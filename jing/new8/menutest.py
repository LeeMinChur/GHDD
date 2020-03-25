class mn_add(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        pysql.sqlConnect(self)
        sql1 = "select ingredient_name from ingredient;"
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
        mn_ins_sql = "insert into menu values (%s,%s,%s,NULL,%s,NULL,%s,NULL);"
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
            "update menu,ingredient set menu.stock1 = ingredient.ingredient_stock where menu.menu_recipe1=ingredient.ingredient_name",
            "update menu,ingredient set menu.stock2 = ingredient.ingredient_stock where menu.menu_recipe2=ingredient.ingredient_name",
            "update menu,ingredient set menu.stock3 = ingredient.ingredient_stock where menu.menu_recipe3=ingredient.ingredient_name"]

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
    # ---------------메뉴수정 버튼기능구현함수입니다-------------#
class mn_mod(QDialog):

    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        pysql.sqlConnect(self)

        sql1 = "select menu_name from menu;"
        self.cursor.execute(sql1)
        res = self.cursor.fetchall()
        rec = [""] + [x[0] for x in res]

        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle("메뉴수정")

        label1 = QLabel("메뉴이름")
        label2 = QLabel("메뉴수정")

        self.lineEdit1 = QLineEdit()
        self.qc = QComboBox(self)
        self.qc.addItems(rec)
        self.qc.currentTextChanged.connect(self.selec)
        self.pushButton1 = QPushButton("메뉴수정")
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

        ing_mod_sql = "update menu set menu_price = %s  where menu_name = %s"
        try:
            a = int(self.lineEdit1.text())
            # input으로 받아온 값이 INT형이 아닐 때 나타내는 에러
        except:
            QMessageBox.information(self, "삽입 오류", "숫자를 입력하세요.", QMessageBox.Yes, QMessageBox.Yes)
            return

        b = self.b

        data = (a, b)
        self.cursor.execute(ing_mod_sql, data)
        self.conn.commit()
        self.conn.close()
        QMessageBox.information(self, "입력완료", "메뉴수정이 완료되었습니다.", QMessageBox.Ok, QMessageBox.Ok)
        self.close()

    def ing_mod_cancel(self):
        self.close()

    # ---------------메뉴삭제 버튼기능구현함수입니다-------------#
class mn_del(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        pysql.sqlConnect(self)
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle("메뉴 삭제")
        self.pushButton1 = QPushButton("메뉴삭제")
        sql1 = "select menu_name from menu;"
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
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(self.pushButton2, 1, 2)
        self.setLayout(layout)

    def selec(self):
        self.a = self.qcombo1.currentText()

    def ing_del_ok(self):
        pysql.sqlConnect(self)
        ing_del_sql = "delete from menu where menu_name=%s;"
        self.a
        self.cursor.execute(ing_del_sql, self.a)
        self.conn.commit()
        self.conn.close()
        QMessageBox.information(self, "입력완료", "재료삭제가 완료되었습니다.", QMessageBox.Ok, QMessageBox.Ok)
        self.close()

    def ing_del_cancel(self):
        self.close()

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
                ing_ins_sql = "insert into ingredient(ingredient_name,ingredient_stock) values (%s,%s);"
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
        else:
            QMessageBox.information(self, "입력 오류", "빈칸 없이 입력하세요.", QMessageBox.Yes, QMessageBox.Yes)


    def ing_ins_cancel(self):
        self.close()

    # ---------------재료발주 버튼기능구현함수입니다-------------#

class ing_mod(QDialog):

    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        pysql.sqlConnect(self)

        sql1 = "select ingredient_name from ingredient;"
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

        ing_mod_sql = "update ingredient set ingredient_stock=ingredient_stock+%s where ingredient_name=%s;"
        try:
            a = int(self.lineEdit1.text())
            # input으로 받아온 값이 INT형이 아닐 때 나타내는 에러
        except:
            QMessageBox.information(self, "삽입 오류", "숫자를 입력하세요.", QMessageBox.Yes, QMessageBox.Yes)
            return


        b = self.b

        data=(a,b)
        self.cursor.execute(ing_mod_sql,data)
        self.conn.commit()
        self.conn.close()
        QMessageBox.information(self, "입력완료", "재료발주가 완료되었습니다.", QMessageBox.Ok, QMessageBox.Ok)
        self.close()


    def ing_mod_cancel(self):
        self.close()

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
        sql1 = "select ingredient_name from ingredient;"
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
        ing_del_sql = "delete from ingredient where ingredient_name=%s;"
        self.a
        self.cursor.execute(ing_del_sql,self.a)
        self.conn.commit()
        self.conn.close()
        QMessageBox.information(self, "입력완료", "메뉴삭제가 완료되었습니다.", QMessageBox.Ok, QMessageBox.Ok)
        self.close()

    def ing_del_cancel(self):
        self.close()


    #-------------------------------------------------------------------##
