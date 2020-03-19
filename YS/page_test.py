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
btn_ok=15
btn_6=16


menu=['선규형','민철','진영','윤수','승주','은오','종진','영신']
menu_cnt=[0,0,0,0,0,0,0,0]
menu_page=int(((len(menu)-1)/4)+1)
choice_menu=[]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn_ok,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_6,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_3,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_5,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
disp=Adafruit_SSD1306.SSD1306_128_64(rst=None, i2c_address=0x3C)
flg=0
def bt1Interrupt(channel):
    global choice_menu
    global menu
    global menu_cnt
    if flg == 0:
        choice_menu.append(menu[0])
        menu_cnt[0] +=1
        print(choice_menu)
    elif flg == 1:
        choice_menu.append(menu[4])
        menu_cnt[4] +=1
        print(choice_menu)
    else:
        pass
def bt2Interrupt(channel):
   global choice_menu
   global menu
   global menu_cnt
   if flg == 0:
        choice_menu.append(menu[1])
        menu_cnt[1] +=1
        print(choice_menu)
   elif flg == 1:
        choice_menu.append(menu[5])
        menu_cnt[5] +=1
        print(choice_menu)
   else:
        pass
def bt3Interrupt(channel):
   global choice_menu
   global menu
   global menu_cnt
   if flg == 0:
        choice_menu.append(menu[2])
        menu_cnt[2] +=1
        print(choice_menu)
   elif flg == 1:
        choice_menu.append(menu[6])
        menu_cnt[6] +=1
        print(choice_menu)
   else:
        pass
def bt4Interrupt(channel):
   global choice_menu
   global menu
   global menu_cnt
   if flg == 0:
        choice_menu.append(menu[3])
        menu_cnt[3] +=1
        print(choice_menu)
   elif flg == 1:
        choice_menu.append(menu[7])
        menu_cnt[7] +=1
        print(choice_menu)
   else:
        pass
print(menu_page)
disp.begin()

disp.clear()
disp.display()

width=disp.width
height=disp.height
image=Image.new('1',(width,height))
draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width,height), outline = 0, fill=0)
padding=0
top= padding
bottom = height-padding

x=0

font =ImageFont.truetype("/fonts/trutype/nanum/NanumGothic.ttf",11)
font2 =ImageFont.truetype("/fonts/trutype/nanum/NanumGothic.ttf",10)
font3 =ImageFont.load_default()

GPIO.add_event_detect(btn_1, GPIO.RISING, callback=bt1Interrupt,bouncetime=200)
GPIO.add_event_detect(btn_2, GPIO.RISING, callback=bt2Interrupt,bouncetime=200)
GPIO.add_event_detect(btn_3, GPIO.RISING, callback=bt3Interrupt,bouncetime=200)
GPIO.add_event_detect(btn_4, GPIO.RISING, callback=bt4Interrupt,bouncetime=200)
try:
    while True:
        exitOuterLoop = False
        image=Image.new('1',(width,height))
        draw = ImageDraw.Draw(image)
        disp.clear()
        draw.text((x+26,top-1), '메뉴를 선택하세요', font=font, fill=255)
        for i in range(int(len(menu)/menu_page)):                    
            draw.text((x,top+((i+1)*10)+2),'{}.{}'.format((i+1),(menu[i])),font=font2,fill=255)
        draw.text((x+34,top+52), '5.다음 7.확인',font=font2, fill=255)
        disp.image(image)
        disp.display()
        if GPIO.input(btn_5) == GPIO.HIGH:
            flg += 1
            while True:
                image=Image.new('1',(width,height))
                draw = ImageDraw.Draw(image)
                disp.clear()
                draw.text((x+26,top), '메뉴를 선택하세요', font=font, fill=255)
                for i in range(int(len(menu)/menu_page)):                    
                    draw.text((x,top+((i+1)*10)+2),'{}.{}'.format((i+1),(menu[i+4])),font=font2,fill=255)
                draw.text((x+34,top+52), '6.이전 7.확인',font=font2, fill=255)
                disp.image(image)
                disp.display()
                time.sleep(2)
                print(GPIO.input(btn_ok))
                if GPIO.input(btn_ok) == GPIO.HIGH:
                    while True:
                        image=Image.new('1',(width,height))
                        draw = ImageDraw.Draw(image)
                        disp.clear()
                        draw.text((x+38,top),'주문 확인',font=font,fill=255)
                        for i in range(int(len(menu)/menu_page)):
                            draw.text((x,top+((i+1)*10)+2),'{}'.format(menu[i]),font=font2,fill=255)
                            draw.text((x+40,top+((i+1)*10)+2),'{}'.format(menu_cnt[i]),font=font2,fill=255)
                        draw.text((x+34,top+52),'5.다음 7.확인',font=font2,fill=255)
                        disp.image(image)
                        disp.display()
                        time.sleep(2)
                        if GPIO.input(btn_5) == GPIO.HIGH:
                            while True:
                                image=Image.new('1',(width,height))
                                draw = ImageDraw.Draw(image)
                                disp.clear()
                                draw.text((x+38,top),'주문 확인',font=font,fill=255)
                                for i in range(int(len(menu)/menu_page)):
                                    draw.text((x,top+((i+1)*10)+2),'{}'.format(menu[i+4]),font=font2,fill=255)
                                    draw.text((x+40,top+((i+1)*10)+2),'{}'.format(menu_cnt[i+4]),font=font2,fill=255)
                                draw.text((x+34,top+52),'6.이전 7.확인',font=font2,fill=255)
                                disp.image(image)
                                disp.display()
                                time.sleep(2)
                                if GPIO.input(btn_6) == GPIO.HIGH:
                                    break
                                elif GPIO.input(btn_ok) == GPIO.HIGH:
                                    image=Image.new('1',(width,height))
                                    draw = ImageDraw.Draw(image)
                                    disp.clear()
                                    draw.text((x+40,top+32),'주문완료',font=font,fill=255)
                                    disp.image(image)
                                    disp.display()
                                    time.sleep(2)
                                    choice_menu=[]
                                    menu_cnt=[0,0,0,0,0,0,0,0]
                                    exitOuterLoop = True
                                    break
                            if exitOuterLoop:
                                break
                        elif GPIO.input(btn_ok) == GPIO.HIGH:
                            image=Image.new('1',(width,height))
                            draw = ImageDraw.Draw(image)
                            disp.clear()
                            draw.text((x+40,top+32),'주문완료',font=font,fill=255)
                            disp.image(image)
                            disp.display()
                            time.sleep(2)
                            choice_menu=[]
                            menu_cnt=[0,0,0,0,0,0,0,0]
                            break
                    break
                elif GPIO.input(btn_6) == GPIO.HIGH:
                    flg -=1
                    break
        elif GPIO.input(btn_ok) == GPIO.HIGH:
            while True:
                image=Image.new('1',(width,height))
                draw = ImageDraw.Draw(image)
                disp.clear()
                draw.text((x+38,top),'주문 확인',font=font,fill=255)
                for i in range(int(len(menu)/menu_page)):
                    draw.text((x,top+((i+1)*10)+2),'{}'.format(menu[i]),font=font2,fill=255)
                    draw.text((x+40,top+((i+1)*10)+2),'{}'.format(menu_cnt[i]),font=font2,fill=255)
                draw.text((x+34,top+52),'5.다음 7.확인',font=font2,fill=255)
                disp.image(image)
                disp.display()
                time.sleep(2)
                if GPIO.input(btn_5) == GPIO.HIGH:
                    while True:
                        image=Image.new('1',(width,height))
                        draw = ImageDraw.Draw(image)
                        disp.clear()
                        draw.text((x+38,top),'주문 확인',font=font,fill=255)
                        for i in range(int(len(menu)/menu_page)):
                            draw.text((x,top+((i+1)*10)+2),'{}'.format(menu[i+4]),font=font2,fill=255)
                            draw.text((x+40,top+((i+1)*10)+2),'{}'.format(menu_cnt[i+4]),font=font2,fill=255)
                        draw.text((x+34,top+52),'6.이전 7.확인',font=font2,fill=255)
                        disp.image(image)
                        disp.display()
                        time.sleep(2)
                        if GPIO.input(btn_6) == GPIO.HIGH:
                            break
                        elif GPIO.input(btn_ok) == GPIO.HIGH:
                            image=Image.new('1',(width,height))
                            draw = ImageDraw.Draw(image)
                            disp.clear()
                            draw.text((x+40,top+32),'주문완료',font=font,fill=255)
                            disp.image(image)
                            disp.display()
                            time.sleep(2)
                            choice_menu=[]
                            menu_cnt=[0,0,0,0,0,0,0,0]
                            exitOuterLoop = True
                            break
                    if exitOuterLoop:
                        break
                            
                elif GPIO.input(btn_ok) == GPIO.HIGH:
                    image=Image.new('1',(width,height))
                    draw = ImageDraw.Draw(image)
                    disp.clear()
                    draw.text((x+40,top+32),'주문완료',font=font,fill=255)
                    disp.image(image)
                    disp.display()
                    time.sleep(2)
                    choice_menu=[]
                    menu_cnt=[0,0,0,0,0,0,0,0]
                    break
        else:
            pass         
    time.sleep(2)
except KeyboardInterrupt:
    GPIO.remove_event_detect(btn_1)
    GPIO.remove_event_detect(btn_2)
    GPIO.remove_event_detect(btn_3)
    GPIO.remove_event_detect(btn_4)
    GPIO.remove_event_detect(btn_5)
    GPIO.cleanup()



