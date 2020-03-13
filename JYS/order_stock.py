import pymysql
#오더메뉴 재고 차감 함수
def order_stock_dec():

    # DB연동
    conn = pymysql.connect(host='192.168.0.7', port=3306, user='root', passwd='5284', db='Project', charset='utf8')

    # DB 커서 변수에 저장
    order_stock_dec_cursor = conn.cursor()

    #오더받은 메뉴(통신 통해서 받아야해서 아직 미구현(안에 메뉴명 넣어서는 테스트 가능))
    order='lemonade'

    # 쿼리문 : 오더받은 메뉴 행 가져오기
    order_stock_dec_sql = "select *from menu where menu_name=%s"

    # 쿼리문 실행하기
    order_stock_dec_cursor.execute(order_stock_dec_sql,order)

    # 열의 내용 하나씩 리스트로 변수에 저장
    order_stock_dec_cursor_res=list(order_stock_dec_cursor.fetchone())

    # 변수의 배열을 가져와서 0인지 확인하고 0이라면 재고부족 띄우고 0이 아니라면 재료재고에서 해당 메뉴 레시피 재고 차감
    if order_stock_dec_cursor_res[3] == 0 or order_stock_dec_cursor_res[5] == 0 or order_stock_dec_cursor_res[7] == 0:
        print("재고가 부족합니다.")

    else:
        # 재료재고에서 해당 메뉴 레시피 재고 차감
        ing="update ingredient set ingredient_stock = ingredient_stock-1 where ingredient_name=%s"

        #메뉴 레시피 이름을 3번(레시피가 3개니까) 불러와서 해당 값이 NULL이라면 해당 레시피는 빼고 불러오기
        for i in range(1,4):
            if order_stock_dec_cursor_res[i*2]!=None:
                order_stock_dec_cursor.execute(ing,order_stock_dec_cursor_res[i*2])
                print(order_stock_dec_cursor_res[i*2]+" ok.")
            else:
                pass

    # 차감된 재고를 메뉴 레시피 재료재고에서도 최신화.
    list_test=["update menu,ingredient set menu.stock1 = ingredient.ingredient_stock where menu.menu_recipe1=ingredient.ingredient_name",
               "update menu,ingredient set menu.stock2 = ingredient.ingredient_stock where menu.menu_recipe2=ingredient.ingredient_name",
               "update menu,ingredient set menu.stock3 = ingredient.ingredient_stock where menu.menu_recipe3=ingredient.ingredient_name"]

    # 쿼리문에서 실행된 내용을 변수에 삽입
    for i in list_test:

        # 쿼리문 실행
        order_stock_dec_cursor.execute(i)

    # DB에 저장
    conn.commit()

    #DB 닫기
    conn.close()

#함수 실행
order_stock_dec()
