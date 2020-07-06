#!/usr/bin/env python3
import sys
import socket
import _thread

my_message = "HI"
error_flag = False
connection_flag = False
# if len(sys.argv)!=3:
#     print("IP or PorT ID Missing")
#     exit(0)
# else:
#     IP_address = str(sys.argv[1])  # Host IP-addresss
#     Port_ID = int(sys.argv[2])  # HOST port ID
# IP_address = "127.0.0.1"
# Port_ID = 3498
client = object


def establish(IP_address, Port_ID):
    try:
        global client
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((IP_address, Port_ID))
        global connection_flag
        connection_flag = True
    except:

        global error_flag
        error_flag = True
        print("No connection could be made because the target machine actively refused it")
        return


def send_message(msg):
    client.send(msg.encode())
    if msg == "end":
        client.close()
        exit(0)


# _thread.start_new_thread(send_message, ("client_send_thread", my_message))
def receive_message():
    while 1:
        data = client.recv(1024).decode()
        global my_message
        my_message = str(data)
        print(str(my_message))


def listen():
    _thread.start_new_thread(receive_message, tuple())
