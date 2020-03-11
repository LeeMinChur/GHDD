#-*-coding:utf-8-*-

import time
import Adafruit_SSD1306
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
bottom = height-padding
x = 0

font = ImageFont.load_default()

while True:

    draw.text((x,top), 'hello', font=font, fill=255)


    disp.image(image)
    disp.display()

    time.sleep(2)
