import socket
import threading
import time
import sys

# from chatbox_server import Disconnect_messsage
Header=64
Format='utf-8'
Disconnect_messsage="Disconnect"
clientt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host= 'orato' #input('enter host name please\n')
port=8080
clientt.connect((host,port))
# print('connected sucessfully')
def send(msg):
    message=msg.encode(Format)
    msg_length=len(message)
    send_length=str(msg_length).encode(Format)
    send_length += b' ' *(Header - len(send_length))
    clientt.send(send_length)
    clientt.send(message) 
    print(clientt.recv(2048).decode(Format))
# def handle_msg(msg):
#     print(msg)

# thread=threading.Thread(target=handle_msg,args=(clientt.recv(1024).decode(Format)))
# thread.start()

send(input())
