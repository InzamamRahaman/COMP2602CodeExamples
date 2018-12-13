import socket 
import operator

# abstracts operation selection from specification 
OPERATIONS = {
    '+': operator.add,
    '-': operator.sub, 
    '*': operator.mul, 
    '/': operator.truediv
}

# processes a message from the client according to the client specification
def process_message(client_message):
    """
    Processes a message from the client. A client message is expected to be a simple binary infix expression containing with operands
    comprising only a single digit

    @param {client_message}: the message from the client
    @return: the response to client - contains the answer to the supplied expression encoded as bytes to be sent across the wire
    """
    decoded_message = client_message.decode()
    operand1 = int(decoded_message[0])
    operation_symb = decoded_message[1]
    operand2 = int(decoded_message[2])
    operation = OPERATIONS[operation_symb]
    result = operation(operand1, operand2)
    result_as_string = str(result)
    response = bytes(result_as_string, 'UTF-8')
    return response 


# set up server socket to receive packets
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_host = socket.gethostbyname('localhost')
server_port = 12345
server_addr = (server_host, server_port)
server_socket.bind(server_addr)

# infinite loop
print('Awaiting messages from the clients.....')
while True:

    # get data from the client
    message, client_addr = server_socket.recvfrom(1024)

    # process message and get response
    response = process_message(message)

    # send the response
    server_socket.sendto(response, client_addr)




