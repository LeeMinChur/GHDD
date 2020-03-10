#-*- coding: utf-8 -*-
from socket import *
import threading
import time
import Adafruit_SSD1306
import RPi.GPIO as GPIO
from PIL import Image, ImageDraw, ImageFont

#disp=Adafruit_SSD1306.SSD1306_128_64(rst=None, i2c_address=0x3C)
#disp.begin()
#disp.clear()
#disp.display()
#width=disp.width
#height=disp.height
#image=Image.new('1',(width,height))
#draw=ImageDraw.Draw(image)
#padding=-2
#top=padding
#botton=height-padding
#x=0
#font=ImageFont.load_default()

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
                r_flag=0
                break
            elif GPIO.input(btnCancel)==GPIO.HIGH:
                sock.send('주문취소'.encode('utf-8'))
                print('send:주문거절')
                r_flag=0
                break
    except:
        pass
def receive(sock):
    try:
        while True:
            recvData = sock.recv(1024)
            if recvData.decode('utf-8')=='주문완료':
                #draw.text((x,top),'order',font=font,fill=255)
                print('receive:주문완료')
                break
            elif recvData.decode('utf-8')=='주문취소':
                print('receive:주문취소')
                r_flag=0
                break
    except:
        pass
HOST=''
PORT=8888

serverSock=socket(AF_INET,SOCK_STREAM)
serverSock.bind((HOST,PORT))
serverSock.listen(5)
conn,addr = serverSock.accept()
while True:
    try:
        sender = threading.Thread(target=send,args=(conn,))
        receiver=threading.Thread(target=receive,args=(conn,))
        sender.start()
        receiver.start()
        sender.join()
        receiver.join()
        #image=Image.new('1',(width,height))
        #draw=ImageDraw.Draw(image)
        #disp.image(image)
        #disp.display()
        time.sleep(0.5)
    except KeyboardInterrupt as e:
        print(e)
        break

    
