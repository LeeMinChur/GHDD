import pymysql
def insert_sales():
    db = pymysql.connect(host='192.168.0.7', port=3306, user='root', passwd='5284', db='Project', charset='utf8')
    Cursor = db.cursor()
    sql="""insert into menu(menu_num,menu_name,menu_price,menu_recipe1,menu_recipe2,menu_recipe3) values (%s, %s, %s, %s, %s, %s)"""
    sql1="""update menu set menu.menu_name = @cnt:=@cnt+1;"""
    mn_num=input()
    mn_name=input()
    mn_price=input()
    mn_recipe1 = input()
    mn_recipe2 = input()
    mn_recipe3 = input()
    data=(mn_num,mn_name,mn_price,mn_recipe1,mn_recipe2,mn_recipe3)
    Cursor.execute(sql,data)
    Cursor.execute(sql1)

    db.commit()
    db.close()


insert_sales()

