import pymysql

#재료재고 삭제 함수
def delete_ing():

    #DB연동
    db = pymysql.connect(host='192.168.0.7', port=3306, user='root', password='5284', db='Project', charset='utf8')

    # DB 커서 변수에 저장
    ing_delete_cursor = db.cursor()

    #쿼리문 : 재고명 입력받아 해당 재고내용 제거
    del_ing_sql="delete from ingredient where ingredient_name=%s"
    print("제거할 재고명을 입력하세요.")
    del_ing=input()

    #쿼리문 실행하기
    ing_delete_cursor.execute(del_ing_sql,del_ing)

    #DB에 저장
    db.commit()

    #DB 닫기
    db.close()

#함수 실행
delete_ing()

