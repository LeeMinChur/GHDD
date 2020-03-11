#-*-coding:utf-8-*-

import time
import socket
import threading
import sys
import Adafruit_SSD1306
import RPi.GPIO as GPIO
from PIL import Image, ImageDraw, ImageFont

HOST = ''
PORT = 8888
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
disp=Adafruit_SSD1306.SSD1306_128_64(rst=None, i2c_address=0x3C)
print ('Socket Created')


disp = Adafruit_SSD1306.SSD1306_128_64(rst=None, i2c_address=0x3C)
disp.begin()

#화면 클리어
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1',(width, height))
draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width,height), outline = 0, fill=0)

padding = -2
top = padding
button1 = 18
button2 = 23
button3 = 24
x = 0

font = ImageFont.load_default()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
global r_flag

try:
    s.bind((HOST,PORT))
except socket.error:
    print('Bind failed')

s.listen(5)
print('Socket waiting messages')
conn, addr = s.accept()
list_test = []
print('Connected')

while True:
   # if conn.recv(1024).decode('utf-8') != '주문접수':
        list_test.append(conn.recv(1024).decode('utf-8'))
        print(conn.recv(1024).decode('utf-8'))
        print(list_test)
   # else:
     #   break
        
draw.text((x,top),list_test, font=font, fill =255)
        


'''
draw.text((x,top),temp, font=font, fill =255)            
draw.text((x,top+50), '1.Check', font=font, fill=255)
draw.text((x,top+60), '2.Cancle', font=font, fill=255)
draw.text((x,top+70), '3.OB', font=font, fill=255)
            
if GPIO.input(button1)==GPIO.HIGH:
    draw.text((x,top), '1.Client', font=font, fill=255)
    draw.text((x,top+10), '2.Manager', font=font, fill=255) 
                
    if GPIO.input(button1)==GPIO.HIGH:
        image = Image.new('1',(width, height))
        draw = ImageDraw.Draw(image)
        disp.clear()
        disp.display()
                
    elif GPIO.input(button2)==GPIO.GIGH:
        image = Image.new('1',(width, height))
        draw = ImageDraw.Draw(image)
        disp.clear()
        disp.display()
                
elif GPIO.input(button2)==GPIO.HIGH:
    image = Image.new('1',(width, height))
    draw = ImageDraw.Draw(image)
    disp.clear()
    disp.display()
    draw.text((x,top), 'You Choice Cancle', font=100, fill=255)
            
elif GPIO.input(button3)==GPIO.HIGH:
    image = Image.new('1',(width, height))
    draw = ImageDraw.Draw(image)
    disp.clear()
    disp.display()
    draw.text((x,top), 'OB', font=font, fill=255)
    
disp.image(image)
disp.display()
time.sleep(2)
'''
conn.close()
   
