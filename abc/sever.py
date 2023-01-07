import threading
import socket

host = '192.168.1.6'  # localhost
port = 55555

sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sever.bind((host, port))
sever.listen()
clients = []
nn = []


def bc(message,from_client):
    print(message)
    for client in clients:
        if client==from_client:
            continue
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            bc(message,client)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            n = nn[index]
            bc(f'{n} left'.encode('ascii'),client)
            nn.remove(n)
            break


def r():
    while True:
        c, a = sever.accept()
        print(f"accepted connection{a}")
        c.send("nick".encode('ascii'))
        n = c.recv(1024).decode('ascii')
        nn.append(n)
        clients.append(c)
        print(f'nickname of the client is{n}!')
        bc(f'nickname of the client is{n}!'.encode('ascii'),c)
        c.send(f'connected'.encode('ascii'))
        thread = threading.Thread(target=handle,args=[c])

        thread.start()


print('server is listening')
try:
    r()
    
except KeyboardInterrupt:
    exit()
