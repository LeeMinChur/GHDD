#-*- coding: utf-8 -*-
from threading import Thread, Lock
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
HOST = '192.168.0.2'
PORT = 9988
btn_1=26
btn_2=19
btn_3=13
btn_4=21
btn_5=20
btn_ok=16
btn_can=15

menu_cnt=[0,0,0,0]
menu=['햄버거','피자','콜라','사이다']
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
#GPIO.add_event_detect(btn_5, GPIO.RISING, callback=bt5Interrupt,bouncetime=200)
lock = Lock()
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
            time.sleep(2)
            if GPIO.input(btn_ok) == GPIO.HIGH:
                choice_menu=[]
                while True:
                    image=Image.new('1',(width,height))
                    draw = ImageDraw.Draw(image)
                    disp.clear()
                    draw.text((x+26,top), '메뉴를 선택하세요', font=font, fill=255)
                    for i in range(len(menu)):                    
                        draw.text((x,top+((i+1)*10)+2),'{}.{}'.format((i+1),(menu[i])),font=font2,fill=255)
                    draw.text((x+34,top+52), '6.확인 7.취소',font=font2, fill=255)
                    disp.image(image)
                    disp.display()
                    time.sleep(2)
                    if GPIO.input(btn_ok) == GPIO.HIGH:
                        while True:
                            image=Image.new('1',(width,height))
                            draw = ImageDraw.Draw(image)
                            disp.clear()
                            draw.text((x+38,top),'주문 확인',font=font,fill=255)
                            for i in range(len(choice_menu)):
                                draw.text((x,top+((i+1)*10)+2),'{}'.format(choice_menu[i]),font=font2,fill=255)
                            draw.text((x+34,top+52),'6.확인 7.취소',font=font2,fill=255)
                            disp.image(image)
                            disp.display()
                            time.sleep(5)
                            
                            if GPIO.input(btn_ok) == GPIO.HIGH:
                                order_list=','.join(choice_menu)
                                sock.send(order_list.encode('utf-8'))
                                
                                time.sleep(1)
                                
                                image=Image.new('1',(width,height))
                                draw = ImageDraw.Draw(image)
                                disp.clear()
                                draw.text((x+40,top+32),'주문완료',font=font,fill=255)
                                disp.image(image)
                                disp.display()
                    
                                while True:
                                    time.sleep(0.1)
                                    recv=sock.recv(1024)
                                    #print(recv.decode('utf-8'))
                                    if recv.decode('utf-8')=='주문완료':
                                        print(recv.decode('utf-8'))
                                        image=Image.new('1',(width,height))
                                        draw = ImageDraw.Draw(image)
                                        disp.clear()
                                        draw.text((x+34,top+32),'주문접수완료',font=font,fill=255)
                                        disp.image(image)
                                        disp.display()
                                        mp3(ordermp3)
                                        time.sleep(2)
                                        choice_menu=[]  
                                        break
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
            
            time.sleep(2)
        except:
            pass

    
def setting(sock):
    global choice_menu
    global menu
    try:
        while True:
            exitOutLoop = False
            time.sleep(0.1)
            recv=sock.recv(1024)
            print(recv.decode())
            if recv.decode('utf-8')=='메뉴세팅':
                menu = []
                lock.acquire()
                while True:
                    image=Image.new('1',(width,height))
                    draw = ImageDraw.Draw(image)
                    disp.clear()
                    draw.text((x+28,top+24),'메뉴가 변경됩니다',font=font,fill=255)
                    draw.text((x+50,top+40),'6. OK ',font=font,fill=255)
                    disp.image(image)
                    disp.display()
                    if GPIO.input(btn_ok) == GPIO.HIGH:
                        sock.send('세팅수락'.encode('utf-8'))
                        while True:
                            time.sleep(0.1)
                            recv=sock.recv(1024)
                            print(recv.decode('utf-8'))
                            sock.send(recv)
                            if recv.decode('utf-8') == '세팅완료':
                                image=Image.new('1',(width,height))
                                draw = ImageDraw.Draw(image)
                                disp.clear()
                                draw.text((x+24,top+24),'메뉴가 변경되었습니다',font=font,fill=255)
                                draw.text((x+28,top+40),'다시 주문해주세요',font=font,fill=255)
                                disp.image(image)
                                disp.display()
                                choice_menu=[]
                                print(menu)
                                lock.release()
                                exitOutLoop = True
                                break
                            else:
                                menu=list(recv.decode('utf-8').split(','))
                                print(menu)
                    elif exitOutLoop:
                        break
            else:
                pass
                
    except:
        pass

def run():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST,PORT))
            t=Thread(target=setting,args=(sock,))
            t1=Thread(target=order, args=(sock,))
            t.daemon = True
            t1.daemon = True
            
            
            t.start()
            t1.start()     
                        
            while True:
                time.sleep(1)
                


    except Exception as e:
        print('run Err: %s' %e)
        pass
    
run()

        






