from audioNL import AudioSender
from audioNL import AudioReceiver

import threading

import socket

#io socket.gethostbyname (socketurethes the

receiver = AudioReceiver ("192.168.235.242", 5555)

receive_thread =threading. Thread(target=receiver.start_server)

sender= AudioSender("192.168.235.235", 9999)

sender_thread=threading.Thread(target=sender.start_stream)

receive_thread.start() 
sender_thread.start()