import pymysql
#리프레시 함수
def refresh_stock():

    # DB연동
    conn = pymysql.connect(host='192.168.0.7', port=3306, user='root', passwd='5284', db='Project', charset='utf8')

    # DB 커서 변수에 저장
    refresh_stock_cursor = conn.cursor()

    #재료 재고를 메뉴 레시피 재료재고에서도 최신화.
    list_test=["update menu,ingredient set menu.stock1 = ingredient.ingredient_stock where menu.menu_recipe1=ingredient.ingredient_name",
               "update menu,ingredient set menu.stock2 = ingredient.ingredient_stock where menu.menu_recipe2=ingredient.ingredient_name",
               "update menu,ingredient set menu.stock3 = ingredient.ingredient_stock where menu.menu_recipe3=ingredient.ingredient_name"]

    # 쿼리문에서 실행된 내용을 변수에 삽입
    for i in list_test:

        # 쿼리문 실행
        refresh_stock_cursor.execute(i)

    # DB에 저장
    conn.commit()

    #DB 닫기
    conn.close()

#함수 실행
refresh_stock()