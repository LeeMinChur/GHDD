import pymysql
def update_sales():
    db = pymysql.connect(host='192.168.0.7', port=3306, user='root', password='5284', db='Project', charset='utf8')
    ing_delete_cursor = db.cursor()
    del_ing_sql="delete from ingredient where ingredient_name=%s"
    del_ing=input()

    ing_delete_cursor.execute(del_ing_sql,del_ing)

    db.commit()
    db.close()

delete_ing()
