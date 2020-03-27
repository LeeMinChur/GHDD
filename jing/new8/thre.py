import threading
import time


class thre():

    def thred7(self):
        print(1)
    def thred(self):
        while True:
            self.thred7()
            time.sleep(2)

    def thred2(self):
        while True:
            print(2)
            time.sleep(2)

    def thred6(self):
        a = threading.Thread(target=thre().thred)
        b = threading.Thread(target=thre().thred2)
        a.start()
        b.start()

class thre2():

    def thred3(self):
        while True:
            print(3)
            time.sleep(2)
    def thred4(self):
        while True:
            print(4)
            time.sleep(2)

# a = threading.Thread(target=thre().thred)
# b = threading.Thread(target=thre2().thred3)
#
# a.start()
# b.start()

class thre3():
    def thred5(self):
        a = threading.Thread(target=thre().thred)
        b = threading.Thread(target=thre2().thred3)
        a.start()
        b.start()

thre().thred6()
