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

HOST = '192.168.0.2'
PORT = 9988
button1 = 26
button2 = 19
button3 = 13
button4 = 21
button5 = 20
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
order_all=[['g','c','b'],['a','c','b'],['민철','영신']]
global order_sum
order_sum=sum(order_all,[])
global cnt_all
cnt_all=[['1','2','3'],['1','4','5'],['1','2']]
global cnt_sum
cnt_sum=sum(cnt_all,[])
    
GPIO.setmode(GPIO.BCM)

GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)




serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)


    
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
    global cnt_sum
    font2 =ImageFont.truetype("/fonts/trutype/nanum/NanumBarunGothic.ttf",11)
    font =ImageFont.truetype("/fonts/trutype/nanum/NanumBarunGothic.ttf",14)
    draw.rectangle((0,15,127,63), outline="white", fill="black")
    draw.text((38,0),"주문목록", font=font, fill='white')
    if index <3 :
        for i in range(len(menustr)): 
            if( i == index):
                menuindex = i
                invert(draw, 2, (i*15)+15, menustr[i])
                invert(draw, 62, (i*15)+15, str(cnt_sum[i]))
            else:
                draw.text((2, (i*15)+15), menustr[i], font=font, fill=255)
                draw.text((62, (i*15)+15), str(cnt_sum[i]), font=font, fill=255)
    else:
        for i in range(index-2,index+1):
            if (i == index):
                menuindex = i
                invert(draw, 2, ((i-(index-2))*15+15), menustr[i])
                invert(draw, 62, ((i-(index-2))*15+15), str(cnt_sum[i]))
            elif (i==len(menustr)):
                pass
            else:
                draw.text((2, ((i-(index-2))*15)+15), menustr[i], font=font, fill=255)
                draw.text((62, ((i-(index-2))*15)+15), str(cnt_sum[i]), font=font, fill=255)
                
def rotary_callback1(channel):  
    global menuindex
    global order_list
    global order_menu
    global order_sum
    global flg
    try:
        if flg==0:
            menuindex -= 1
            with canvas(device) as draw:
                menu2(device, draw, order_sum,menuindex%len(order_sum))
        else:
            pass
    finally:
        print("Ending")
        
def rotary_callback2(channel):
    global menuindex
    global order_list
    global order_menu
    global order_sum
    try:
        if flg==0:
            menuindex += 1
            with canvas(device) as draw:
                menu2(device, draw, order_sum,menuindex%len(order_sum))
        else:
            pass
    finally:
        print("Ending")
    
        
def recv(sock):
    global flg
    global order_list
    global order_cnt
    global order_menu
    global order_all
    global order_sum
    global cnt_sum
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
            elif recv.decode('utf-8')=='주문취소':
                with canvas(device) as draw:
                    draw.rectangle(device.bounding_box, outline="white", fill="black")
                    draw.text((43, 20), "주문이",font=font, fill="white")
                    draw.text((15, 35), "취소되었습니다", font=font,fill="white")
                flg=1
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
                cnt_sum=sum(cnt_all,[])
                order_all.append(order_menu)
                order_sum=sum(order_all,[])
                with canvas(device) as draw:
                    menu2(device, draw, order_sum,0)
                print(order_all)
    except:
        pass
    
    
def sdcallback(channel):    
    global flg
    global order_list
    global order_menu
    global order_all
    global cnt_all
    global cnt_sum
    global order_sum
    font =ImageFont.truetype("/fonts/trutype/nanum/NanumBarunGothic.ttf",15)
    try:
        if flg==0:
            print('send')
            with canvas(device) as draw:
                draw.text((5,25), '주문완료 되었습니다.', font=font, fill=255)        
            mp3(orderconfirmmp3)
            sock.send('주문완료'.encode('utf-8'))
            order_list=[]
            flg=1
            print(flg)
        elif flg==1:
            print('hi')
            with canvas(device) as draw:
                menu2(device,draw,order_sum,0)
            flg =0
    except:
        pass
    
def sdcallback2(channel):
    global flg
    global order_list
    global order_menu
    global order_all
    global cnt_all
    global cnt_sum
    global order_sum
    font =ImageFont.truetype("/fonts/trutype/nanum/NanumBarunGothic.ttf",15)
    try:
        if flg==0:
            with canvas(device) as draw:
                    draw.text((5,25), '제품출고 되었습니다.', font=font, fill=255)
                mp3(productout)
                sock.send('제품출고'.encode('utf-8'))
            order_all.pop(0)
            order_sum=sum(order_all,[])
            cnt_all.pop(0)
            cnt_sum=sum(cnt_all,[])
            flg=2
            print(flg)
        elif flg==2:
            with canvas(device) as draw:
                menu2(device,draw,order_sum,0)
            flg=0
    except:
        pass
        

                
GPIO.add_event_detect(button4,GPIO.RISING, callback=sdcallback2, bouncetime=250)  
GPIO.add_event_detect(button3,GPIO.RISING, callback=sdcallback, bouncetime=250)    
GPIO.add_event_detect(button1,GPIO.RISING, callback=rotary_callback1, bouncetime=250)
GPIO.add_event_detect(button2,GPIO.RISING, callback=rotary_callback2, bouncetime=250)


try:
    font1 =ImageFont.truetype("/fonts/trutype/nanum/NanumBarunGothic.ttf",14)
    with canvas(device) as draw:
        menu2(device,draw,order_sum,0)
    
    receiver=Thread(target=recv,args=(sock,))
    receiver.daemon = True
    receiver.start()
    
except KeyboardInterrupt:
    GPIO.clear()
