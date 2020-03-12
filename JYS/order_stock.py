import pymysql
def order_stock():
    conn = pymysql.connect(host='192.168.0.7', port=3306, user='root', passwd='5284', db='Project', charset='utf8')
    cursor = conn.cursor()

    order='americano'
    sql = "select *from menu where menu_name=%s"
    cursor.execute(sql,order)
    res=list(cursor.fetchone())

    if res[3] == 0 or res[5] == 0 or res[7] == 0:
        print("재고가 부족합니다.")
  
    else:
        ing="update ingredient set ingredient_stock = ingredient_stock-1 where ingredient_name=%s"
        for i in range(1,4):
            if res[i*2]!=None:
                cursor.execute(ing,res[i*2])
                print(res[i*2]+" ok.")
            else:
                pass

    list_test=["update menu,ingredient set menu.stock1 = ingredient.ingredient_stock where menu.menu_recipe1=ingredient.ingredient_name",
               "update menu,ingredient set menu.stock2 = ingredient.ingredient_stock where menu.menu_recipe2=ingredient.ingredient_name",
               "update menu,ingredient set menu.stock3 = ingredient.ingredient_stock where menu.menu_recipe3=ingredient.ingredient_name"]
    for i in list_test:
        cursor.execute(i)

    conn.commit()
    conn.close()

order_stock()
