#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont



btn_1=26
btn_2=19
btn_3=13
btn_4=21
btn_5=20
btn_ok=16
btn_can=15

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
padding=-2
top= padding
bottom = height-padding

x=0

font =ImageFont.load_default()

GPIO.add_event_detect(btn_1, GPIO.RISING, callback=bt1Interrupt,bouncetime=200)
GPIO.add_event_detect(btn_2, GPIO.RISING, callback=bt2Interrupt,bouncetime=200)
GPIO.add_event_detect(btn_3, GPIO.RISING, callback=bt3Interrupt,bouncetime=200)
GPIO.add_event_detect(btn_4, GPIO.RISING, callback=bt4Interrupt,bouncetime=200)
GPIO.add_event_detect(btn_5, GPIO.RISING, callback=bt5Interrupt,bouncetime=200)

while True:
    image=Image.new('1',(width,height))
    draw = ImageDraw.Draw(image)
    disp.clear()
    draw.text((x,top), 'Choice menu', font=font, fill=255)
    for i in range(len(menu)+2):
        if i-len(menu)==0:
            draw.text((x,top+((i+1)*8)),'{}.ok'.format(i+1),font=font,fill=255)
        elif i-len(menu)==1:
            draw.text((x,top+((i+1)*8)),'{}.cancel'.format(i+1),font=font,fill=255)
        else:
            draw.text((x,top+((i+1)*8)),'{}.{}'.format((i+1),(menu[i])),font=font,fill=255)
    disp.image(image)
    disp.display()
    if GPIO.input(btn_ok) == GPIO.HIGH:
        if len(choice_menu)>6:
            image=Image.new('1',(width,height))
            draw = ImageDraw.Draw(image)
            disp.clear()
            draw.text((x+25,top+24),'Please order',font=font,fill=255)
            draw.text((x+28,top+40),'less than 7',font=font,fill=255)
            disp.image(image)
            disp.display()
            time.sleep(2)
            choice_menu=[]
        else:
            while True:
                image=Image.new('1',(width,height))
                draw = ImageDraw.Draw(image)
                disp.clear()
                print(choice_menu)
                draw.text((x,top),'Order check',font=font,fill=255)
                for i in range(len(choice_menu)+1):
                    if i-len(choice_menu)==0:
                        draw.text((x,top+((i+1)*8)),'1.OK 2.Cancel',font=font,fill=255)
                    else:
                        draw.text((x,top+((i+1)*8)),'{}'.format(choice_menu[i]),font=font,fill=255)
                disp.image(image)
                disp.display()
                time.sleep(2)
                if GPIO.input(btn_1) == GPIO.HIGH:
                    image=Image.new('1',(width,height))
                    draw = ImageDraw.Draw(image)
                    disp.clear()
                    draw.text((x+23,top+32),'Order complete',font=font,fill=255)
                    disp.image(image)
                    disp.display()
                    time.sleep(2)
                    choice_menu=[]
                    break
                elif GPIO.input(btn_2) == GPIO.HIGH:
                    image=Image.new('1',(width,height))
                    draw = ImageDraw.Draw(image)
                    disp.clear()
                    draw.text((x+10,top+32),'Return choice menu',font=font,fill=255)
                    disp.image(image)
                    disp.display()
                    time.sleep(2)
                    choice_menu=[]
                    break
    elif GPIO.input(btn_can) == GPIO.HIGH:
        image=Image.new('1',(width,height))
        draw = ImageDraw.Draw(image)
        disp.clear()
        draw.text((x+10,top+32),'Return choice menu',font=font,fill=255)
        disp.image(image)
        disp.display()
        time.sleep(2)
        choice_menu=[]
                             
                               
    time.sleep(2)
