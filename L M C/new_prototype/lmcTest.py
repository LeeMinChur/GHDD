import socket
import threading
import socketserver
import time
import argparse
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
import RPi.GPIO as GPIO
import pygame

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

freq=24000
bitsize=-16
channels=1
sbuffer=2048
ordercheckmp3="ordercheck.mp3"
orderconfirmmp3="ordercomfirm.mp3"
orderdeniedmp3="orderdenied.mp3"
ordercancelmp3="ordercancel.mp3"
productout="productout.mp3"

print ('Socket created')




order_list=['민철','민철','민철','영신','윤수','진영','영신','윤수','선규','선규','찬호','찬호','대원','종진','은오']
temp_all=[['민철','민철','민철','영신'],['윤수','진영','영신','윤수','선규'],['선규','찬호','찬호','대원','종진','은오']]
#order_list=['ham','ber',:

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
font1=ImageFont.truetype("/fonts/frutype/nanum/NanumBarunGothic.ttf",10)
GPIO.setwarnings(False)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        
def receive(s):
    global ovlap
    while True:
        try: 
            image=Image.new('1',(width,height))
            draw = ImageDraw.Draw(image)
            disp.clear()
            draw.text((x+29,top),'order list',font=font, fill=255)
            ovlap=[]
            ovlap =list(set(order_list))
            print(ovlap)
            c = []
            for i in ovlap:
                c.append(order_list.count(str(i)))
            #temp_all = []      
            temp=[]
            s = (2*5)+1
                       
            '''for i in range(len(ovlap)):
                temp.append(ovlap[i])             
            temp_all.append(temp)'''
            #print(temp_all[0])
            #print(temp_all)
            
            #print(temp_all)
            
            for i in range(0,4):
                draw.text((x,top+(s*(i+1))), '{}'.format(ovlap[i]), font=font1, fill=255)
                draw.text((x+40,top+(s*(i+1))), '{}'.format(c[i]), font=font1, fill=255)           
            draw.text((x,top+56),'5.다음페이지',font=font1, fill=255)
            
            if GPIO.input(button5)==GPIO.HIGH:
                while True:                
                    s = (2*5)+1
                    image = Image.new('1',(width, height))
                    draw = ImageDraw.Draw(image)
                    disp.clear()
                    ovlap2=[]
                    for i in range(5,len(ovlap)):
                        ovlap2.append(ovlap[i])
                    for i in range(0,4):
                        draw.text((x,top+12+(s*(i))), '{}'.format(ovlap2[i]), font=font1, fill=255)
                        draw.text((x+40,top+(s*(i+1))), '{}'.format(c[i]), font=font1, fill=255) 
                        draw.text((x+29,top),'order list',font=font, fill=255)
                        draw.text((x,top+56),'5.이전단계',font=font1, fill=255)
                    disp.image(image)
                    disp.display()
                    if GPIO.input(button5)==GPIO.HIGH:                        
                        break
            
            if GPIO.input(button3)==GPIO.HIGH:
                time.sleep(1)
                while True:
                    image = Image.new('1',(width, height))
                    draw = ImageDraw.Draw(image)
                    disp.clear()
                    draw.text((x+29,top),'order list',font=font, fill=255)
                    draw.text((x+20,top+29),'1.Client1  2.Clinet2 ',font=font1, fill=255)
                    draw.text((x+20,top+41),'3.Client2  4.Clinet4 ',font=font1, fill=255)
                    disp.image(image)
                    disp.display()               
                    if GPIO.input(button1)==GPIO.HIGH:
                        image = Image.new('1',(width, height))
                        draw = ImageDraw.Draw(image)
                        disp.clear()
                        while True:                            
                            for i in range(len(temp_all[0])):                               
                                draw.text((x,top+12+(s*(i))), '{}'.format(temp_all[0][i]), font=font1, fill=255)                            
                                disp.image(image)
                                disp.display()
                            draw.text((x+40,top+56),'5.이전단계',font=font1, fill=255)
                            if GPIO.input(button5)==GPIO.HIGH:
                                break
                    if GPIO.input(button2)==GPIO.HIGH:
                        image = Image.new('1',(width, height))
                        draw = ImageDraw.Draw(image)
                        disp.clear()
                        while True:                            
                            for i in range(len(temp_all[1])):                               
                                draw.text((x,top+12+(s*(i))), '{}'.format(temp_all[1][i]), font=font1, fill=255)                            
                                disp.image(image)
                                disp.display()
                            draw.text((x+40,top+56),'5.이전단계',font=font1, fill=255)
                            if GPIO.input(button5)==GPIO.HIGH:
                                break
                    if GPIO.input(button3)==GPIO.HIGH:
                        image = Image.new('1',(width, height))
                        draw = ImageDraw.Draw(image)
                        disp.clear()
                        while True:                            
                            for i in range(len(temp_all[2])):                               
                                draw.text((x,top+12+(s*(i))), '{}'.format(temp_all[2][i]), font=font1, fill=255)                            
                                disp.image(image)
                                disp.display()
                            draw.text((x+40,top+56),'5.이전단계',font=font1, fill=255)
                            if GPIO.input(button5)==GPIO.HIGH:
                                break
                    if GPIO.input(button4)==GPIO.HIGH:
                        image = Image.new('1',(width, height))
                        draw = ImageDraw.Draw(image)
                        disp.clear()
                        while True:
                            for i in range(len(temp_all[3])):
                                draw.text((x,top+12+(s*(i))), '{}'.format(temp_all[3][i]), font=font1, fill=255)
                                disp.image(image)
                                disp.display()
                                draw.text((x+40,top+56),'5.이전단계',font=font1, fill=255)
                            if GPIO.input(button5)==GPIO.HIGH:
                                break
                    draw.text((x+40,top+56),'5.이전단계',font=font1, fill=255)       
                if GPIO.input(button5)==GPIO.HIGH:
                    break
                        
            '''if GPIO.input(button2)==GPIO.HIGH:
                sock.send('주문완료'.encode('utf-8'))
                break   
                
            if GPIO.input(button2)==GPIO.HIGH:
                sock.send('주문완료'.encode('utf-8'))
                image = Image.new('1',(width, height))
                draw = ImageDraw.Draw(image)
                disp.clear()
                draw.text((x+29,top+25), '주문완료', font=font, fill=255)
                #mp3(orde료rdeniedmp3)
                disp.image(image)
                disp.display()'''
                    
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
                        
          
                    
            disp.image(image)
            disp.display()
            time.sleep(0.01)
        except KeyboardInterrupt as e:
            
            s.close()
            sock.close()
            break

def run():
    try:
        #sender=threading.Thread(target=send,args=(s,))
        receiver=threading.Thread(target=receive, args=(s,))
        receiver.start()
        #sender.start()
        #sender.join()
        receiver.join()
        while True:
            time.sleep(1)
            
    except Exception as e:
        print('run Err: %s' % e)
        pass
    
    
def sender1(channel):
    global ovlap
    
    order_list = []
    ovlap = []
    print(ovlap)
   
GPIO.add_event_detect(button1,GPIO.RISING, callback=sender1, bouncetime=200)

run()
