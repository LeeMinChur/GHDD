#-*- coding: utf-8 -*-
import socket
import argparse
import threading
import sys
import RPi.GPIO as GPIO
import time
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
import pygame
btnOrder=16
btnCancel=15
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(btnOrder, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btnCancel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
ordermp3="order.mp3"
ordercancelmp3="ordercancel.mp3"
orderacceptmp3="orderaccept.mp3"
freq=24000
bitsize=-16
channels=1
sbuffer=2048
def mp3(source):
    pygame.mixer.init(freq,bitsize,channels,sbuffer)
    pygame.mixer.music.load(source)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play()
    
def send(sock):
    try:
        while True:
            time.sleep(0.1)
            if GPIO.input(btnOrder)==GPIO.HIGH:
                    sock.sendall('주문완료'.encode('utf-8'))
                    mp3(ordermp3)
                    print('send:주문완료')
                    time.sleep(0.5)
            elif GPIO.input(btnCancel)==GPIO.HIGH:
                    sock.sendall('주문취소'.encode('utf-8'))
                    mp3(ordercancelmp3)
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
               # mp3(orderacceptmp3)
                print('receive:주문접수')
            elif recvData.decode('utf-8')=='주문거절':
               # mp3(orderdenied.mp3)
                print('recevie:주문거절')
            
    except:
        pass
HOST='192.168.0.133'
PORT=8888

clientSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientSock.connect((HOST,PORT))
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
        conn.socket.close()
        break
