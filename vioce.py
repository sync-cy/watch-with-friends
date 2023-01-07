from audioNL import AudioSender
from audioNL import AudioReceiver

import threading

import socket

#io socket.gethostbyname (socketurethes the

receiver = AudioReceiver ("localhost", 9999)

receive_thread =threading. Thread(target=receiver.start_server)

sender= AudioSender("136.185.197.149", 9999)

sender_thread=threading.Thread(target=sender.start_stream)

receive_thread.start() 
sender_thread.start()