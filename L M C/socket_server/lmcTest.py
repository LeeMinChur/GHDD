import socket
import threading
import socketserver
import time
import argparse
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
import RPi.GPIO as GPIO
import pygame

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

freq=24000
bitsize=-16
channels=1
sbuffer=2048
ordercheckmp3="ordercheck.mp3"
orderconfirmmp3="ordercomfirm.mp3"
orderdeniedmp3="orderdenied.mp3"
ordercancelmp3="ordercancel.mp3"
productout="productout.mp3"

print ('Socket created')




order_list=['민철','민철','민철','영신','윤수','진영','영신','윤수','선규','선규']
#order_list=['ham','ber',:

disp = Adafruit_SSD1306.SSD1306_128_64(rst=None, i2c_address=0x3C)
disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1',(width, height))
draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width,height), outline = 0, fill=0)

padding = -2
top = padding
button1 = 24
button2 = 23
button3 = 18
button4 = 25
button5 = 8
x = 0

font = ImageFont.load_default()
font1=ImageFont.truetype("/fonts/frutype/nanum/NanumBarunGothic.ttf",10)
GPIO.setwarnings(False)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def send(sock):
    while True:
        try:
            conn.send('주문완료'.encode('utf-8'))
            time.sleep(0.001)
            if GPIO.input(button1)==GPIO.HIGH:
                sock.send('주문완료'.encode('utf-8'))
                break
        except:
            pass
while True:
    try: 
        image=Image.new('1',(width,height))
        draw = ImageDraw.Draw(image)
        disp.clear()
        draw.text((x+29,top),'order list',font=font, fill=255)
        ovlap=[]
        for i in range(len(order_list)):
            ovlap =list( set(order_list))
        print(ovlap)
        c = []
        for i in ovlap:
            c.append(order_list.count(str(i)))
        print(c)
        temp_all = []      
        temp=[]
        s = (2*5)+1
        #draw.text((x+50,top+8*(i+1)),'{}'.format(c),font=font1, fill=255)
        for i in range(len(order_list)):
            temp.append(order_list[i])
        for i in range(len(ovlap)):
            draw.text((x,top+(s*(i+1))), '{}'.format(ovlap[i]), font=font1, fill=255)
            draw.text((x+40,top+(s*(i+1))), '{}'.format(c[i]), font=font1, fill=255)
            if ovlap[4] or c[4] :
                print('멈춤')
                break
        draw.text((x,top+56),'1.OK 2.Cancel 3.Bye',font=font, fill=255)
        disp.image(image)
        disp.display()
        if GPIO.input(button1)==GPIO.HIGH:
            sock.send('주문완료'.encode('utf-8'))
            break            
            
        if GPIO.input(button2)==GPIO.HIGH:
            conn.send('주문완료'.encode('utf-8'))
            image = Image.new('1',(width, height))
            draw = ImageDraw.Draw(image)
            disp.clear()
            draw.text((x+29,top+25), 'Cancle', font=font, fill=255)
            #mp3(orderdeniedmp3)
            disp.image(image)
            disp.display()
                
        if GPIO.input(button3)==GPIO.HIGH:
            image = Image.new('1',(width, height))
            draw = ImageDraw.Draw(image)
            disp.clear()
            draw.text((x+29,top+25), 'Bye', font=font, fill=255)
            disp.image(image)
            disp.display()
            #mp3(ordercheckmp3)
                
        if GPIO.input(button4)==GPIO.HIGH:
            image = Image.new('1',(width, height))
            draw = ImageDraw.Draw(image)
            disp.clear()
            for i in range(len(temp_all)):
                draw.text((x,top+8*(i+1)), '{}'.format(temp_all[i]), font=font, fill=255)
            disp.image(image)
            disp.display()
                    
        if GPIO.input(button5)==GPIO.HIGH:
            break
                
        disp.image(image)
        disp.display()
        time.sleep(0.01)
    except KeyboardInterrupt as e:
            
        s.close()
        sock.close()
        break



