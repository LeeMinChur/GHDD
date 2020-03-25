import socket
import threading
import socketserver
import time
import argparse
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
import RPi.GPIO as GPIO
import pygame

HOST = '192.168.0.2'
PORT=9988
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


'''try:
    s.bind((HOST,PORT))
    s.listen(2)
    conn,addr = s.accept()
except socket.error:
    print('Bind failed')
    s.close()'''


print ('Socket awaiting messages')
order_list=[]
        
def mp3(source):
    pygame.mixer.init(freq,bitsize,channels,sbuffer)
    pygame.mixer.music.load(source)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play()

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
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST,PORT))

temp_all = []



def receive(sock):
    while True:
        try: 
            image=Image.new('1',(width,height))
            draw = ImageDraw.Draw(image)
            disp.clear()
            
            draw.text((x+29,top),'order list',font=font, fill=255)
            
            recv=sock.recv(1024)
            print(recv.decode('utf-8'))          
            ovalp=[]
            temp_all = []
            c = []
            s = (2*5)+1
             
            order_list=list(recv.decode('utf-8').split(','))
            
            ovlap =list(set(order_list))
            print(ovlap)
            
            for i in ovlap:
                c.append(order_list.count(str(i)))
                
            for i in range(0,4):
                draw.text((x,top+(s*(i+1))), '{}'.format(ovlap[i]), font=font1, fill=255)
                draw.text((x+40,top+(s*(i+1))), '{}'.format(c[i]), font=font1, fill=255)           
            draw.text((x,top+56),'5.다음페이지',font=font1, fill=255)
                
                
            temp_all.append(order_list)            
            print(temp_all)         
                
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
                    
            if GPIO.input(button5)==GPIO.HIGH:
                break
                
            disp.image(image)
            disp.display()
            time.sleep(0.01)
        except KeyboardInterrupt as e:
            
            s.close()
            sock.close()
            break
def sender1(channel):
    order_list = []
    ovlap = []
    sock.send('주문완료'.encode('utf-8'))

def sender2(channel):
    sock.send('제품출고'.encode('utf-8'))
    
GPIO.add_event_detect(button1,GPIO.RISING, callback=sender1, bouncetime=200)
GPIO.add_event_detect(button2,GPIO.RISING, callback=sender2, bouncetime=200)
def run():
    try:
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as sock:
            sock.connect((HOST,PORT))
            receiver=threading.Thread(target=receive, args=(sock,))
            receiver.start()
            receiver.join()
            while True:
                time.sleep(1)
            
    except Exception as e:
        print('run Err: %s' % e)
        pass
while True:
    try:
        print('hi')
        time.sleep(5)
    except:
        pass

    


#receive(s)
'''temp_all = []      
while True:
    try:        
        print(order_list)
        image = Image.new('1',(width, height))
        draw = ImageDraw.Draw(image)
        disp.clear()
        draw.text((x+29,top),'Order List',font=font, fill=255)
        temp=[]
        for i in range(len(order_list)):
            temp.append(order_list[i])
            draw.text((x,top+8*(i+1)), '{}'.format(order_list[i]), font=font, fill=255)
        temp_all.append(temp)
        draw.text((x,top+56),'1.OK 2.Cancel 3.Bye',font=font, fill=255)
        disp.image(image)
        disp.display()
        time.sleep(2)
        if GPIO.input(button1)==GPIO.HIGH:
            send(s)
            image = Image.new('1',(width, height))
            draw = ImageDraw.Draw(image)
            disp.clear()
            draw.text((x+29,top+25), 'OK', font=font, fill=255)
            mp3(orderconfirmmp3)
            disp.image(image)
            disp.display()
            
        if GPIO.input(button2)==GPIO.HIGH:
            image = Image.new('1',(width, height))
            draw = ImageDraw.Draw(image)
            disp.clear()
            draw.text((x+29,top+25), 'Cancle', font=font, fill=255)
            mp3(orderdeniedmp3)
            disp.image(image)
            disp.display()
            
        if GPIO.input(button3)==GPIO.HIGH:
            image = Image.new('1',(width, height))
            draw = ImageDraw.Draw(image)
            disp.clear()
            draw.text((x+29,top+25), 'Bye', font=font, fill=255)
            disp.image(image)
            disp.display()
            mp3(ordercheckmp3)
            
        if GPIO.input(button4)==GPIO.HIGH:
            image = Image.new('1',(width, height))
            draw = ImageDraw.Draw(image)
            disp.clear()
            for i in range(len(temp_all)):
                draw.text((x,top+8*(i+1)), '{}'.format(temp_all[i]), font=font, fill=255)
            disp.image(image)
            disp.display()
                
        if GPIO.input(button5)==GPIO.HIGH:
            break
            
        disp.image(image)
        disp.display()
        time.sleep(2)
        #thread()
    except KeyboardInterrupt as e:
        print(e)
        s.close()
        conn.close()
        break'''
