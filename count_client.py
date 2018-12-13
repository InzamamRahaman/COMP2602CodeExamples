import socket 
import random 


# instantiate client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_host = socket.gethostbyname('localhost')
server_port = 6300
server_addr = (server_host, server_port)

bad_message = "FOOBAR!"

for i in range(100):
    # Generate data 
    num = random.randint(1, 3)
    message = f'{num}' if random.random() <= 0.5 else bad_message
    print('Sending ', message)
    data = bytes(message, 'UTF-8')

    # send data to the server
    client_socket.sendto(data, server_addr)



