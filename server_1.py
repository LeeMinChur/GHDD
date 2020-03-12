#-*- coding: utf-8 -*-
import socket
import sys
import time
import threading
import Adafruit_SSD1306
import RPi.GPIO as GPIO
from PIL import Image, ImageDraw, ImageFont


HOST = ''
PORT = 8888
def handle_client(client_socket,addr):
    print("주소" , addr)
    user = client_socket.recv(1024)
    string = "id: %s" % user.decode()
    client_socket.sendall(string.encode())
def eccept_func():
    global server_socket

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt
    


disp.begin()

disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1',(width,height))

draw=ImageDraw.Draw(image)

draw.rectangle((0,0,width,height), outline=0,fill=0)

padding = -2
top = padding
bottom = height-padding

x=0

font = ImageFont.load_default()
button1=14
button2=15
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

print('socket created')
order_flag = 0;
try:
    s.bind((HOST,PORT))
except socket.error:
    print('bind failed')
s.listen(10)
print('wait')
(conn,addr) = s.accept()
print("connected")
while True:
    image = Image.new('1',(width,height))
    draw=ImageDraw.Draw(image)
    data = conn.recv(1024)
    print('recevied : ' + data)
    if data == '주문완료':
        draw.text((x,top), 'order', font=font, fill=255)
        order_flag = 1
    elif data == '주문취소':
        draw.text((x,top), 'cancel', font=font, fill=255)
        order_flage = 0
    disp.image(image)
    disp.display()
    time.sleep(0.2)
conn.close()
