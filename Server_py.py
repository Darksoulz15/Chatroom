import socket
import sys
import _thread
from threading import Thread

# Simple initialization of variable(in python they should be termed as objects)

Max_clients = 10
message = "Welcome to chat room!!"
list_of_client_IP = []
list_of_client_socket = []

# inputting the the IP-address and port id for the HOST

IP_address = str(sys.argv[1])  # Standard loop-back interface address (127.0.0.1-local-host)
Port_ID = int(sys.argv[2])  # Port to listen on (non-privileged ports are > 1023)
print("Server successfully Established on IP-address: " + IP_address + "and Port: " + str(Port_ID))

# 3 main steps to establish a socket
# server is the object of socket created
# bind associates all IPaddress and the port
# .listen() keeps snooping through the port for any requests
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP_address, Port_ID))
server.listen(Max_clients)

# this function tends to broadcast the messages to every client except back to the sender itself

def broadcast(received_message, clients, client_socket):
    for client in list_of_client_socket:
        if client != client_socket:
            received_message = str(clients) + ": " + received_message
            client.send(received_message.encode())

# this fuunction recieves the messages from all the connected clients

def receive_message(ip):
    while True:
        for clients in list_of_client_socket:
            message = clients.recv(1024).decode()
            broadcast(message, ip, clients)
            print(str(ip) + ": " + str(message))

# this funtion tend to send the message by the the host to every client connected

def send_message():
    while True:
        my_message_s = input("=>")
        if my_message_s == "show connected device":
            print("List of Connected devices is: " + str(list_of_client_IP))
        else:
            broadcast(my_message_s, IP_address, None)
        if my_message_s == "end":
            for all_clients in list_of_client_socket:
                all_clients.close()
            server.close()
            exit(0)


_thread.start_new_thread(send_message, ()) # multithreadding

# accept any of the client request from the defined port and pass the object to the recieve_message funtion
# for every new client joining the server
def connection_establish():
    count = 0
    while count < Max_clients:
        print("Waiting for Client to Connect.")

        new_client_connect, IP_address_of_client = server.accept()
        list_of_client_IP.append(IP_address_of_client)
        list_of_client_socket.append(new_client_connect)
        print("New client of IP-address: " + repr(list_of_client_IP[-1]) + "is connected")
        count = len(list_of_client_socket)
        print("List of Connected devices is: " + repr(list_of_client_IP))
        _thread.start_new_thread(receive_message(IP_address_of_client), ())
connection_establish()

