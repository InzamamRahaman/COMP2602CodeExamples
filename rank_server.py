import socket

def process_message(message):
    web_arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    
    # transform to a normal string
    message = message.decode()

    # each message is of the format "RANK x?"
    # There is always a whitespace between the "RANK" and "x?" (which contains the actual useful information)
    # We split the string by whitespace and store the two parts into separate variables
    rank_string, rank_num = message.split()

    # Alternative strategy: since we know that the number 
    # starts at position 5 in the message and goes up to but does
    # not include the last character, we can simply use a slice
    # pull the "x" out of the string
    #rank_num = message[5:-1]

    # the rank portion is of the form "x?"
    # we need to cast this to an integer
    # but we can't with that "?". Note that "?" is the last character. We can remove the question mark but taking 
    # every character up to but not including the last character
    rank_num = rank_num[:-1]

    # cast to an integer
    rank_num = int(rank_num)

    # subtract 1 to get the index in web_arr
    rank_idx = rank_num - 1
    response = web_arr[rank_idx]

    # prepare response
    response = bytes(response, 'UTF-8')
    return response


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

    # prepare response to client
    response = process_message(message)

    # send response to client
    server_socket.sendto(response, client_addr)
