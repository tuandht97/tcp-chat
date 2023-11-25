"""Tkinter GUI Chat Client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter


def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")  # Decoding of data is done on the client side
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # Event is passed by binders.
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.destroy()


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()


def connect_to_server():
    """Connects to the server with the specified IP and port."""
    host = host_entry.get()
    port = port_entry.get()

    if not port:
        port = 33000
    else:
        port = int(port)

    global client_socket, ADDR
    ADDR = (host, port)

    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(ADDR)

    # Destroy the connection frame and start the chat frame
    connection_frame.destroy()
    chat_frame.pack()

    # Start the receive thread after connecting to the server
    receive_thread = Thread(target=receive)
    receive_thread.start()


# Create the main window
top = tkinter.Tk()
top.title("CHAT APPLICATION")

# Create frames for connection and chat
connection_frame = tkinter.Frame(top)
chat_frame = tkinter.Frame(top)

# Connection Frame
host_label = tkinter.Label(connection_frame, text="Host IP:")
host_label.pack()
host_entry = tkinter.Entry(connection_frame)
host_entry.pack()

port_label = tkinter.Label(connection_frame, text="Port:")
port_label.pack()
port_entry = tkinter.Entry(connection_frame)
port_entry.pack()

connect_button = tkinter.Button(connection_frame, text="Connect", command=connect_to_server)
connect_button.pack()

connection_frame.pack()

# Chat Frame
messages_frame = tkinter.Frame(chat_frame)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("Type here.")
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(chat_frame, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(chat_frame, text="Send", command=send)
send_button.pack()

chat_frame.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

BUFSIZ = 1024

tkinter.mainloop()  # Starts GUI execution.