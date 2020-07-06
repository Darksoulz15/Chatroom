#!/usr/bin/env python3
import sys
import socket
import _thread
my_message = "HI"
IP_address = str(sys.argv[1])  # Host IP-addresss
Port_ID = int(sys.argv[2])  # HOST port ID

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP_address, Port_ID))


def send_message(threadname, my_message):
    while my_message != "end":
        my_message = input("=>")

        client.send(my_message.encode())
        if my_message == "end":
            client.close()
            exit(0)


_thread.start_new_thread(send_message, ("client_send_thread", my_message))
while True:
    data = client.recv(1024).decode()
    print(str(data))

client.close()
