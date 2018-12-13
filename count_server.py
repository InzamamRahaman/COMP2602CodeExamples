import socket


counts = [0, 0, 0]

def process_message(message):
    message = message.decode()
    if message == '1':
        counts[0] += 1
    elif message == '2':
        counts[1] += 1
    else:
        counts[2] += 1


# setup socket to recieve data from the client
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_host = socket.gethostbyname('localhost')
server_port = 6300
server_addr = (server_host, server_port)
server_socket.bind(server_addr)

print('Listening......')
while True:
    # get data from the client
    message, client_addr = server_socket.recvfrom(1024)

    # handle client message
    process_message(message)

    if counts[1] == 10:
        print(f'{counts[0]}, {counts[1]}, {counts[2]}')
        break

server_socket.close()

