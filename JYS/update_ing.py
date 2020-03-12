import pymysql

#재료 재고 추가 함수
def update_ing():

    # DB연동
    conn = pymysql.connect(host='192.168.0.7', port=3306, user='root', passwd='5284', db='Project', charset='utf8')

    # DB 커서 변수에 저장
    ing_stock_update_cursor = conn.cursor()

    # 쿼리문 : 추가 할 재고 개수, 재료재고 이름(순서대로) 입력받아 메뉴 가격 변경( UI 텍스트필드를 서로 교차해서 만들면 좋을 것 같음(쿼리문 문법때문에 내가 못함))
    ing_stock_update_sql="update ingredient set ingredient_stock = ingredient_stock+%s  where ingredient_name = %s"

    # 추기 할 재고 개수 입력(숫자만 입력받을 때 까지 반복하도록 예외처리, 숫자를 입력받으면 반복문 빠져나가기)
    while (True):
        try:
            ing_stock_update_stock = int(input())
            # input으로 받아온 값이 INT형이 아닐 때 나타내는 에러
        except ValueError:
            print("숫자를 입력해주세요")

        else:
            break

    #재료 이름 입력
    ing_stock_update_name=input()

    # 변수 생성 후 입력받은 변수들을 이 변수에 삽입(이렇게 하지 않으면 excute가 argument를 최대 2개 밖에 받지 않아서 에러가 발생한다.)
    ing_stock_update_data=( ing_stock_update_stock, ing_stock_update_name)

    # 쿼리문 실행
    ing_stock_update_cursor.execute(ing_stock_update_sql,ing_stock_update_data)

    # 추가한 재고를 메뉴 레시피 재료재고에서도 최신화.
    ing_stock_update_reference_stock = [
        "update menu,ingredient set menu.stock1 = ingredient.ingredient_stock where menu.menu_recipe1=ingredient.ingredient_name",
        "update menu,ingredient set menu.stock2 = ingredient.ingredient_stock where menu.menu_recipe2=ingredient.ingredient_name",
        "update menu,ingredient set menu.stock3 = ingredient.ingredient_stock where menu.menu_recipe3=ingredient.ingredient_name"]

    # 쿼리문에서 실행된 내용을 변수에 삽입
    for i in ing_stock_update_reference_stock:

        # 쿼리문 실행
        ing_stock_update_cursor.execute(i)

    #DB에 저장
    conn.commit()

    #DB 닫기
    conn.close()

#함수 실행
update_ing()
