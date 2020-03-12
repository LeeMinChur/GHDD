import pymysql
import re
def insert_menu():
    db = pymysql.connect(host='192.168.0.7', port=3306, user='root', passwd='5284', db='Project', charset='utf8')
    menu_ins_cursor = db.cursor()
    #쿼리문(해당 테이블 열개수에서 입력받을 만큼 %s 개수 설정)
    ins_menu_sql="insert into menu values (%s,%s,%s,%s,%s)"
    mn_name=input()
    mn_price=input()
    mn_recipe1=input()
    mn_recipe2 = input()
    mn_recipe3 = input()
    data=(mn_name,mn_price,mn_recipe1,mn_recipe2,mn_recipe3)
    menu_ins_cursor.execute(ins_menu_sql,data)

    db.commit()
    db.close()

insert_menu()

