#-*- coding: utf-8 -*-
import socket
import socketserver
import ssl
import threading
import argparse
import time
import Adafruit_SSD1306
import RPi.GPIO as GPIO
from PIL import Image, ImageDraw, ImageFont
import pygame
user_list=[]
notice_flag=0
freq=24000
bitsize=-16
channels=1
sbuffer=2048
ordercheckmp3="ordercheck.mp3"
orderconfirmmp3="ordercomfirm.mp3"
orderdeniedmp3="orderdenied.mp3"
ringmp3="ring.mp3"
HOST=''
PORT=8888
btnOrder=14
btnCancel=15
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(btnOrder,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btnCancel,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
global r_flag
def mp3(source):
    pygame.mixer.init(freq,bitsize,channels,sbuffer)
    pygame.mixer.music.load(source)
    pygame.mixer.music.set_volume(0)
    pygame.mixer.music.play()
def send(sock):
    try:
        while True:
            if GPIO.input(btnOrder)==GPIO.HIGH :
                sock.send('주문접수'.encode('utf-8'))
                mp3(orderconfirmmp3)
                print('send:주문접수')
                time.sleep(0.5)
                r_flag=0
            elif GPIO.input(btnCancel)==GPIO.HIGH:
                sock.send('주문거절'.encode('utf-8'))
                print('send:주문거절')
                mp3(orderdeniedmp3)
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
                mp3(ringmp3)
                time.sleep(2)
                mp3(ordercheckmp3)
                print('receive:주문완료')
            elif recvData.decode('utf-8')=='주문취소':
                print('receive:주문취소')
                r_flag=0
    except:
        pass

serverSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("socket created!")
try:
    serverSock.bind((HOST,PORT))
except socket.error:
    serverSock.close()
    print('bind failed')
serverSock.listen(5)
#print('succes!')
#conn,addr = serverSock.accept()
#print('connected')
#print(conn)
def wheh():
    conn,(addr,port)=serverSock.accept()
    print(port)
    user_list.appand(port)
    t=threading.Thread(target=wheh)
    sender=threading.Thread(target=send,args=(conn,))
    receiver=threading.Thread(target=receive,args=(conn,))
    t.start()
    while True:
        print('connect:', addr,port)
        sender.start()
        receiver.start()
        sender.join()
        receiver.join()
        time.sleep(0.5)
        conn.close()

while True:
    try:
        wheh()
    except KeyboardInterrupt as e:
        print(e)
        serverSock.close()
        conn.close()
        break

    
