import socket 


# setup the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# get host addressing data
server_host = socket.gethostbyname('localhost')
server_port = 12345
server_addr = (server_host, server_port)

terminator = '***'

# infinite loop
while True:

    # get input from stdin
    expression = input('Please enter a binary infix expression without spaces:')
    expression = expression.strip()

    # if we have recieved our terminator from the user, we close the programme
    if expression == terminator:
        break 

    # prepare message and send it to the server
    message = bytes(expression, 'UTF-8')
    client_socket.sendto(message, server_addr)

    # get the response and output it to the user
    response, _ = client_socket.recvfrom(1024)
    response = response.decode()
    print(expression, '=', response)

client_socket.close()