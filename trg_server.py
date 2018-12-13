import pickle
import socket
import math
import numpy as np



def process_client(client_socket):
    data = client_socket.recv(1024)
    data = data.decode()
    x, y = data.split(',')
    x, y = float(x), float(y)
    hyp =  np.round(math.sqrt(x * x + y * y), 2)
    theta = np.round(math.asin(x / hyp), 2)
    gamma = np.round(math.asin(y / hyp), 2)
    content = f'{hyp},{theta},{gamma}'
    ans = bytes(content, 'UTF-8')
    return ans


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
with server_socket:
    host = socket.gethostbyname('localhost')
    port = 12345
    addr = (host, port)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print('Listening....')
    while True:
        client_socket, client_addr = server_socket.accept()
        message = process_client(client_socket)
        client_socket.send(message)
        






    
