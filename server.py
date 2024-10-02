import socket

# Define host and port
HOST = '127.0.0.1'  # localhost
PORT = 12345        # Port to listen on (non-privileged ports are > 1023)  



# Create a socket object
server_socket = socket.socket()






















# Bind the socket to the host and port
server_socket.bind((HOST, PORT))





# Listen for incoming connections
server_socket.listen(5)
print(f"Server is listening on {HOST}:{PORT}...")














# client_socket_obj ,client_ip_address = server_socket.accept()





# print("client_socket_obj",client_socket_obj)
# print("client_ip_address",client_ip_address)












# Accept a client connection
client_socket, client_address = server_socket.accept()
print(f"Connected to client at {client_address}")

custom_msg = ""
# Receive data from client
while True:
    
    data = client_socket.recv(1024)
    if not data:
        pass
    else:
        decoded_data =  data.decode()
        custom_msg = f"Hello Good morning !!!! ::: {decoded_data}"
        # print(f"Received from client: {data.decode()}")   ## to make it to string
        print("type of custom msg",type(custom_msg))
    # Echo back to 
    encoded_msg = custom_msg.encode()


    client_socket.sendall(encoded_msg)

# # Close the sockets
# client_socket.close()
# server_socket.close()
# print("Connection closed.")
