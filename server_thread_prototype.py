#-*- coding: utf-8 -*-
from socket import *
import threading
import time
import Adafruit_SSD1306
import RPi.GPIO as GPIO
from PIL import Image, ImageDraw, ImageFont


btnOrder=14
btnCancel=15
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(btnOrder,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btnCancel,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
global r_flag

def send(sock):
    try:
        while True:
            if GPIO.input(btnOrder)==GPIO.HIGH :
                sock.send('주문접수'.encode('utf-8'))
                print('send:주문접수')
                time.sleep(0.5)
                r_flag=0
            elif GPIO.input(btnCancel)==GPIO.HIGH:
                sock.send('주문취소'.encode('utf-8'))
                print('send:주문거절')
                r_flag=0
                time.sleep(0.5)
            time.sleep(0.01)
    except Exception as e:
        print(e)
        pass
def receive(sock):
    try:
        while True:
            recvData = sock.recv(1024)
            if recvData.decode('utf-8')=='주문완료':
                print('receive:주문완료')
            elif recvData.decode('utf-8')=='주문취소':
                print('receive:주문취소')
                r_flag=0
    except:
        pass
HOST=''
PORT=8888

serverSock=socket(AF_INET,SOCK_STREAM)
try:
    serverSock.bind((HOST,PORT))
except socket.error:
    print('bind failed')
serverSock.listen(5)
print('succes!')
conn,addr = serverSock.accept()
print('connected')
user="123"
while True:
    try:
        sender = threading.Thread(target=send,args=(conn,))
        receiver=threading.Thread(target=receive,args=(conn,))
        sender.start()
        receiver.start()
        sender.join()
        receiver.join()
        time.sleep(0.5)
    except KeyboardInterrupt as e:
        print(e)
        conn.close()
        break

    
