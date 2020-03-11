import pymysql
def insert_ing():
    db = pymysql.connect(host='192.168.0.7', port=3306, user='root', passwd='5284', db='Project', charset='utf8')
    ing_ins_Cursor = db.cursor()
    ins_ing_sql="insert into ingredient values (%s, %s)"
    ing_name=input()
    ing_stock=input()
    data=(ing_name,ing_stock)
    ing_ins_Cursor.execute(ins_ing_sql,data)

    db.commit()
    db.close()

insert_ing()
