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
btn_next=20
btn_prev=16
btn_ok=15
btn_can=22


menu=['햄버거','피자','콜라','사이다','치킨','소주','맥주','막창']
menu_cnt=[0,0,0,0,0,0,0,0]
menu_page=int(((len(menu)-1)/4)+1)
choice_menu=[]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn_ok,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_prev,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_3,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_next,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_can,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
disp=Adafruit_SSD1306.SSD1306_128_64(rst=None, i2c_address=0x3C)
flg=0
def bt1Interrupt(channel):
    global choice_menu
    global menu
    global menu_cnt
    global sock
    if flg == 0:
        choice_menu.append(menu[0])
        menu_cnt[0] +=1
       
        print(choice_menu)
    elif flg == 1:
        choice_menu.append(menu[4])
        menu_cnt[4] +=1
      
        print(choice_menu)
    else:
        pass
def bt2Interrupt(channel):
   global choice_menu
   global menu
   global menu_cnt
   if flg == 0:
        choice_menu.append(menu[1])
        menu_cnt[1] +=1
      
        print(choice_menu)
   elif flg == 1:
        choice_menu.append(menu[5])
        menu_cnt[5] +=1
    
        print(choice_menu)
   else:
        pass
def bt3Interrupt(channel):
   global choice_menu
   global menu
   global menu_cnt
   if flg == 0:
        choice_menu.append(menu[2])
        menu_cnt[2] +=1
        
        print(choice_menu)
   elif flg == 1:
        choice_menu.append(menu[6])
        menu_cnt[6] +=1
        
        print(choice_menu)
   else:
        pass
def bt4Interrupt(channel):
   global choice_menu
   global menu
   global menu_cnt
   if flg == 0:
        choice_menu.append(menu[3])
        menu_cnt[3] +=1
        
        print(choice_menu)
   elif flg == 1:
        choice_menu.append(menu[7])
        menu_cnt[7] +=1
       
        print(choice_menu)
   else:
        pass



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
#GPIO.add_event_detect(btn_next, GPIO.RISING, callback=bt5Interrupt,bouncetime=200)
lock = Lock()
def order(sock):
    global choice_menu
    global menu
    global flg
    global menu_page
    global menu_cnt

    while True:
        try:
            image=Image.new('1',(width,height))
            draw = ImageDraw.Draw(image)
            disp.clear()
            draw.text((x+28,top+24), '주문하시겠습니까?', font=font, fill=255)
            draw.text((x+50,top+40), '7.확인',font=font, fill=255)
            disp.image(image)
            disp.display()
            if GPIO.input(btn_ok) == GPIO.HIGH:
                choice_menu=[]
                while True:
                    exitOuterLoop = False
                    image=Image.new('1',(width,height))
                    draw = ImageDraw.Draw(image)
                    disp.clear()
                    draw.text((x+26,top-1), '메뉴를 선택하세요', font=font, fill=255)
                    for i in range(int(len(menu)/menu_page)):                    
                        draw.text((x,top+((i+1)*10)+2),'{}.{}'.format((i+1),(menu[i])),font=font2,fill=255)
                    draw.text((x+24,top+52), '5.다음 7.확인 8.취소',font=font2, fill=255)
                    disp.image(image)
                    disp.display()
                    if GPIO.input(btn_next) == GPIO.HIGH:
                        while not exitOuterLoop:
                            flg = 1
                            image=Image.new('1',(width,height))
                            draw = ImageDraw.Draw(image)
                            disp.clear()
                            draw.text((x+26,top), '메뉴를 선택하세요', font=font, fill=255)
                            for i in range(int(len(menu)/menu_page)):                    
                                draw.text((x,top+((i+1)*10)+2),'{}.{}'.format((i+1),(menu[i+4])),font=font2,fill=255)
                            draw.text((x+24,top+52), '6.이전 7.확인 8.취소',font=font2, fill=255)
                            disp.image(image)
                            disp.display()
                            time.sleep(2)
                            if GPIO.input(btn_ok) == GPIO.HIGH:
                                while not exitOuterLoop:
                                    image=Image.new('1',(width,height))
                                    draw = ImageDraw.Draw(image)
                                    disp.clear()
                                    draw.text((x+38,top),'주문 확인',font=font,fill=255)
                                    for i in range(int(len(menu)/menu_page)):
                                        draw.text((x,top+((i+1)*10)+2),'{}'.format(menu[i]),font=font2,fill=255)
                                        draw.text((x+50,top+((i+1)*10)+2),'{}'.format(menu_cnt[i]),font=font2,fill=255)
                                    draw.text((x+24,top+52),'5.다음 7.확인 8.취소',font=font2,fill=255)
                                    disp.image(image)
                                    disp.display()
                                    time.sleep(2)
                                    if GPIO.input(btn_next) == GPIO.HIGH:
                                        while not exitOuterLoop:
                                            image=Image.new('1',(width,height))
                                            draw = ImageDraw.Draw(image)
                                            disp.clear()
                                            draw.text((x+38,top),'주문 확인',font=font,fill=255)
                                            for i in range(int(len(menu)/menu_page)):
                                                draw.text((x,top+((i+1)*10)+2),'{}'.format(menu[i+4]),font=font2,fill=255)
                                                draw.text((x+50,top+((i+1)*10)+2),'{}'.format(menu_cnt[i+4]),font=font2,fill=255)
                                            draw.text((x+24,top+52),'6.이전 7.확인 8.취소',font=font2,fill=255)
                                            disp.image(image)
                                            disp.display()
                                            time.sleep(2)
                                            if GPIO.input(btn_prev) == GPIO.HIGH:
                                                break
                                            elif GPIO.input(btn_ok) == GPIO.HIGH:
            
                                                order_list=','.join(choice_menu)
                                                sock.send(order_list.encode('utf-8'))
                                                image=Image.new('1',(width,height))
                                                draw = ImageDraw.Draw(image)
                                                disp.clear()
                                                draw.text((x+40,top+32),'주문완료',font=font,fill=255)
                                                disp.image(image)
                                                disp.display()
                                                time.sleep(2)
                                                choice_menu=[]
                                                menu_cnt=[0,0,0,0,0,0,0,0]
                                                exitOuterLoop= True
                                                while True:
                                                    time.sleep(0.1)
                                                    recv=sock.recv(1024)
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
                                        
                                    elif GPIO.input(btn_ok) == GPIO.HIGH:
                                        
                                        order_list=','.join(choice_menu)
                                        sock.send(order_list.encode('utf-8'))
                                        image=Image.new('1',(width,height))
                                        draw = ImageDraw.Draw(image)
                                        disp.clear()
                                        draw.text((x+40,top+32),'주문완료',font=font,fill=255)
                                        disp.image(image)
                                        disp.display()
                                        time.sleep(2)
                                        choice_menu=[]
                                        menu_cnt=[0,0,0,0,0,0,0,0]
                                        exitOuterLoop=True
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
                                if exitOuterLoop:
                                    break
                                
                            elif GPIO.input(btn_prev) == GPIO.HIGH:
                                flg -= 1
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
                    elif GPIO.input(btn_ok) == GPIO.HIGH:
                        while not exitOuterLoop:
                            image=Image.new('1',(width,height))
                            draw = ImageDraw.Draw(image)
                            disp.clear()
                            draw.text((x+38,top),'주문 확인',font=font,fill=255)
                            for i in range(int(len(menu)/menu_page)):
                                draw.text((x,top+((i+1)*10)+2),'{}'.format(menu[i]),font=font2,fill=255)
                                draw.text((x+50,top+((i+1)*10)+2),'{}'.format(menu_cnt[i]),font=font2,fill=255)
                            draw.text((x+24,top+52),'5.다음 7.확인 8.취소',font=font2,fill=255)
                            disp.image(image)
                            disp.display()
                            time.sleep(2)
                            if GPIO.input(btn_next) == GPIO.HIGH:
                                while not exitOuterLoop:
                                    image=Image.new('1',(width,height))
                                    draw = ImageDraw.Draw(image)
                                    disp.clear()
                                    draw.text((x+38,top),'주문 확인',font=font,fill=255)
                                    for i in range(int(len(menu)/menu_page)):
                                        draw.text((x,top+((i+1)*10)+2),'{}'.format(menu[i+4]),font=font2,fill=255)
                                        draw.text((x+50,top+((i+1)*10)+2),'{}'.format(menu_cnt[i+4]),font=font2,fill=255)
                                    draw.text((x+24,top+52),'6.이전 7.확인 8.취소',font=font2,fill=255)
                                    disp.image(image)
                                    disp.display()
                                    time.sleep(2)
                                    if GPIO.input(btn_prev) == GPIO.HIGH:
                                        break
                                    elif GPIO.input(btn_ok) == GPIO.HIGH:
                                        
                                        order_list=','.join(choice_menu)
                                        sock.send(order_list.encode('utf-8'))
                                        image=Image.new('1',(width,height))
                                        draw = ImageDraw.Draw(image)
                                        disp.clear()
                                        draw.text((x+40,top+32),'주문완료',font=font,fill=255)
                                        disp.image(image)
                                        disp.display()
                                        time.sleep(2)
                                        choice_menu=[]
                                        menu_cnt=[0,0,0,0,0,0,0,0]
                                        exitOuterLoop = True
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
                            
                                        
                            elif GPIO.input(btn_ok) == GPIO.HIGH:
                                
                                order_list=','.join(choice_menu)
                                sock.send(order_list.encode('utf-8'))
                                image=Image.new('1',(width,height))
                                draw = ImageDraw.Draw(image)
                                disp.clear()
                                draw.text((x+40,top+32),'주문완료',font=font,fill=255)
                                disp.image(image)
                                disp.display()
                                time.sleep(2)
                                choice_menu=[]
                                menu_cnt=[0,0,0,0,0,0,0,0]
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
        except:
            pass

time.sleep(2)
        


def setting(sock):
    global choice_menu
    global menu
    global menu_cnt

    try:
        while True:
            exitOutLoop = False
            time.sleep(0.1)
            recv=sock.recv(1024)
            print('1')
            print(recv.decode())
            if recv.decode('utf-8')=='메뉴세팅':
                while not exitOutLoop:
                    image=Image.new('1',(width,height))
                    draw = ImageDraw.Draw(image)
                    disp.clear()
                    draw.text((x+28,top+24),'메뉴가 변경됩니다',font=font,fill=255)
                    draw.text((x+50,top+40),'7. OK ',font=font,fill=255)
                    disp.image(image)
                    disp.display()
                        
                
                    if GPIO.input(btn_ok) == GPIO.HIGH:
                        menu = []
                        menu_cnt=[0,0,0,0]
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
                                time.sleep(2)
                                print(menu)
                                exitOutLoop = True
                                break
                            else:
                                menu=list(recv.decode('utf-8').split(','))
                                print(menu)

                    else:
                        continue
                   
    except:
        pass

def run():
    global t1
    global sock

    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            t=Thread(target=setting,args=(sock,))
            t1=Thread(target=order, args=(sock,))
   
            sock.connect((HOST,PORT))
            
            
            t.daemon = True
            
            
            t.start()
            t1.start()
            
            
            
                      
            
            
            while True:
                time.sleep(1)
                


    except Exception as e:
        print('run Err: %s' %e)
        pass
    
run()
