#-*- coding: utf-8 -*-
from socket import *
import threading
import sys
import RPi.GPIO as GPIO
import time
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont

btnOrder=14
btnCancel=15
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(btnOrder, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btnCancel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def send(sock):
    try:
        while True:
            time.sleep(0.1)
            if GPIO.input(btnOrder)==GPIO.HIGH:
                    sock.send('주문완료'.encode('utf-8'))
                    print('send:주문완료')
                    time.sleep(0.5)
            elif GPIO.input(btnCancel)==GPIO.HIGH:
                    sock.send('주문취소'.encode('utf-8'))
                    print('send:주문취소')
                    time.sleep(0.5)
    except:
        pass
def receive(sock):
    try:


        while True:
            time.sleep(1)
            recvData = sock.recv(1024)
            if recvData.decode('utf-8') == '주문접수':
                print('receive:주문접수')
            elif recvData.decode('utf-8')=='주문취소':
                print('recevie:주문거절')
    except:
        pass
HOST='192.168.0.140'
PORT=8888

clientSock=socket(AF_INET,SOCK_STREAM)
clientSock.connect((HOST,PORT))
user="test"
while True:
    try:
        sender=threading.Thread(target=send,args=(clientSock,))
        receiver=threading.Thread(target=receive,args=(clientSock,))
        sender.start()
        receiver.start()
        receiver.join()
        sender.join()
        time.sleep(0.5)
    except KeyboardInterrupt as e:
        print(e)
        conn.close()
        break
