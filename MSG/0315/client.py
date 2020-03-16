# -*- coidng:utf-8-*-

import  socket
import sys

HOST,PORT = "192.168.0.13",3000

try:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((HOST,PORT))

except socket.error as msg:
    print("fail to creat socket. Error code:%s \n Error Message : %s" % (str(msg[0]), msg[1]))
    sys.exit(0)

print("socket created")

while True:
    try:
        data = input("input:")
        if data == ":/quit" or not data:
            sock.close()
            break

        try:
            sock.sendall(data.encode()+"\n".encdoe())
            received=sock.recv(1024)
        finally:
            print("senet:        {}".format(data))
            print("received:    {}".format(received.decode())
        except KeyboardInterrupt as e:
            print(e)
            data = ":/quit"

sock.close()
