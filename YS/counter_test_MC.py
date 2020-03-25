#-*- coding: utf-8 -*-
from threading import Thread
import socket
from RPi import GPIO
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
from time import sleep
import socket
from PIL import ImageFont, ImageDraw

HOST = '192.168.0.2'
PORT = 9988
btn_up = 26
btn_down = 19
btn_ok = 13
btn_order = 21
btn_test = 20
global menuindex
order_cnt=[]
global order_list
order_list=[]
    
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST,PORT))
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn_up, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_down, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_ok, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_order, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_test, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)

def invert(draw,x,y,text):
    font =ImageFont.truetype("/fonts/trutype/nanum/NanumBarunGothic.ttf",14)
    draw.rectangle((x, y, x+128, y+15), outline=255, fill=255)
    draw.text((x, y), text, font=font, outline=0,fill="black")
    
# Box and text rendered in portrait mode
def menu2(device, draw, menustr,index):
    global menuindex
    global order_cnt
    font2 =ImageFont.truetype("/fonts/trutype/nanum/NanumBarunGothic.ttf",11)
    font =ImageFont.truetype("/fonts/trutype/nanum/NanumBarunGothic.ttf",14)
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    if index <4 :
        for i in range(len(menustr)): 
            if( i == index):
                menuindex = i
                invert(draw, 2, i*15, menustr[i])
                invert(draw, 62, i*15, str(order_cnt[i]))
            else:
                draw.text((2, i*15), menustr[i], font=font, fill=255)
                draw.text((62, i*15), str(order_cnt[i]), font=font, fill=255)
    else:
        for i in range(index-3,index+2):
            if (i == index):
                menuindex = i
                invert(draw, 2, (i-(index-3))*15, menustr[i])
                invert(draw, 62, (i-(index-3))*15, str(order_cnt[i]))
            elif (i==len(menustr)):
                pass
            else:
                draw.text((2, (i-(index-3))*15), menustr[i], font=font, fill=255)
                draw.text((62, (i-(index-3))*15), str(order_cnt[i]), font=font, fill=255)
                
def rotary_callback1(channel):  
    global menuindex
    global order_list
    global order_menu
    global flg
    try:
        menuindex -= 1
        with canvas(device) as draw:
            menu2(device, draw, order_menu,menuindex%len(order_menu))
    finally:
        print("Ending")
        
def rotary_callback2(channel):
    global menuindex
    global order_list
    global order_menu
    try:
        menuindex += 1
        with canvas(device) as draw:
            menu2(device, draw, order_menu,menuindex%len(order_menu))
    finally:
        print("Ending")
        
def recv(sock):
    global order_list
    global order_cnt
    global order_menu
    font =ImageFont.truetype("/fonts/trutype/nanum/NanumBarunGothic.ttf",15)
    try:
        while True:
            sleep(0.1)
            recv=sock.recv(1024)
            print(recv.decode('utf-8'))
            if recv.decode('utf-8')=='주문완료':
                pass
            elif recv.decode('utf-8')=='메뉴세팅':
                pass
            elif recv.decode('utf-8')=='세팅완료':
                pass        
            elif ',' in recv.decode('utf-8'):
                order_list=list(recv.decode('utf-8').split(','))
                order_menu=list(set(order_list))
                for i in order_menu:
                    order_cnt.append(order_list.count(i))
                with canvas(device) as draw:
                    menu2(device, draw, order_menu,0)
            
                
                           
    except:
        pass
    
GPIO.add_event_detect(btn_up, GPIO.RISING , callback=rotary_callback1, bouncetime=250)
GPIO.add_event_detect(btn_down,GPIO.RISING, callback=rotary_callback2, bouncetime=250)
#GPIO.add_event_detect(btn_ok, GPIO.RISING , callback=sw_callback, bouncetime=300)
#GPIO.add_event_detect(btn_order, GPIO.RISING, callback=order_page ,bouncetime=300)
#GPIO.add_event_detect(btn_test, GPIO.RISING, callback=test ,bouncetime=300)

try:
    t=Thread(target=recv,args=(sock,))
    t.daemon = True
    t.start()
    
except KeyboardInterrupt:
    GPIO.clear()