# -*- coding: utf-8 -*-
"""
@author: ChatRoom ==> Client
"""

import socket
import threading

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 7000))

def receive():
    while True:
        try:
           
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break
        
def write():
    while True:

write_thread = threading.Thread(target=write)
write_thread.start()