"""Tkinter GUI Chat Client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import re


def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")  # Decoding of data is done on the client side
            msg_list.insert(tkinter.END, re.sub(r'\d{6}-', '', msg))
            msg_list.see(tkinter.END) 

        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # Event is passed by binders.
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes("111111-" + msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.destroy()


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()


def send_count_khoidong(num):
    message = "111111-_________Khởi động - Câu {}".format(str(num))
    my_msg.set(message)
    send()

def send_count_vcnv(num):
    message = "111111-_________VCNV - Câu {}".format(str(num))
    my_msg.set(message)
    send()
    count_buttons_vcnv[num-1].config(state=tkinter.DISABLED)

def send_count_tangtoc(num):
    message = "111111-_________Tăng tốc - Câu {}".format(str(num))
    my_msg.set(message)
    send()
    count_buttons_tangtoc[num-1].config(state=tkinter.DISABLED)

def send_count_vedich(num):
    message = "111111-_________Về đích - Câu {}".format(str(num))
    my_msg.set(message)
    send()
    # count_buttons_vedich[num-1].config(state=tkinter.DISABLED)


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
top.title("HÀNH TRÌNH KHÁM PHÁ TRI THỨC 2023")

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

connect_button = tkinter.Button(connection_frame, text="Kết nối", command=connect_to_server)
connect_button.pack()

connection_frame.pack()

# Chat Frame
messages_frame = tkinter.Frame(chat_frame)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("Nhập tên đội")
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=15, width=100, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

input_frame = tkinter.Frame(chat_frame)
input_frame.pack()

entry_field = tkinter.Entry(input_frame, textvariable=my_msg, width=50)
entry_field.grid(row=0, column=0, padx=4, pady=4, sticky="we")
entry_field.bind("<Return>", send)

send_button = tkinter.Button(input_frame, text="Gửi câu trả lời", command=send)
send_button.grid(row=0, column=1, padx=4, pady=4)

count_button_frame = tkinter.Frame(input_frame)
count_button_frame.grid(row=1, column=0, columnspan=3, padx=4, pady=4)

#Khoi dong
count_button_frame = tkinter.Frame(input_frame)
count_button_frame.grid(row=1, column=0, columnspan=3, padx=4, pady=4)

number_label = tkinter.Label(count_button_frame, text="Khởi động:")
number_label.grid(row=0, column=0, padx=4, pady=4)

count_buttons = []
for i in range(1, 13):
    button = tkinter.Button(count_button_frame, text=str(i), width=5, command=lambda num=i: send_count_khoidong(num))
    button.grid(row=0, column=i, padx=4, pady=4)
    count_buttons.append(button)


# Vuot chuong ngai vat
count_buttons_vcnv = []
number_label_row2 = tkinter.Label(count_button_frame, text="VCNV:")
number_label_row2.grid(row=1, column=0, padx=4, pady=4)

for i in range(1, 6):
    button = tkinter.Button(count_button_frame, text=str(i), width=5, command=lambda num=i: send_count_vcnv(num))
    button.grid(row=1, column=i, padx=4, pady=4)
    count_buttons_vcnv.append(button)

#Tang toc
count_buttons_tangtoc = []
number_label_row2 = tkinter.Label(count_button_frame, text="Tăng tốc:")
number_label_row2.grid(row=2, column=0, padx=4, pady=4)

for i in range(1, 9):
    button = tkinter.Button(count_button_frame, text=str(i), width=5, command=lambda num=i: send_count_tangtoc(num))
    button.grid(row=2, column=i, padx=4, pady=4)
    count_buttons_tangtoc.append(button)

# Ve dich
count_buttons_vedich = []
number_label_row3 = tkinter.Label(count_button_frame, text="Về đích:")
number_label_row3.grid(row=3, column=0, padx=4, pady=4)

for i in range(1, 6):
    button = tkinter.Button(count_button_frame, text=str(i), width=5, command=lambda num=i: send_count_vedich(num))
    button.grid(row=3, column=i, padx=4, pady=4)
    count_buttons_vedich.append(button)


chat_frame.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

BUFSIZ = 1024

tkinter.mainloop()  # Starts GUI execution.