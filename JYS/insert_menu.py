import pymysql

def insert_menu():
    menu_recipe=[]
    db = pymysql.connect(host='192.168.0.7', port=3306, user='root', passwd='5284', db='Project', charset='utf8')
    menu_ins_cursor = db.cursor()
    ins_menu_sql="insert into menu values (%s,%s,%s,NULL,%s,NULL,%s,NULL)"
    mn_name=input()
    mn_price=input()
    for i in range(3):
        menu_recipe.append(input())
        if menu_recipe[i]=='':
            menu_recipe[i]=None



    data=(mn_name,mn_price,menu_recipe[0],menu_recipe[1],menu_recipe[2])
    menu_ins_cursor.execute(ins_menu_sql,data)

    list_test = [
        "update menu,ingredient set menu.stock1 = ingredient.ingredient_stock where menu.menu_recipe1=ingredient.ingredient_name",
        "update menu,ingredient set menu.stock2 = ingredient.ingredient_stock where menu.menu_recipe2=ingredient.ingredient_name",
        "update menu,ingredient set menu.stock3 = ingredient.ingredient_stock where menu.menu_recipe3=ingredient.ingredient_name"]
    for i in list_test:
       menu_ins_cursor.execute(i)

    db.commit()
    db.close()

insert_menu()

