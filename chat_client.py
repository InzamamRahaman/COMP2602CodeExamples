import socket 
import threading

class Listener(threading.Thread):
    def __init__(self, client_socket):
        super().__init__()
        self.client_socket = client_socket
    
    def run(self):
        message = self.client_socket.recv(2048)
        message = message.decode()
        print(message + '\n')

    def send(self, message):
        message = bytes(message, 'UTF-8')
        self.client_socket.send(message)

server_host = socket.gethostbyname('localhost')
server_port = 12345
server_addr = (server_host, server_port)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
with client_socket:
    listener = Listener(client_socket)
    client_socket.connect(server_addr)
    listener.start()
    while True:
        message = input("")
        listener.send(message)



