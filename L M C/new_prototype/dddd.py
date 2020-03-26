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
btn_up = 24
btn_down = 23
button3 = 18
button4 = 25
button5 = 8
flg = 0

global menuindex
order_cnt=[]
global order_list
order_list=[]
global order_all
order_all=[]
    
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST,PORT))
GPIO.setmode(GPIO.BCM)

GPIO.setup(btn_up, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_down, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)




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
    global flg
    global order_list
    global order_cnt
    global order_menu
    global order_all
    font =ImageFont.truetype("/fonts/trutype/nanum/NanumBarunGothic.ttf",15)
    try:
        while True:
            sleep(0.1)
            recv=sock.recv(1024)
            print(recv.decode('utf-8'))
            if recv.decode('utf-8')=='주문완료':
                print('주문완료')
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
                order_all.append(order_menu)
                with canvas(device) as draw:
                    menu2(device, draw, order_menu,0)
                print(order_all)
    except:
        pass
    
    
def sdcallback(channel):    
    global flg
    global order_list
    global order_menu
    font =ImageFont.truetype("/fonts/trutype/nanum/NanumBarunGothic.ttf",15)
    try:
        print(flg)
        if flg == 0:
            print('send')
            with canvas(device) as draw:
                draw.text((20,5), '주문완료 되었습니다.', font=font, fill=255)
            sock.send('주문완료'.encode('utf-8'))
            order_list=[]
            print(flg)
            flg=2
            pass           
        elif flg == 2:
            with canvas(device) as draw:
                draw.text((20,25), '제품출고 되었습니다.', font=font, fill=255)
            sock.send('제품출고'.encode('utf-8'))
            flg=0
    except:
        pass
        
def orderlist(channel):

    global flg
    global order_list
    global order_cnt
    global order_menu
    global order_all
    font1=ImageFont.truetype("/fonts/frutype/nanum/NanumBarunGothic.ttf",10)
    try:
        draw.text((x+29,top),'order list',font=font, fill=255)
        draw.text((x+20,top+29),'1.Client1  2.Clinet2 ',font=font1, fill=255)
        draw.text((x+20,top+41),'3.Client2  4.Clinet4 ',font=font1, fill=255)
        if GPIO.input(button1)==GPIO.HIGH:
            while True:
                for i in range(len(order_all[0])):
                    draw.text((x,top+12+(s*(i))), '{}'.format(order_all[0][i]), font=font1, fill=255)                   
                    draw.text((x+40,top+56),'5.이전단계',font=font1, fill=255)
                    if GPIO.input(button5)==GPIO.HIGH:
                        break        
    except:
        pass
            

GPIO.add_event_detect(button4,GPIO.RISING, callback=orderlist, bouncetime=250)
GPIO.add_event_detect(button3,GPIO.RISING, callback=sdcallback, bouncetime=200)    
GPIO.add_event_detect(btn_up, GPIO.RISING , callback=rotary_callback1, bouncetime=250)
GPIO.add_event_detect(btn_down,GPIO.RISING, callback=rotary_callback2, bouncetime=250)

try:
    receiver=Thread(target=recv,args=(sock,))
    receiver.daemon = True
    receiver.start()
    
except KeyboardInterrupt:
    GPIO.clear()
