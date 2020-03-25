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

btn_up = 26
btn_down = 19
btn_ok = 13
btn_order = 21
btn_test = 20
flg=0
HOST = '192.168.0.2'
PORT = 9988
global menuindex
names = ['아메리카노','카페모카','카페라떼','레몬에이드','초코라떼','에스프레소']
choice_menu=[]
order_cnt=[]
for i in range(len(names)):
    order_cnt.append(0)


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
        
def menu(device, draw, menustr,index):
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
            else:
                draw.text((2, i*15), menustr[i], font=font, fill=255)
    else:
        for i in range(index-3,index+2):
            if (i == index):
                menuindex = i
                invert(draw, 2, (i-(index-3))*15, menustr[i])
            elif (i==len(menustr)):
                pass
            else:
                draw.text((2, (i-(index-3))*15), menustr[i], font=font, fill=255)        


def sw_callback(channel):  
    global menuindex
    global insubmenu
    global order_cnt
    global choice_menu
    global flg
    font =ImageFont.truetype("/fonts/trutype/nanum/NanumBarunGothic.ttf",15)
    try:
        if flg==0:
            with canvas(device) as draw:
                draw.rectangle(device.bounding_box, outline="white", fill="black")
                draw.text((30, 20), "장바구니에",font=font, fill="white")
                draw.text((20, 35), "추가되었습니다", font=font,fill="white")
                choice_menu.append(names[menuindex])
                order_cnt[menuindex] +=1

        elif flg==1:
            with canvas(device) as draw:
                draw.rectangle(device.bounding_box, outline="white", fill="black")
                draw.text((38, 25), "주문 접수",font=font, fill="white")
                order_list=','.join(choice_menu)
                sock.send(order_list.encode('utf-8'))
                
        elif flg==2:
            with canvas(device) as draw:
                menu(device, draw, names,0)
            flg=0
        elif flg==3:
            sock.send('세팅수락'.encode('utf-8'))

    except:
        pass
def order_page(channel):
    global flg
    global order_cnt
    flg = not flg
    if flg == 1:
        with canvas(device) as draw:
            menu2(device, draw, names,0)
    elif flg ==0:
        choice_menu=[]
        order_cnt=[]
        for i in range(len(names)):
            order_cnt.append(0)
        with canvas(device) as draw:
            menu(device, draw, names,0)
        
            


def rotary_callback1(channel):  
    global menuindex
    global flg
    try:
        menuindex -= 1
        if flg==0:
            with canvas(device) as draw:
                menu(device, draw, names,menuindex%len(names))
        elif flg==1:
            with canvas(device) as draw:
                menu2(device, draw, names,menuindex%len(names))
    finally:
        print("Ending")
def rotary_callback2(channel):
    global menuindex
    global flg
    try:
        menuindex += 1
        if flg==0:
            with canvas(device) as draw:
                menu(device, draw, names,menuindex%len(names))
        elif flg==1:
            with canvas(device) as draw:
                menu2(device, draw, names,menuindex%len(names))
    finally:
        print("Ending")
def test(channel):
    sock.send('제품출고'.encode('utf-8'))

def recv(sock):
    global flg
    global choice_menu
    global order_cnt
    global names
    font =ImageFont.truetype("/fonts/trutype/nanum/NanumBarunGothic.ttf",15)
    try:
        while True:
            sleep(0.1)
            recv=sock.recv(1024)
            #print(recv.decode('utf-8'))
            if recv.decode('utf-8')=='주문완료':
                with canvas(device) as draw:
                    draw.rectangle(device.bounding_box, outline="white", fill="black")
                    draw.text((20, 30), "주문접수완료",font=font, fill="white")
                    choice_menu=[]
                    order_cnt=[]
                    for i in range(len(names)):
                        order_cnt.append(0)
                flg=2
            elif recv.decode('utf-8')=='메뉴세팅':
                with canvas(device) as draw:
                    draw.rectangle(device.bounding_box, outline="white", fill="black")
                    draw.text((10, 30), "메뉴가 변경됩니다",font=font, fill="white")
                flg=3
            elif recv.decode('utf-8')=='세팅완료':
                with canvas(device) as draw:
                    draw.rectangle(device.bounding_box, outline="white", fill="black")
                    draw.text((5, 20), "메뉴가 변경되었습니다",font=font, fill="white")
                    draw.text((10, 35), "다시 주문해주세요",font=font, fill="white")
                    choice_menu=[]
                    order_cnt=[]
                    for i in range(len(names)):
                        order_cnt.append(0)
                    flg=2        
            elif recv.decode('utf-8') != ','.join(choice_menu):
                names=list(recv.decode('utf-8').split(','))
                sock.send('메뉴확인'.encode('utf-8'))
            
                
                           
    except:
        pass

    



GPIO.add_event_detect(btn_up, GPIO.RISING , callback=rotary_callback1, bouncetime=250)
GPIO.add_event_detect(btn_down,GPIO.RISING, callback=rotary_callback2, bouncetime=250)
GPIO.add_event_detect(btn_ok, GPIO.RISING , callback=sw_callback, bouncetime=300)
GPIO.add_event_detect(btn_order, GPIO.RISING, callback=order_page ,bouncetime=300)
GPIO.add_event_detect(btn_test, GPIO.RISING, callback=test ,bouncetime=300)



try:
    with canvas(device) as draw:
        menu(device, draw, names,0)
    t=Thread(target=recv,args=(sock,))
    t.daemon = True
    t.start()
    
except KeyboardInterrupt:
    GPIO.clear()
    
        
        
    
