import threading
import socket
from pynput.keyboard import Listener
from keymap import execuite

n = input("choose a nickname:")


host = '192.168.1.6'  # localhost
port = 55555
class inuse:
    use=False
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((host, port))

using=inuse()
def re():
    while True:
        # try:
        m = c.recv(1024).decode('ascii')
        if m == 'nick':
            c.send(n.encode('ascii'))
        else:
            execuite(m ,using)
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
    if  using.use:
        return
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
    if  using.use:
        return
    unmodified_key = Keyboard_listner.canonical(key)
    c.send(f'{find_Key_to_send(unmodified_key ,key)}_=R\n'.encode('ascii'))


Keyboard_listner = Listener(on_press=on_press, on_release=on_release)
Keyboard_listner.start()
