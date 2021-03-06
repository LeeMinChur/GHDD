import socket
import threading
import socketserver
import time
import argparse
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
import RPi.GPIO as GPIO


freq=24000
bitsize=-16
channels=1
sbuffer=2048
ordercheckmp3="ordercheck.mp3"
orderconfirmmp3="ordercomfirm.mp3"
orderdeniedmp3="orderdenied.mp3"
ordercancelmp3="ordercancel.mp3"
productout="productout.mp3"


order_list=['이민철','장윤수','박대원','홍영신','장승주','전진영','문선규']
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
GPIO.setwarnings(False)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    
while True:
        image = Image.new('1',(width, height))
        draw = ImageDraw.Draw(image)
        disp.clear()
        draw.text((x+29,top),'Order List',font=font, fill=255)
        temp=[]
        for i in range(len(order_list)):
            temp.append(order_list[i])
            draw.text((x,top+8*(i+1)), '{}'.format(order_list[i]), font=font, fill=255)
        temp_all.append(temp)
        draw.text((x,top+56),'1.OK 2.Cancel 3.Bye',font=font, fill=255)
        disp.image(image)
        disp.display()
        if GPIO.input(button2)==GPIO.HIGH:
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



'''temp_all = []      
while True:
    try:        
        print(order_list)
        image = Image.new('1',(width, height))
        draw = ImageDraw.Draw(image)
        disp.clear()
        draw.text((x+29,top),'Order List',font=font, fill=255)
        temp=[]
        for i in range(len(order_list)):
            temp.append(order_list[i])
            draw.text((x,top+8*(i+1)), '{}'.format(order_list[i]), font=font, fill=255)
        temp_all.append(temp)
        draw.text((x,top+56),'1.OK 2.Cancel 3.Bye',font=font, fill=255)
        disp.image(image)
        disp.display()
        time.sleep(2)
        if GPIO.input(button1)==GPIO.HIGH:
            send(s)
            image = Image.new('1',(width, height))
            draw = ImageDraw.Draw(image)
            disp.clear()
            draw.text((x+29,top+25), 'OK', font=font, fill=255)
            mp3(orderconfirmmp3)
            disp.image(image)
            disp.display()
            
        if GPIO.input(button2)==GPIO.HIGH:
            image = Image.new('1',(width, height))
            draw = ImageDraw.Draw(image)
            disp.clear()
            draw.text((x+29,top+25), 'Cancle', font=font, fill=255)
            mp3(orderdeniedmp3)
            disp.image(image)
            disp.display()
            
        if GPIO.input(button3)==GPIO.HIGH:
            image = Image.new('1',(width, height))
            draw = ImageDraw.Draw(image)
            disp.clear()
            draw.text((x+29,top+25), 'Bye', font=font, fill=255)
            disp.image(image)
            disp.display()
            mp3(ordercheckmp3)
            
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
        time.sleep(2)
        #thread()
    except KeyboardInterrupt as e:
        print(e)
        s.close()
        conn.close()
        break'''

