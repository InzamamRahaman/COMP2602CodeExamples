import socket 
import random 


# instantiate client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_host = socket.gethostbyname('localhost')
server_port = 6300
server_addr = (server_host, server_port)


# Generate data 
num = random.randint(1, 10)
message = f'RANK {num}?'
print('Sending ', message)
data = bytes(message, 'UTF-8')

# send data to the server
client_socket.sendto(data, server_addr)

# get response from server and output to user
response, server_addr = client_socket.recvfrom(1024)
response = response.decode()
print(response)
