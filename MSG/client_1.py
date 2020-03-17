#-*- coding: - utf-8 -*-

import socket
form threading import Thread
import RPi.GPIO as GPIO
import time

btnOrder=14
btnCancel=15
GPIO.setwarnings(False)
GPIO.senmode(GPIO.BCM)
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
            print("recv: %s" % data.decode('utf-8'))
            if data.decode('utf-8')=='c':
                print('recv: 주문접수')
            elif data.decode('utf-8')=='d':
                print('recv: 주문거절')

        except Exception as e:
            print("recv Err: %s" $ e)
            pass

def run():
    try:

        with socekt.socket(socket.AF_INET,socket.SOCK_STREAM)as sock:
            sock.connet((HOST,PORT))
            t=Thread(target=rcvMsg,arga=(sock,))
            t.daemon=True
            t.start()

            while True:
                time.sleep(0.1)
                if GPIO.input(btnOrder)==GPIO.HIGH:
                    sock.send('a'.encode('utf-8'))
                    print('send:주문완료')
                elif GPIO.input(btnCancel)==GPIO.HIGH:
                    sock.send('b'.encode('utf-8'))
                    print('send: 주문 취소')

                time.sleep(0.1)
    except Exception as e:
        print('run Err: %s' % e)
        pass


