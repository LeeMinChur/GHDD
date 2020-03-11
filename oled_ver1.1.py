#-*-coding:utf-8-*-

import time
import Adafruit_SSD1306
import RPi.GPIO as GPIO
from PIL import Image, ImageDraw, ImageFont

disp = Adafruit_SSD1306.SSD1306_128_64(rst=None, i2c_address=0x3C)

disp.begin()


#화면 클리어
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1',(width, height))
draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width,height), outline = 0, fill=0)

padding = -2
top = padding
button1 = 18
x = 0

font = ImageFont.load_default()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(button1)==GPIO.HIGH:
         draw.text((x,top), 'hello', font=font, fill=255)



    disp.image(image)
    disp.display()

    time.sleep(2)
