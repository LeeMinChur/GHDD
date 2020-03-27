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
import pygame

HOST = '192.168.0.13'
PORT = 9988
button1 = 24
button2 = 23
button3 = 18
button4 = 25
button5 = 8
flg = 0
freq=24000
bitsize=-16
channels=1
sbuffer=2048


orderconfirmmp3="ordercomfirm.mp3"
productout="productout.mp3"

global menuindex
order_cnt=[]
global order_list
order_list=[]
global order_all
order_all=[]
global cnt_all
cnt_all=[]
    
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST,PORT))
GPIO.setmode(GPIO.BCM)

GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)




serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)

font1 =ImageFont.truetype("/fonts/trutype/nanum/NanumBarunGothic.ttf",14)
with canvas(device) as draw:
    draw.text((15,25), '          GHDD', font=font1, fill=255)
    
    
def mp3(source):
    pygame.mixer.init(freq,bitsize,channels,sbuffer)
    pygame.mixer.music.load(source)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play()
    


def invert(draw,x,y,text):
    font =ImageFont.truetype("/fonts/trutype/nanum/NanumBarunGothic.ttf",14)
    draw.rectangle((x, y, x+128, y+15), outline=255, fill=255)
    draw.text((x, y), text, font=font, outline=0,fill="black")
    
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
    global cnt_all
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
                order_list.pop()
                order_menu=list(set(order_list))
                for i in order_menu:
                    order_cnt.append(order_list.count(str(i)))
                cnt_all.append(order_cnt)
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
    global order_all
    global cnt_all
    font =ImageFont.truetype("/fonts/trutype/nanum/NanumBarunGothic.ttf",15)
    try:
        print('send')
        with canvas(device) as draw:
            draw.text((5,25), '주문완료 되었습니다.', font=font, fill=255)        
        mp3(orderconfirmmp3)
        sock.send('주문완료'.encode('utf-8'))
        order_list=[]
        pass
    except:
        pass
    
def sdcallback2(channel):
    global flg
    global order_list
    global order_menu
    global order_all
    global cnt_all
    font =ImageFont.truetype("/fonts/trutype/nanum/NanumBarunGothic.ttf",15)
    try:
        with canvas(device) as draw:
            draw.text((5,25), '제품출고 되었습니다.', font=font, fill=255)
        mp3(productout)
        sock.send('제품출고'.encode('utf-8'))
        order_all.pop(0)
        cnt_all.pop(0)
        print(order_all)
    except:
        pass
        
def orderlist(channel):
    print('3')
    global flg
    global order_list
    global order_cnt
    global order_menu
    global order_all
    global cnt_all
    s = (2*5)+1
    font2 = ImageFont.load_default()
    font1=ImageFont.truetype("/fonts/frutype/nanum/NanumBarunGothic.ttf",10)
    try:
        print('2')
        with canvas(device) as draw:
            draw.text((29,0),'order list',font=font2, fill=255)
            draw.text((20,29),'1.Client1  2.Clinet2 ',font=font2, fill=255)
            draw.text((20,41),'3.Client2  4.Clinet4 ',font=font2, fill=255)
                
        if GPIO.input(button1)==GPIO.HIGH:
            while True:
                for i in range(len(order_all[0])):
                    with canvas(device) as draw:
                        draw.text((29,0),'order list',font=font2, fill=255)
                        draw.text((0,12+(s*(i))), '{}'.format(order_all[0][i]), font=font1, fill=255)
                        draw.text((40,s*(i+1)), '{}'.format(cnt_all[0][i]), font=font1, fill=255)
                        draw.text((40,56),'5.이전단계',font=font1, fill=255)                                    
                if GPIO.input(button5)==GPIO.HIGH:
                    break
        elif GPIO.input(button2)==GPIO.HIGH:
            while True:
                for i in range(len(order_all[1])):
                    with canvas(device) as draw:
                        draw.text((29,0),'order list',font=font2, fill=255)
                        draw.text((0,12+(s*(i))), '{}'.format(order_all[1][i]), font=font1, fill=255)
                        draw.text((40,s*(i+1)), '{}'.format(cnt_all[1][i]), font=font1, fill=255)
                        draw.text((40,56),'5.이전단계',font=font1, fill=255)
                if GPIO.input(button5)==GPIO.HIGH:
                    break
        elif GPIO.input(button3)==GPIO.HIGH:
            while True:
                 for i in range(len(order_all[2])):
                     with canvas(device) as draw:
                        draw.text((29,0),'order list',font=font2, fill=255)
                        draw.text((0,12+(s*(i))), '{}'.format(order_all[2][i]), font=font1, fill=255)
                        draw.text((40,s*(i+1)), '{}'.format(cnt_all[2][i]), font=font1, fill=255)
                        draw.text((40,56),'5.이전단계',font=font1, fill=255)
                 if GPIO.input(button5)==GPIO.HIGH:
                     break
        elif GPIO.input(button4)==GPIO.HIGH:
            while True:
                for i in range(len(order_all[3])):
                    with canvas(device) as draw:
                        draw.text((29,0),'order list',font=font2, fill=255)
                        draw.text((0,12+(s*(i))), '{}'.format(order_all[3][i]), font=font1, fill=255)
                        draw.text((40,s*(i+1)), '{}'.format(cnt_all[3][i]), font=font1, fill=255)
                        draw.text((40,56),'5.이전단계',font=font1, fill=255)
                if GPIO.input(button5)==GPIO.HIGH:
                    break
    except:
        pass
    
    
GPIO.add_event_detect(button5,GPIO.RISING, callback=orderlist, bouncetime=250)             
GPIO.add_event_detect(button4,GPIO.RISING, callback=sdcallback2, bouncetime=200)  
GPIO.add_event_detect(button3,GPIO.RISING, callback=sdcallback, bouncetime=200)    
GPIO.add_event_detect(button1,GPIO.RISING, callback=rotary_callback1, bouncetime=250)
GPIO.add_event_detect(button2,GPIO.RISING, callback=rotary_callback2, bouncetime=250)


try:
    receiver=Thread(target=recv,args=(sock,))
    receiver.daemon = True
    receiver.start()
    
except KeyboardInterrupt:
    GPIO.clear()
