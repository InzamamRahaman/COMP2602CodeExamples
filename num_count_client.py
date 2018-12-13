import socket 
import pickle
import random 

TERMINATOR = 'STOP'

# Generate random integer from 1 to 20 inclusive
def random_int():
    lo = 1
    hi = 20
    num = random.randint(lo, hi)
    return num


server_host = socket.gethostbyname('localhost')
server_port = 6300
server_addr = (server_host, server_port)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
with client_socket:
    client_socket.connect(server_addr)
    while True:
        num = random_int()
        message = f'{num}'
        message = bytes(message, 'UTF-8')
        client_socket.send(message)
        response = client_socket.recv(1024)
        response = response.decode()
        # If we receieve the terminator from the server, then we know we need to stop
        if response == TERMINATOR:
            break



