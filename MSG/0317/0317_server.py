from socket import *
import threading
import time
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
        global put_data
        print(self.c_socket)
        while True:
            get_data=self.c_socket.recv(1024)
            print('receive:%s'%get_data.decode('utf-8'))
            data = get_data.decode('utf-8')
            if data == 'a':
                put_data='a'
            elif data =='b':
                put_data='b'
            elif data =='c':
                put_data='c'
            elif data =='d':
                put_data='d'
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
index=0
s_socket = socket(AF_INET, SOCK_STREAM)
s_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
ufsize=1024
host = ''
port = 9988
s_socket.bind((host,port))
s_socket.listen(5)
creat_thread(s_socket)
while True:
    if Cserver(put_data)=='1':
        break
    try:
        for i in t:
            i.c_send(put_data)
            time.sleep(0.5)
    except Exception as e:
        pass

for j in t:
    try:
        j.c_socket.close()
    except Exception as e:
        pass
s_socket.close()
