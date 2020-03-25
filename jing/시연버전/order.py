import pymysql
from new8.sql_and_query import pysql
from new8.server_ms import *

def result():
    from new8.server_ms import get_data2
    db = pymysql.connect(host='192.168.0.7', port=3306, user='root', passwd='5284', db='Project', charset='utf8')
    cursor = db.cursor()
    # pysql.sqlConnect()
    print("겟데이터:" , get_data2)

    for i in get_data2:
        sql1 = "select 메뉴이름 from 메뉴 where 메뉴이름=%s";
        cursor.execute(sql1, i)
        res1 = cursor.fetchone()
        rec1 = (list(res1))
        print(rec1)

        sql2 = "select 메뉴가격 from 메뉴 where 메뉴이름=%s";
        cursor.execute(sql2,i)
        res2 = cursor.fetchone()
        rec2=(list(res2))
        print(rec2)

        ##################통신연동 시 사용 할 영수증 쿼리문######################
        sql3= "insert into 판매내역 values (%s,default,%s,%s)"
        a=rec1
        b=None
        c=rec2
        data = (a,b,c)
        cursor.execute(sql3, data)

    db.commit()
    db.close()


class result2():

    def test10000(self):
        from new8.server_ms import get_data2
        print("dmdmd : ", end="")
        print(get_data2)
        time.sleep(1)

    def test123213(self):
        while True:
            self.test10000()

c = threading.Thread(target=result2().test123213())
c.start()
