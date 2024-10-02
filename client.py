import socket

# Define server address and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345
















# Create a socket object
client_socket = socket.socket()










# Connect to server
client_socket.connect((SERVER_HOST, SERVER_PORT))




print("connected to serever")







# Send data to server
while True:
    message = input("Enter your name  (type 'exit' to quit): ")
    if message.lower() == 'exit':
        break
    client_socket.sendall(message.encode('utf-8'))

    

    # Receive data from server
    data = client_socket.recv(1024)
    print(f"Received from server: {data.decode('utf-8')}")

# Close the socket
client_socket.close()
print("Connection closed.")
