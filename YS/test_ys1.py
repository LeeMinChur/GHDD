#-*- coding: utf-8 -*-
from threading import Thread
import socket
from RPi import GPIO
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
import time 
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
names = ['1','2','3','4']
choice_menu=[]
order_cnt=[]
menu_price=['1','2','3','4']
for i in range(len(names)):
    order_cnt.append(0)
now=time.localtime()
menuindex=0


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
    font2 =ImageFont.truetype("/fonts/trutype/nanum/NanumBarunGothic.ttf",15)
    font =ImageFont.truetype("/fonts/trutype/nanum/NanumBarunGothic.ttf",14)

    draw.rectangle((0,15,127,63), outline="white", fill="black")
    draw.text((38,0),"주문확인", font=font, fill='white')
    if index <3 :
        for i in range(len(menustr)): 
            if( i == index):
                menuindex = i
                invert(draw, 2, (i*15)+15, menustr[i])
                invert(draw, 90, (i*15)+15, str(order_cnt[i]))
            else:
                draw.text((2, (i*15)+15), menustr[i], font=font, fill=255)
                draw.text((90, (i*15)+15), str(order_cnt[i]), font=font, fill=255)
    else:
        for i in range(index-2,index+1):
            if (i == index):
                menuindex = i
                invert(draw, 2, ((i-(index-2))*15+15), menustr[i])
                invert(draw, 90, ((i-(index-2))*15+15), str(order_cnt[i]))
            elif (i==len(menustr)):
                pass
            else:
                draw.text((2, ((i-(index-2))*15)+15), menustr[i], font=font, fill=255)
                draw.text((90, ((i-(index-2))*15)+15), str(order_cnt[i]), font=font, fill=255)
            
def menu(device, draw, menustr,index):
    global menuindex
    global order_cnt
    global menu_price
    font2 =ImageFont.truetype("/fonts/trutype/nanum/NanumBarunGothic.ttf",15)
    font =ImageFont.truetype("/fonts/trutype/nanum/NanumBarunGothic.ttf",14)
    draw.rectangle((0,15,127,63), outline="white", fill="black")
    draw.text((38,0),"메뉴목록", font=font, fill='white')
    if index <3 :
        for i in range(len(menustr)): 
            if( i == index):
                menuindex = i
                invert(draw, 2, (i*15)+15, menustr[i])
                invert(draw, 90, (i*15)+15, menu_price[i])
            else:
                draw.text((2, (i*15)+15), menustr[i], font=font, fill=255)
                draw.text((90, (i*15)+15), menu_price[i], font=font, fill=255)
    else:
        for i in range(index-2,index+1):
            if (i == index):
                menuindex = i
                invert(draw, 2, ((i-(index-2))*15+15), menustr[i])
                invert(draw, 90, ((i-(index-2))*15+15), menu_price[i])
            elif (i==len(menustr)):
                pass
            else:
                draw.text((2, ((i-(index-2))*15)+15), menustr[i], font=font, fill=255)
                draw.text((90, ((i-(index-2))*15)+15), menu_price[i], font=font, fill=255)          


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
                draw.text((38, 25), "주문접수",font=font, fill="white")
                order_list=','.join(choice_menu)+','
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
        
def cancel(channel):
    global flg
    global choice_menu
    global order_cnt
    font =ImageFont.truetype("/fonts/trutype/nanum/NanumBarunGothic.ttf",15)
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((43, 20), "주문이",font=font, fill="white")
        draw.text((15, 35), "취소되었습니다", font=font,fill="white")
        choice_menu=[]
        order_cnt=[]
        for i in range(len(names)):
            order_cnt.append(0)
        flg=2

def recv(sock):
    global flg
    global now
    global choice_menu
    global order_cnt
    global menu_price
    global names
    font =ImageFont.truetype("/fonts/trutype/nanum/NanumBarunGothic.ttf",15)
    try:
        while True:
            time.sleep(0.1)
            recv=sock.recv(1024)
            print(recv.decode('utf-8'))
            if recv.decode('utf-8')=='주문완료':
                if flg==1:
                    with canvas(device) as draw:
                        draw.rectangle(device.bounding_box, outline="white", fill="black")
                        draw.text((25, 10), "주문접수완료",font=font, fill="white")
                        draw.text((20, 25), "%04d/%02d/%02d" % (now.tm_year, now.tm_mon, now.tm_mday),font=font, fill="white")
                        draw.text((30, 40), "%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec),font=font, fill="white")
                        choice_menu=[]
                        order_cnt=[]
                        for i in range(len(names)):
                            order_cnt.append(0)
                    flg=2
                else:
                    pass
            elif recv.decode('utf-8')=='메뉴세팅':
                with canvas(device) as draw:
                    draw.rectangle(device.bounding_box, outline="white", fill="black")
                    draw.text((10, 30), "메뉴가변경됩니다",font=font, fill="white")
                flg=3
            elif recv.decode('utf-8')=='세팅완료':
                if flg==3:
                    with canvas(device) as draw:
                        draw.rectangle(device.bounding_box, outline="white", fill="black")
                        draw.text((43, 8), "메뉴가",font=font, fill="white")
                        draw.text((17, 23), "변경되었습니다", font=font,fill="white")
                        draw.text((10, 38), "다시주문해주세요",font=font, fill="white")
                        choice_menu=[]
                        order_cnt=[]
                        for i in range(len(names)):
                            order_cnt.append(0)
                        flg=2
                else:
                    with canvas(device) as draw:
                        menu(device, draw, names,0)
                    flg=0
                    order_cnt=[]
                    for i in range(len(names)):
                        order_cnt.append(0)
            elif '/' in recv.decode('utf-8'):
                names=list(recv.decode('utf-8').split('/'))
                names.pop()
                sock.send('메뉴확인'.encode('utf-8'))
            elif '.' in recv.decode('utf-8'):
                menu_price=list(recv.decode('utf-8').split('.'))
                menu_price.pop()
                sock.send('가격확인'.encode('utf-8'))
            
                
                           
    except:
        pass

    



GPIO.add_event_detect(btn_up, GPIO.RISING , callback=rotary_callback1, bouncetime=250)
GPIO.add_event_detect(btn_down,GPIO.RISING, callback=rotary_callback2, bouncetime=250)
GPIO.add_event_detect(btn_ok, GPIO.RISING , callback=sw_callback, bouncetime=300)
GPIO.add_event_detect(btn_order, GPIO.RISING, callback=order_page ,bouncetime=300)
GPIO.add_event_detect(btn_test, GPIO.RISING, callback=cancel ,bouncetime=300)



try:
    font =ImageFont.truetype("/fonts/trutype/nanum/NanumBarunGothic.ttf",15)
    while True:
        with canvas(device) as draw:
            menu(device, draw, names,0)
        
    t=Thread(target=recv,args=(sock,))
    t.daemon = True
    t.start()
    
except KeyboardInterrupt:
    GPIO.clear()
    
        