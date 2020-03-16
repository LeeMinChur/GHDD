#-*- coding:utf-8-*-

import threading
import socketserver
import socket
import sys

class CustomException(Exception):

    def __init__(self,value):

        self.value=value
    def __str__(self):
        return self.value


def raise_exception(err_msg, ip_addr='NONE'):
    raise custom_Exception(err_msg)

def print_delimiter():
    print('='*20)

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):

        cur_thread=threading.current_thread()
        print("{} was started for {}".format(cur_thread.getName(),self.client_address[0]))

        while True:
            try:
                self.recv_data=self.request.recv(1024).strip()

                if self.recv_data.decode('utf-8')=="/quit" or not self.recv_data.decode('utf-8'):
                    print_delimiter()
                    raise_exception("{} was gone".format(self.client_address[0]))
            except NameError as e:
                print("{0} got an error: {1}".format(self.client_address[0],e))
                self.request.send("bye".encode())
                break
            except CustomException as e:
                print(e)
                self.request.send("bye".encode())
                break
            print("{} wrote:".format(self.client_address[0]))
            print(self.recv_data.decode())

            self.request.sendall(self.recvdata.encode(),upper())

        print("{}was ended for {}".format(cur_thread.getName(),self.client_address[0]))
        print_delimiter()

class ThreadedTCPServer(socketserver.ThreadingMixIn,socketserver.TCPServer):
    pass

if __name__=="__main__":
    HOST,PORT="0.0.0.0",3000

    try:
        server = ThreadedTCPServer((socket.gethostbyname(HOST),PORT),ThreadedTCPRequestHandler)

    except socket.error as msg:
        print("bind failed.closing..")
        print("Error code : %s \nError Message: %s " % (str(msg[0]) ,msg[1]))
        sys.exit()

    print("socket Bind os {}".format(PORT))
    ip,port = server.server_address

    server_thread=threading.Thread(target=server.serve_forever)
    server_thread.daemon=True
    server_thread.start()
    print("server loop running in thread:", server_thread.name)
    server.serve_forever()
    server.shotdown()
    server.server_close()
    
                                                
                                                                                        
