import pymysql
def update_ing():
    db = pymysql.connect(host='192.168.0.7', port=3306, user='root', passwd='5284', db='Project', charset='utf8')
    ing_update_cursor = db.cursor()
    update_ing_sql="update ingredient set ingredient_stock = ingredient_stock+%s  where ingredient_name = %s"
    update_ing_stock=input()
    update_ing_name=input()

    data=( update_ing_stock, update_ing_name)
    ing_update_cursor.execute(update_ing_sql,data)

    list_test = [
        "update menu,ingredient set menu.stock1 = ingredient.ingredient_stock where menu.menu_recipe1=ingredient.ingredient_name",
        "update menu,ingredient set menu.stock2 = ingredient.ingredient_stock where menu.menu_recipe2=ingredient.ingredient_name",
        "update menu,ingredient set menu.stock3 = ingredient.ingredient_stock where menu.menu_recipe3=ingredient.ingredient_name"]
    for i in list_test:
        ing_update_cursor.execute(i)
    db.commit()
    db.close()

update_ing()
