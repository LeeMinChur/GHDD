import socket
import socketserver
import time
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
import RPi.GPIO as GPIO

HOST = ''
PORT=8888
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)


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
button3 = 18
button2 = 23
button1 = 24
x = 0

font = ImageFont.load_default()
GPIO.setwarnings(False)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
print ('Socket created')

try:
    s.bind((HOST,PORT))
except socket.error:
    print('Bind failed')

s.listen(5)
print ('Socket awaiting messages')
conn,addr = s.accept()
order_list=[]
print ('Connected')


while True:
    recv=conn.recv(1024)
    if recv.decode('utf-8') =='주문접수':
        break
    else:
        order_list.append(recv.decode('utf-8'))
        conn.send('order complete'.encode('utf-8'))
        #print(list_test)


        
while True:
    image = Image.new('1',(width, height))
    draw = ImageDraw.Draw(image)
    disp.clear()
    draw.text((x+29,top),'Order List',font=font, fill=255)
    for i in range(len(order_list)):
        draw.text((x,top+8*(i+1)), '{}'.format(order_list[i]), font=font, fill=255)
    draw.text((x,top+56),'1.OK 2.Cancel 3.Bye',font=font, fill=255)

    if GPIO.input(button1)==GPIO.HIGH:
        image = Image.new('1',(width, height))
        draw = ImageDraw.Draw(image)
        disp.clear()
        draw.text((x+29,top+25), 'OK', font=font, fill=255)
    if GPIO.input(button2)==GPIO.HIGH:
        break
    if GPIO.input(button3)==GPIO.HIGH:
        break
    disp.image(image)
    disp.display()
    time.sleep(2)
    
conn.close()

