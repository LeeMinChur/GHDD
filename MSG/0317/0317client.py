#-*- coding: utf-8 -*-

import socket
from threading import Thread
import RPi.GPIO as GPIO
import time

btnOrder=14
btnCancel=15
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(btnOrder,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btnCancel,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

HOST='192.168.0.13'
PORT=9988

def rcvMsg(sock):
    while True:
        try:
            data=sock.recv(1024)
            if not data:
                break
            if data.decode('utf-8')=='a':
                print('recv: 주문완료')
                time.sleep(1)
            elif data.decode('utf-8')=='b':
                print('recv: 주문취소')
                time.sleep(1)

        except Exception as e:
            print("recv Err: %s" % e)
            pass
def sendMsg(sock):
    try:
        while True:
            if GPIO.input(btnOrder)==GPIO.HIGH:
                sock.send('c'.encode())
                print('send:주문접수')
                time.sleep(1)
            elif GPIO.input(btnCancel)==GPIO.HIGH:
                sock.send('d'.encode())
                print('send: 주문거절')
                time.sleep(1)
            else:
                pass
    except Exception as e:
        print("send Err: %s" %e)
        pass

def run():
    try:

        with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as sock:
            sock.connect((HOST,PORT))
            t=Thread(target=rcvMsg,args=(sock,))
            t1=Thread(target=sendMsg,args=(sock,))
            t1.daemon=True
            t.daemon=True
            t.start()
            t1.start()

            while True:
                time.sleep(1)

    except Exception as e:
        print('run Err: %s' % e)
        pass

run()
