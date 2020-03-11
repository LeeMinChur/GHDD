import pymysql
def delete_menu():
    db = pymysql.connect(host='192.168.0.7', port=3306, user='root', passwd='5284', db='Project', charset='utf8')
    menu_cursor = db.cursor()
    del_menu_sql="delete from menu where menu_name=%s"
    del_mn=input()

    menu_cursor.execute(del_menu_sql,del_mn)

    db.commit()
    db.close()


delete_menu()

