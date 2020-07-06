import tkinter as tk
import Client_py
import _thread

# main window for getting and connecting into a network
main_window = tk.Tk()
ip_label = tk.Label(text="Enter the IP-address")
ip_entry = tk.Entry(master=main_window)
port_label = tk.Label(text="Enter the Port-ID")
port_entry = tk.Entry(master=main_window)
cnt_btn = tk.Button(master=main_window, text="Connect")


def kill():
    main_window.destroy()
    exit(0)
    # return "break"


quit_btn = tk.Button(master=main_window, text="quit", command=lambda: kill())
ip_label.pack()
ip_entry.pack()
port_label.pack()
port_entry.pack()
cnt_btn.pack(side=tk.LEFT)
quit_btn.pack(side=tk.RIGHT)


def connect(event):
    Client_py.establish(str(ip_entry.get()), int(port_entry.get()))
    main_window.destroy()
    return "break"


cnt_btn.bind("<Button-1>", connect)
main_window.mainloop()


def eror_pop():
    error_pop_up = tk.Tk()
    pop_error = tk.Label(master=error_pop_up, text="No connection could be made because the target machine actively "
                                                   "refused it")
    quit_btn = tk.Button(master=error_pop_up, text="quit")
    pop_error.pack()
    quit_btn.pack()

    def destroy(event):
        Client_py.client.close()
        error_pop_up.destroy()
        exit(0)

    quit_btn.bind("<Button-1>", destroy)

    error_pop_up.mainloop()


if Client_py.error_flag:
    eror_pop()


elif Client_py.connection_flag:

    # creating a main window
    window = tk.Tk()

    # Creating a frame for entering and sending the messages
    user_frame = tk.Frame(master=window)
    user_frame.grid(row=1, column=0)
    text_field = tk.Entry(master=user_frame)
    # my_message = text_field.get()
    text_field.pack(side=tk.LEFT)
    send_button = tk.Button(master=user_frame, text="Send")


    def send_msg(event):
        Client_py.send_message(text_field.get())


    send_button.bind("<Button-1>", send_msg)
    send_button.pack(side=tk.RIGHT)
    # window.bind("<Return>", Client_py.send_message(text_field.get()))  # Enter Key also to send message

    # Creating a frame for receiving the messages from the client
    client_frame = tk.Frame(master=window)
    client_frame.grid(row=0, column=0)
    label = tk.Label(master=client_frame, text="Recieved message")
    label.pack(side=tk.TOP)
    rcve_msg = tk.Label(master=client_frame, text=".....")
    Listen_btn = tk.Button(master=client_frame, text="Listen")
    Listen_btn.pack()


    def display():
        while 1:
            rcve_msg["text"] = Client_py.my_message


    _thread.start_new_thread(display, tuple())
    rcve_msg.pack()


    def listen_btn(self):
        Client_py.listen()


    Listen_btn.bind("<Button-1>", listen_btn)
    window.mainloop()

