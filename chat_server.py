import threading 
import socket


class Client(threading.Thread):
    def __init__(self, client_addr, client_socket, all_connections, num):
        super().__init__()
        self.client_addr = client_addr 
        self.client_socket = client_socket
        self.all_connections = all_connections
        self.num = num

    def _get_notified(self, message, num):
        if self.num!= num:
            message = message.decode()
            message = f'#{num} says: {message}'
            message = bytes(message, 'UTF-8')
            self.client_socket.send(message)

    def _notify(self, message):
        for client in self.all_connections:
            client._get_notified(message, self.num)
    def run(self):
        message = self.client_socket.recv(2048)
        self._notify(message)

        

connected_clients = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
with server_socket:
    host = socket.gethostbyname('localhost')
    port = 12345
    addr = (host, port)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)
    num = 0
    print('Listening....')
    while True:
        client_socket, client_addr = server_socket.accept()
        print(client_socket)
        print(f'Got from client #{num}')
        client = Client(client_addr, client_socket, connected_clients, num)
        connected_clients.append(client)
        num += 1 
        client.start()






    
