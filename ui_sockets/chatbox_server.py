import socket
from sqlite3 import connect
import time
import threading
from tkinter import *
import sys
host = socket.gethostbyname(socket.gethostname())
print('server will start on host:',host) 
Header=64
port=8080
Format='utf-8'
Disconnect_messsage='!Disconnect'
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected=True
    while connected:
        msg_length=conn.recv(Header).decode(Format)
        if msg_length:
            msg_length=len(msg_length)
            msg=conn.recv(msg_length).decode(Format)
            if msg==Disconnect_messsage:
                connected=False
            print(f"[{addr}: {msg}]")
            # conn.send('Msg received'.encode(Format))
            conn.send(msg.encode(Format))
    conn.close()

def start():
    server.listen()
    print(f"[Listening] sever is listening on{host}")
    while True:
        conn,addr=server.accept()
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[Active Connections]{threading.active_count() - 1}")
print("[Starting] server is starting...")
start()