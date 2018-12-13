import pickle
import socket
import math
import numpy as np

TERMINATOR = 'STOP'

# the ith index stores the count for i+1
# except for the last entry, which stores the invalid count
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
EMPTY = 'EMPTY'

def process_client(client_socket):
    data = client_socket.recv(1024)
    data = data.decode()
    num = int(data)
    idx = min(10, num - 1) # get array index to increment
    arr[idx] += 1
    ans = bytes(EMPTY, 'UTF-8') # send dummy back to client
    return ans


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
with server_socket:
    host = socket.gethostbyname('localhost')
    port = 6300
    addr = (host, port)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print('Listening....')
    while True:
        client_socket, client_addr = server_socket.accept()

        # continue accepting from the client until we have received and processed 100 messages
        while sum(arr) < 100:
            message = process_client(client_socket)
            client_socket.send(message)
        
        # tell the client to stop
        message = bytes(TERMINATOR, 'UTF-8')
        client_socket.send(message)

        # print the counts
        for i in range(10 + 1):
            x = arr[i]
            if i < 10:
                print(f"# of {i + 1}'s: {x}'")
            else:
                print(f'Num invalid: {x}')
        arr = [0] * 11
        
        






    
