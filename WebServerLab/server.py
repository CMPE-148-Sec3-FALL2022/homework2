# import socket module
from socket import *
import sys  # In order to terminate the program

# Prepare a sever socket
PORT = 6789  # port specified in instructions
HOST = "127.0.0.1"  # default localhost IP address
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((HOST, PORT))  # bind the port
serverSocket.listen(1)  # start listening for connections

while True:
    # Establish the connection
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()  # accept the TCP connection
    try:
        # Get the message
        message = connectionSocket.recv(1024)  # recieve with buffer size of 1024
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.readlines()
        f.close()

        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.0 200 OK\r\n\r\n".encode())

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        connectionSocket.send("HTTP/1.0 404 Not Found\r\n\r\n".encode())

        # Close client socket
        connectionSocket.send("404 Not Found".encode())

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
