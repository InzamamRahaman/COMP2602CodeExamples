import socket 
import pickle


server_host = socket.gethostbyname('localhost')
server_port = 12345
server_addr = (server_host, server_port)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
with client_socket:
    arr = [1,2,3]
    message = pickle.dumps(arr)
    client_socket.connect(server_addr)
    client_socket.send(message)
    response = client_socket.recv(1024)
    response = response.decode()
    print(response)



