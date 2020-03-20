#-*- coding: utf-8 -*-
import threading
import argparse
import pygame
import socket
import RPi.GPIO as GPIO
import time
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
import sys


ordermp3="order.mp3"
ordercancelmp3="ordercancel.mp3"
orderacceptmp3="orderaccept.mp3"
freq=24000
bitsize=-16
channels=1
sbuffer=2048
def mp3(source):
    pygame.mixer.init(freq,bitsize,channels,sbuffer)
    pygame.mixer.music.load(source)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play()
HOST = '192.168.0.133'
PORT = 8888
btn_1=26
btn_2=19
btn_3=13
btn_4=21
btn_5=20
btn_ok=16
btn_can=15

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

menu=['coffee','hamburger','hotdog','donut','pizza']
choice_menu=[]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn_ok,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_can,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_3,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_5,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
disp=Adafruit_SSD1306.SSD1306_128_64(rst=None, i2c_address=0x3C)
def bt1Interrupt(channel):
    global choice_menu
    global menu
    choice_menu.append(menu[0])
def bt2Interrupt(channel):
   global choice_menu
   global menu
   choice_menu.append(menu[1])
def bt3Interrupt(channel):
   global choice_menu
   global menu
   choice_menu.append(menu[2]) 
def bt4Interrupt(channel):
   global choice_menu
   global menu
   choice_menu.append(menu[3])
def bt5Interrupt(channel):
   global choice_menu
   global menu
   choice_menu.append(menu[4])


disp.begin()

disp.clear()
disp.display()

width=disp.width
height=disp.height
image=Image.new('1',(width,height))
draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width,height), outline = 0, fill=0)
padding=0
top= padding
bottom = height-padding

x=0

font =ImageFont.truetype("/fonts/trutype/nanum/NanumBarunGothic.ttf",11)
font2 =ImageFont.truetype("/fonts/trutype/nanum/NanumBarunGothic.ttf",10)
font3 =ImageFont.load_default()

GPIO.add_event_detect(btn_1, GPIO.RISING, callback=bt1Interrupt,bouncetime=200)
GPIO.add_event_detect(btn_2, GPIO.RISING, callback=bt2Interrupt,bouncetime=200)
GPIO.add_event_detect(btn_3, GPIO.RISING, callback=bt3Interrupt,bouncetime=200)
GPIO.add_event_detect(btn_4, GPIO.RISING, callback=bt4Interrupt,bouncetime=200)
GPIO.add_event_detect(btn_5, GPIO.RISING, callback=bt5Interrupt,bouncetime=200)
s.connect((HOST,PORT))
def order(sock):
    global choice_menu
    global menu
    while True:
        try:
            image=Image.new('1',(width,height))
            draw = ImageDraw.Draw(image)
            disp.clear()
            draw.text((x+28,top+24), '주문하시겠습니까?', font=font, fill=255)
            draw.text((x+50,top+40), '6.확인',font=font, fill=255)
            disp.image(image)
            disp.display()
            if GPIO.input(btn_ok) == GPIO.HIGH:
                choice_menu=[]
                while True:
                    image=Image.new('1',(width,height))
                    draw = ImageDraw.Draw(image)
                    disp.clear()
                    draw.text((x+26,top), '메뉴를 선택하세요', font=font, fill=255)
                    for i in range(len(menu)):                    
                        draw.text((x,top+((i+1)*8)+2),'{}.{}'.format((i+1),(menu[i])),font=font3,fill=255)
                    draw.text((x+34,top+52), '6.확인 7.취소',font=font2, fill=255)
                    disp.image(image)
                    disp.display()
                    time.sleep(2)
                    if GPIO.input(btn_ok) == GPIO.HIGH:
                        if len(choice_menu)>5:
                            image=Image.new('1',(width,height))
                            draw = ImageDraw.Draw(image)
                            disp.clear()
                            draw.text((x+40,top+24),'5개 까지만',font=font,fill=255)
                            draw.text((x+24,top+40),'주문할 수 있습니다',font=font,fill=255)
                            disp.image(image)
                            disp.display()
                            time.sleep(2)
                            choice_menu=[]
                        else:
                            while True:
                                image=Image.new('1',(width,height))
                                draw = ImageDraw.Draw(image)
                                disp.clear()
                                draw.text((x+38,top),'주문 확인',font=font,fill=255)
                                for i in range(len(choice_menu)):
                                    draw.text((x,top+((i+1)*8)+2),'{}'.format(choice_menu[i]),font=font3,fill=255)
                                draw.text((x+34,top+52),'6.확인 7.취소',font=font2,fill=255)
                                disp.image(image)
                                disp.display()
                                time.sleep(5)
                                
                                if GPIO.input(btn_ok) == GPIO.HIGH:
                                    for i in choice_menu:
                                        sock.sendall(i.encode('utf-8'))
                                        time.sleep(0.1)
                                    sock.send('주문접수'.encode('utf-8'))
                                    image=Image.new('1',(width,height))
                                    draw = ImageDraw.Draw(image)
                                    disp.clear()
                                    draw.text((x+40,top+32),'주문완료',font=font,fill=255)
                                    disp.image(image)
                                    disp.display()
                                    mp3(ordermp3)
                                    time.sleep(2)
                                    choice_menu=[]
                                    ordercheck(s)      
                                    break
                                
                                elif GPIO.input(btn_can) == GPIO.HIGH:
                                    image=Image.new('1',(width,height))
                                    draw = ImageDraw.Draw(image)
                                    disp.clear()
                                    draw.text((x+30,top+24),'처음화면으로',font=font,fill=255)
                                    draw.text((x+36,top+40),'돌아갑니다',font=font,fill=255)
                                    disp.image(image)
                                    disp.display()
                                    time.sleep(2)
                                    choice_menu=[]
                                    break
                                else:
                                    continue
                            break   
                                   
                    elif GPIO.input(btn_can) == GPIO.HIGH:
                        image=Image.new('1',(width,height))
                        draw = ImageDraw.Draw(image)
                        disp.clear()
                        draw.text((x+30,top+24),'처음화면으로',font=font,fill=255)
                        draw.text((x+36,top+40),'돌아갑니다',font=font,fill=255)
                        disp.image(image)
                        disp.display()
                        time.sleep(2)
                        choice_menu=[]
                        break                
                time.sleep(2)
        except:
            pass
    
def ordercheck(sock):
    try:
        while True:
            time.sleep(0.1)
            recv=sock.recv(1024)
            if recv.decode('utf-8')=='주문완료':
                image=Image.new('1',(width,height))
                draw = ImageDraw.Draw(image)
                disp.clear()
                draw.text((x+34,top+32),'주문접수완료',font=font,fill=255)
                disp.image(image)
                disp.display()
                mp3(ordermp3)
                time.sleep(2)
                break
    except:
        pass
def setting(sock):
    global menu
    try:
        while True:
            time.sleep(0.1)
            recv=sock.recv(1024)
            if recv.decode('utf-8')=='메뉴세팅':
                image=Image.new('1',(width,height))
                draw = ImageDraw.Draw(image)
                disp.clear()
                draw.text((x+34,top+32),'메뉴가 변경됩니다 다시 주문해주세요',font=font,fill=255)
                disp.image(image)
                disp.display()
                time.sleep(2)
                break
                
    except:
        pass
    
while True:
    try:
        order_customer=threading.Thread(target=order,args=(s,))
        order_complete=threading.Thread(target=ordercheck,args=(s,))
        menu_setting=threading.Thread(target=setting,args=(s,))
        order_customer.start()
        order_complete.start()
        menu_setting.start()
        order_customer.join()
        order_complete.join()
        menu_setting.join()
        time.sleep(0.5)
        
    except KeyboardInterrupt as e:
        print(e)
        s.close()
        GPIO.remove_event_detect(btn_1)
        GPIO.remove_event_detect(btn_2)
        GPIO.remove_event_detect(btn_3)
        GPIO.remove_event_detect(btn_4)
        GPIO.remove_event_detect(btn_5)
        GPIO.cleanup()
        break







