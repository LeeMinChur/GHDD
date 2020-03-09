#-*- coding: utf-8 -*-
import socket
import sys
import RPi.GPIO as GPIO
import time
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont

HOST = '192.168.0.140'
PORT = 8888

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

disp=Adafruit_SSD1306.SSD1306_128_64(rst=None, i2c_address=0x3C)

disp.begin()
disp.clear()
disp.display()

width=disp.width
height=disp.height
image=Image.new('1',(width, height))
draw=ImageDraw.Draw(image)
draw.rectangle((0,0,width,height),outline=0, fill=0)
padding=-2
top=padding
bottom=height-padding
x=0
font=ImageFont.load_default()
button1=14
button2=15
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while True:
    image=Image.new('1',(width,height))
    draw=ImageDraw.Draw(image)
    draw.text((x,top), 'HI', font=font, fill=255)
    if GPIO.input(button1)==GPIO.HIGH:
        draw.text((x,top+8), 'order', font=font, fill=255)
        s.send('주문완료')
    elif GPIO.input(button2)==GPIO.HIGH:
        draw.text((x,top+8), 'cancle', font=font,fill=255)
        s.send('주문취소')
    disp.image(image)
    disp.display()
    time.sleep(0.2)
    #data=raw_input('Enter comma:')
    # s.send(data)
    # reply = s.recv(1024)
    # print('recevied server'+r
