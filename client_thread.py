#-*- coding: utf-8 -*-
from socket import *
import threading
import sys
import RPi.GPIO as GPIO
import time
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont

#disp=Adafruit_SSD1306.SSD1306_128_64(rst=None, i2c_address=0x3C)

#disp.begin()
#disp.clear()
#disp.display()

#width=disp.width
#height=disp.height
#image=Image.new('1',(width, height))
#draw=ImageDraw.Draw(image)
#draw.rectangle((0,0,width,height),outline=0, fill=0)
#padding=-2
#top=padding
#bottom=height-padding
#x=0
#font=ImageFont.load_default()
btnOrder=14
btnCancel=15
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(btnOrder, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btnCancel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def send(sock):
    try:
        while True:
            if GPIO.input(btnOrder)==GPIO.HIGH:
                    sock.send('주문완료'.encode('utf-8'))
                    print('send:주문완료')
                    break
            elif GPIO.input(btnCancel)==GPIO.HIGH:
                    sock.send('주문취소'.encode('utf-8'))
                    print('send:주문취소')
                    break
    except:
        pass
def receive(sock):
    try:


        while True:
            recvData = sock.recv(1024)
           
            if recvData.decode('utf-8') == '주문접수':
                #draw.text((x,top),'order complete!!',font=font,fill=255)
                print('receive:주문접수')
                break
            elif recvData.decode('utf-8')=='주문취소':
                #draw.text((x,top+8),'oredr Denied!!',font=font,fill=255)
                print('recevie:주문거절')
                break
    except:
        pass
HOST='192.168.0.140'
PORT=8888

clientSock=socket(AF_INET,SOCK_STREAM)
clientSock.connect((HOST,PORT))

while True:
    try:
        sender=threading.Thread(target=send,args=(clientSock,))
        receiver=threading.Thread(target=receive,args=(clientSock,))
        sender.start()
        receiver.start()
        receiver.join()
        sender.join()
        #image=Image.new('1',(width,height))
        #draw=ImageDraw.Draw(image)
        #disp.image(image)
        #dist.display()
        time.sleep(0.5)
    except KeyboardInterrupt as e:
        print(e)
        break
