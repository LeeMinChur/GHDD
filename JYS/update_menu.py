import pymysql

#메뉴 가격 변경 함수
def menu_price_update():

    # DB연동
    conn = pymysql.connect(host='192.168.0.7', port=3306, user='root', passwd='5284', db='Project', charset='utf8')

    # DB 커서 변수에 저장
    menu_price_update_cursor = conn.cursor()

    #쿼리문 : 메뉴가격, 메뉴이름(순서대로) 입력받아 메뉴 가격 변경( UI 텍스트필드를 서로 교차해서 만들면 좋을 것 같음(쿼리문 문법때문에 내가 못함))
    menu_price_update_sql=["update menu set menu_price = %s  where menu_name = %s"]

    # 쿼리문에서 실행된 내용을 변수에 삽입
    for menu_price_update_sql_input in menu_price_update_sql:

        # 변경할 메뉴 가격 입력(숫자만 입력받을 때 까지 반복하도록 예외처리, 숫자를 입력받으면 반복문 빠져나가기)
        while(True):
            try:
                menu_price_update_price = int(input())
            # input으로 받아온 값이 INT형이 아닐 때 나타내는 에러
            except ValueError:
                print("숫자만 넣어주세요")
            else:
                break

        #변경할 메뉴 이름 입력
        menu_price_update_name=input()

        # 변수 생성 후 입력받은 변수들을 이 변수에 삽입(이렇게 하지 않으면 excute가 argument를 최대 2개 밖에 받지 않아서 에러가 발생한다.)
        data=(menu_price_update_price,menu_price_update_name)

        # 쿼리문 실행
        menu_price_update_cursor.execute(menu_price_update_sql_input,data)

    #DB에 저장
    conn.commit()

    #DB 닫기
    conn.close()

#함수 실행
menu_price_update()
