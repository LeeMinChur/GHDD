import pymysql
def update_ing():
    db = pymysql.connect(host='192.168.0.7', port=3306, user='root', passwd='5284', db='Project', charset='utf8')
    ing_update_cursor = db.cursor()
    update_ing_sql="update ingredient set ingredient_stock = %s  where ingredient_name = %s"
    update_ing_stock=input()
    update_ing_name=input()
    data=( update_ing_stock, update_ing_name)
    ing_update_cursor.execute(update_ing_sql,data)

    db.commit()
    db.close()

update_ing()
