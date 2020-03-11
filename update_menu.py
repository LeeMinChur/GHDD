import pymysql
def update_menu():
    db = pymysql.connect(host='192.168.0.7', port=3306, user='root', passwd='5284', db='Project', charset='utf8')
    menu_update_cursor = db.cursor()
    update_menu_sql="update menu set menu_price = %s  where menu_name = %s"
    update_mn_price=input()
    update_mn_name=input()
    data=(update_mn_price,update_mn_name)
    menu_update_cursor.execute(update_menu_sql,data)

    db.commit()
    db.close()

update_menu()
