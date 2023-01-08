import threading
import socket,time
from pynput.keyboard import Listener
from keymap import *

n = input("choose a nickname:")


host = '192.168.1.6'  # localhost
port = 4444
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((host, port))
using:bool=False
def execuite(recKey:str):
    global using
    if recKey=="connected" or recKey.startswith('nickname') or recKey.endswith('left'):
        print(recKey)
        return
    lines=recKey.splitlines()
  
    if(len(lines)<1):
        for line in lines:
            execuite(line,using)
    else:
        key,op= lines[0].split('_=')
        print(f'[{key}, {op}]')
        using=True
        # Keyboard_listner.stop()
        if key in special_keylist:
            if op=='P':
                keyboardContoller.press(special_keymap.get(key))
            if op=='R':
                keyboardContoller.release(special_keymap.get(key))  
        elif key[1] in string.printable:
            if op=='P':
                keyboardContoller.press(key[1])
            if op=='R':
                keyboardContoller.release(key[1])
        time.sleep(.005)
        # Keyboard_listner.start()
        using=False

def re():
    while True:
        # try:
        m = c.recv(1024).decode('ascii')
        if m == 'nick':
            c.send(n.encode('ascii'))
        else:
            execuite(m )
        # except:
        #     print('error')
        #     c.close()
        #     break


def write():
    while True:
        m = f'{n}:{input("")}'
        c.send(m.encode('ascii'))


rt = threading.Thread(target=re)
rt.start()
wt = threading.Thread(target=write)
# wt.start()


def on_press(key):
    
    print(f'key={key},using={using}  + P')
    if not using:
        unmodified_key = Keyboard_listner.canonical(key)
        c.send(f'{find_Key_to_send(unmodified_key ,key)}_=P\n'.encode('ascii'))


def find_Key_to_send(unmodified_key, key):
    # print(f'[un= {unmodified_key}, key= {key}]')
    if len(str(unmodified_key)) > len(str(key)):
        return unmodified_key
    else:
        if '\\x'in str(key):
            # print('oh')
            return unmodified_key
        return key


def on_release(key):
    print(f'key={key},using={using}  + r')
    if not using:
        unmodified_key = Keyboard_listner.canonical(key)
        c.send(f'{find_Key_to_send(unmodified_key ,key)}_=R\n'.encode('ascii'))


Keyboard_listner = Listener(on_press=on_press, on_release=on_release)
Keyboard_listner.start()
