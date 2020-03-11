#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont



button_1=15
button_2=16
button_ok=20
button_can=21

menu=['coffee','hamburger']
choice_menu=[]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_ok,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_can,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
disp=Adafruit_SSD1306.SSD1306_128_64(rst=None, i2c_address=0x3C)
def bt1Interrupt(channel):
    global choice_menu
    global menu
    choice_menu.append(menu[0])
def bt2Interrupt(channel):
   global choice_menu
   global menu
   choice_menu.append(menu[1])

def okInterrupt(channel):
    global choice_menu
    image=Image.new('1',(width,height))
    draw = ImageDraw.Draw(image)
    disp.clear()
    print(choice_menu)
    for i in range(len(choice_menu)+1):
        if i-len(choice_menu)==0:
            draw.text((x,top+(i*8)),'order complete',font=font,fill=255)
        else:
            draw.text((x,top+(i*8)),'{}.{}'.format((i+1),(choice_menu[i])),font=font,fill=255)
    disp.image(image)
    disp.display()
    time.sleep(2)   
    choice_menu=[]
def canInterrupt(channel):    
    global choice_menu
    image=Image.new('1',(width,height))
    draw = ImageDraw.Draw(image)
    disp.clear()
    draw.text((x,top), 'order canceled',font=font,fill=255)
    disp.image(image)
    disp.display()
    choice_menu=[]

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

GPIO.add_event_detect(15, GPIO.RISING, callback=bt1Interrupt,bouncetime=200)
GPIO.add_event_detect(16, GPIO.RISING, callback=bt2Interrupt,bouncetime=200)
GPIO.add_event_detect(20, GPIO.RISING, callback=okInterrupt,bouncetime=500)
GPIO.add_event_detect(21, GPIO.RISING, callback=canInterrupt,bouncetime=500)
while True:
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
    time.sleep(2)
