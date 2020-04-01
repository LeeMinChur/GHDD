from socket import *
import threading
import time

import pymysql
from PyQt5.QtWidgets import QMainWindow

from new8.sql_and_query import send_menu
# from new8.ui_and_function2 import Ui_MainWindow


class Cserver(threading.Thread):
    def __init__(self,socket):
        super().__init__()
        self.s_socket=socket

    def run(self):
        global index
        self.c_socket,addr=self.s_socket.accept()
        print(addr[0],addr[1],"이 연결되었습니다")
        index=index+1
        creat_thread(self.s_socket)
        t=threading.Thread(target=self.c_recv)
        t.setdaemon=True
        t.start()

    def c_recv(self):
        send_menu.test11(self)

        global put_data
        global flag
        global get_data2
        print(self.c_socket)
        while True:
            put_data = ""


            get_data=self.c_socket.recv(1024)
            print('receive:%s'%get_data.decode('utf-8'))

            print("list get_data2: %s " % get_data2)
            data = get_data.decode('utf-8')
            print("server data: %s" % data)
            if  data == "세팅수락":
                send_menu.test11(self)
                put_data =  self.send_menu2 + "/"
                flag =1
                print('sending : %s' % put_data)

            elif data == "고객시작":
                put_data = self.send_menu2 + "/"
                flag =1
                print('sending : %s' % put_data)

            elif data == "가격확인":
                print('receive:%s'%get_data.decode('utf-8'))
                put_data ="세팅완료"
                print('sending : %s' % put_data)
                flag =1


            elif data == "메뉴확인":
                send_menu.test11(self)
                print('receive:%s'%get_data.decode('utf-8'))
                put_data = self.send_price + "."
                print('sending : %s' % put_data)
                flag =1
            elif data == "주문완료":
                put_data=data
                flag =1
            elif data == "주문취소":
                put_data=data
                flag =1
                db = pymysql.connect(host='192.168.0.13', port=3306, user='root', passwd='1234', db='Project', charset='utf8')
                cursor = db.cursor()
                sql="delete from 판매내역 where 주문출고 is null;"
                cursor.execute(sql)
                db.commit()
                db.close()

            elif data == "제품출고":
                print("출고되었습니다.")

                db = pymysql.connect(host='192.168.0.13', port=3306, user='root', passwd='1234', db='Project', charset='utf8')
                cursor = db.cursor()
                for i in get_data2:
                    sql="update 메뉴 set 레시피1_재료재고 = 레시피1_재료재고 - 1, 레시피2_재료재고=레시피2_재료재고 -1, 레시피3_재료재고=레시피3_재료재고 -1 where 메뉴이름=%s;"
                    cursor.execute(sql, i)
                for i in get_data2:
                    sql_time="update 판매내역 set 주문출고=now()  where 출고확인 is null"
                    sql_out="update 판매내역 set 출고확인='출고완료' where 출고확인 is null"
                    cursor.execute(sql_time)
                    cursor.execute(sql_out)




                sql_list=["update 재료재고,메뉴 set 재료재고.재료재고=메뉴.레시피1_재료재고 where 재료재고.재료=메뉴.레시피1;",
                          "update 재료재고,메뉴 set 재료재고.재료재고=메뉴.레시피2_재료재고 where 재료재고.재료=메뉴.레시피2;",
                          "update 재료재고,메뉴 set 재료재고.재료재고=메뉴.레시피3_재료재고 where 재료재고.재료=메뉴.레시피3;",
                          "update 메뉴,재료재고 set 메뉴.레시피1_재료재고=재료재고.재료재고 where 메뉴.레시피1=재료재고.재료;",
                          "update 재료재고,메뉴 set 메뉴.레시피2_재료재고=재료재고.재료재고 where 메뉴.레시피2=재료재고.재료;",
                          "update 재료재고,메뉴 set 메뉴.레시피3_재료재고=재료재고.재료재고 where 메뉴.레시피3=재료재고.재료;"]

                for i in sql_list:
                    cursor.execute(i)

                db.commit()
                db.close()

                flag=1

            else:
                get_data2 = list(get_data.decode('utf-8').split(','))
                get_data2.pop()
                put_data = data
                db = pymysql.connect(host='192.168.0.13', port=3306, user='root', passwd='1234', db='Project', charset='utf8')
                cursor = db.cursor()

                for i in get_data2:
                    sql1 = "select 메뉴이름 from 메뉴 where 메뉴이름=%s;"
                    cursor.execute(sql1, i)
                    res1 = cursor.fetchone()
                    rec1 = (list(res1))
                    print(rec1)

                    sql2 = "select 메뉴가격 from 메뉴 where 메뉴이름=%s;"
                    cursor.execute(sql2,i)
                    res2 = cursor.fetchone()
                    rec2=(list(res2))
                    print(rec2)

                    ##################통신연동 시 사용 할 영수증 쿼리문######################
                    sql3= "insert into 판매내역 values (%s,now(),%s,%s,%s);"
                    a=rec1
                    b=None
                    c=rec2
                    d=None
                    data = (a,b,c,d)
                    cursor.execute(sql3, data)

                db.commit()
                db.close()
                flag =1
            time.sleep(2)

    def c_send(self,put_data):
        self.c_socket.send(put_data.encode('utf-8'))


def creat_thread(s_socket):
    global index
    t.append(Cserver(s_socket))
    t[index].setdaemon=True
    t[index].start()

t=[]
put_data=""
get_data=""
data=""
get_data2=[]
flag=0
index=0
s_socket = socket(AF_INET, SOCK_STREAM)
s_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
ufsize=1024
host = ''
port = 9988
s_socket.bind((host,port))
s_socket.listen(5)
creat_thread(s_socket)

def main_thread():
    global put_data
    global flag
    while True:
        flag = 0
        if Cserver(put_data)=='1':
            break
        try:
            if put_data=="":
                pass
            else :
                if flag == 1:
                    for i in t:
                        i.c_send(put_data)
                        time.sleep(0.5)
                    put_data=""
        except Exception as e:
            pass

    for j in t:
        try:
            j.c_socket.close()
        except Exception as e:
            pass
    s_socket.close()

def subthread(snd_Text):
    global put_data
    try:
        for i in t:
            i.c_send(snd_Text)
            time.sleep(0.1)
    except Exception as e:
        pass


main_thread=threading.Thread(target=main_thread)
main_thread.daemon=True
main_thread.start()


sub_thread=threading.Thread(target=subthread(0))
sub_thread.daemon=True
sub_thread.start()
