import pymysql

#메뉴 추가 함수
def menu_insert():

    # DB연동
    conn = pymysql.connect(host='192.168.0.7', port=3306, user='root', passwd='5284', db='Project', charset='utf8')

    #DB 커서 변수에 저장
    menu_ins_cursor = conn.cursor()

    #쿼리문 : 이름, 가격, 레시피1, 레시피2, 레시피3(순서대로)입력 받아서 메뉴추가
    menu_ins_sql="insert into menu values (%s,%s,%s,NULL,%s,NULL,%s,NULL)"

    #메뉴 이름 입력
    menu_ins_name=input()

    #메뉴 가격 입력(숫자만 입력받을 때 까지 반복하도록 예외처리, 숫자를 입력받으면 반복문 빠져나가기)
    while (True):
        try:
            menu_ins_price = int(input())

        #input으로 받아온 값이 INT형이 아닐 때 나타내는 에러
        except ValueError:
            print("숫자를 입력해주세요")

        else:
            break

    #레시피 반복문을 위한 리스트 변수 생성
    menu_ins_recipe = []

    #레시피 반복문(생성한 리스트 변수에 입력받은 레시피 반복하여 넣는데 만약, 레시피 열 3개 중에 2개만 사용한다면 입력하지 않는다.)
    for i in range(3):
        menu_ins_recipe.append(input())
        if menu_ins_recipe[i]=='':

            #사용하지 않는 레시피열을 NULL처리를 위해 None을 삽입
            menu_ins_recipe[i]=None

    #변수 생성 후 입력받은 변수들을 이 변수에 삽입(이렇게 하지 않으면 excute가 argument를 최대 2개 밖에 받지 않아서 에러가 발생한다.)
    data=(menu_ins_name,menu_ins_price,menu_ins_recipe[0],menu_ins_recipe[1],menu_ins_recipe[2])

    #쿼리문 실행
    menu_ins_cursor.execute(menu_ins_sql,data)

    #생성한 메뉴의 레시피가 재고에 있다면 그대로 삽입해준다.

    menu_ins_reference_stock = [
        "update menu,ingredient set menu.stock1 = ingredient.ingredient_stock where menu.menu_recipe1=ingredient.ingredient_name",
        "update menu,ingredient set menu.stock2 = ingredient.ingredient_stock where menu.menu_recipe2=ingredient.ingredient_name",
        "update menu,ingredient set menu.stock3 = ingredient.ingredient_stock where menu.menu_recipe3=ingredient.ingredient_name"]

    #쿼리문에서 실행된 내용을 변수에 삽입
    for i in menu_ins_reference_stock:

        # 쿼리문 실행
        menu_ins_cursor.execute(i)

    #DB에 저장
    conn.commit()

    #DB닫기
    conn.close()

#함수 실행
menu_insert()

