import pymysql

#메뉴 삭제함수
def delete_menu():

    # DB연동
    conn = pymysql.connect(host='192.168.0.7', port=3306, user='root', passwd='5284', db='Project', charset='utf8')

    # DB 커서 변수에 저장
    delete_menu_cursor = conn.cursor()

    #쿼리문 : 메뉴이름을 입력받아 메뉴 삭제
    del_menu_sql="delete from menu where menu_name=%s"

    #삭제할 메뉴 이름 입력
    delete_menu_name=input()

    # 쿼리문 실행
    delete_menu_cursor.execute(del_menu_sql,delete_menu_name)

    #DB에 저장
    conn.commit()

    #DB 닫기
    conn.close()

#함수 실행
delete_menu()

