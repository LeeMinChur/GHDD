import pymysql
def select_table_menu():
    db = pymysql.connect(host='192.168.0.7', port=3306, user='root', passwd='5284', db='Project', charset='utf8')
    cursor = db.cursor()

    sql4 = ''' select *from menu'''
    cursor.execute(sql4)

    res = cursor.fetchall()
    res1 = cursor.fetchone()
    for i in range(0, len(res)):
        for j in range(0, 4):
            print(res[i][j])
    return


    db.close()

select_table_menu()