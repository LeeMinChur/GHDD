import pymysql

#재료 추가 함수
def ing_insert():

    # DB연동
    conn = pymysql.connect(host='192.168.0.7', port=3306, user='root', passwd='5284', db='Project', charset='utf8')

    # DB 커서 변수에 저장
    ing_ins_cursor = conn.cursor()

    #쿼리문 : 재료이름, 재료개수(순서대로) 입력받아서 재고 추가
    ing_ins_sql="insert into ingredient values (%s, %s)"

    # 재료 이름 입력
    ing_ins_name=input()

    # 재료 개수 입력(숫자만 입력받을 때 까지 반복하도록 예외처리, 숫자를 입력받으면 반복문 빠져나가기)
    while (True):
        try:
            ing_ins_stock = int(input())
        # input으로 받아온 값이 INT형이 아닐 때 나타내는 에러
        except ValueError:
            print("숫자를 입력해주세요")

        else:
            break

    # 변수 생성 후 입력받은 변수들을 이 변수에 삽입(이렇게 하지 않으면 excute가 argument를 최대 2개 밖에 받지 않아서 에러가 발생한다.)
    data=(ing_ins_name,ing_ins_stock)

    # 생성한 메뉴의 레시피가 재고에 있다면 그대로 삽입해준다.

    ing_ins_reference_stock = [
        "update menu,ingredient set menu.stock1 = ingredient.ingredient_stock where menu.menu_recipe1=ingredient.ingredient_name",
        "update menu,ingredient set menu.stock2 = ingredient.ingredient_stock where menu.menu_recipe2=ingredient.ingredient_name",
        "update menu,ingredient set menu.stock3 = ingredient.ingredient_stock where menu.menu_recipe3=ingredient.ingredient_name"]

    # 쿼리문에서 실행된 내용을 변수에 삽입
    for i in ing_ins_reference_stock:

        # 쿼리문 실행
        ing_ins_cursor.execute(i)

    # 쿼리문 실행
    ing_ins_cursor.execute(ing_ins_sql,data)

    # DB에 저장
    conn.commit()

    #DB 닫기
    conn.close()

#함수 실행
ing_insert()
