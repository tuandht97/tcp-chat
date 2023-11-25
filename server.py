import tkinter as tk
import socket
import threading

window = tk.Tk()
window.title("Server")


HOST = "127.0.0.1"
PORT = 8080
client_name = ""
clients = []
client_names = []

def send_recv_client_msg(client_connection, client_ip_addr):
    global server, client_name, clients, clients_addr
    client_msg = ""
    client_name = client_connection.recv(4096)
    client_name = client_name.decode("utf-8")
    print(type(client_name))
    welcome_message = "Welcome " + client_name + ". Use 'exit' to quit"
    client_connection.send(welcome_message.encode("utf-8"))
    client_names.append(client_name)

    update_client_names_display(client_names) # method, TODO

    while True:
        print("Waiting to receive message from a client")
        data = client_connection.recv(4096)
        if not data: break
        if data == "exit": break

        client_msg = data.decode("utf-8")
        idx = get_client_index(clients, client_connection)
        sending_client_name = client_names[idx]

        for client in clients:
            if client != client_connection:
                message_to_other_clients = sending_client_name + "->" + client_msg
                client.send(message_to_other_clients.encode("utf-8"))

    # remove client
    idx = get_client_index(clients, client_connection)
    del client_names[idx]
    del clients[idx]
    client_connection.close()

    update_client_names_display(client_names) # TODO

def get_client_index(client_list, curr_client):
    for i in range(0, len(client_list)):
        if client_list[i] == curr_client:
            return i
    return -1 

def update_client_names_display(name_list):
    tkDisplay.config(state=tk.NORMAL)
    tkDisplay.delete('1.0', tk.END)
    for client in name_list:
        tkDisplay.insert(tk.END, client+"\n")
    tkDisplay.config(state=tk.DISABLED)


def accept_clients(some_server):
    print("got to accept clients function")
    while True:
        client, addr = some_server.accept()
        print("Server accepted a client")
        clients.append(client)
        threading._start_new_thread(send_recv_client_msg, (client,addr),)

def start_server():
    startButton.config(state=tk.DISABLED)
    stopButton.config(state=tk.NORMAL)
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Created server socket")
    server.bind((HOST, PORT))
    server.listen(5)
    print("Server is listening")
    threading._start_new_thread(accept_clients, (server,))

    hostLabel["text"] = "Host: " + HOST
    portLabel["text"] = "Port: " + str(PORT)



def stop_server():
    stopButton.config(state=tk.DISABLED)
    startButton.config(state=tk.NORMAL)

# top section has two buttons, one to start the server and one to stop it.
topFrame = tk.Frame(window)

startButton = tk.Button(topFrame, text="Start", command=start_server)
startButton.pack(side=tk.LEFT)

stopButton = tk.Button(topFrame, text="Stop", command=stop_server, state=tk.DISABLED)
stopButton.pack()
topFrame.pack(side=tk.TOP, pady=(5,0))

# center frame displays host and port number of server 
centerFrame = tk.Frame(window)
hostLabel = tk.Label(centerFrame, text="Host: x.x.x.x")
hostLabel.pack(side=tk.LEFT)
portLabel = tk.Label(centerFrame, text="Port: ####")
portLabel.pack()
centerFrame.pack(side=tk.TOP, pady=(5,0))

clientsFrame = tk.Frame(window)
clientsLabel = tk.Label(clientsFrame, text="*****CONNECTED CLIENTS******")
scrollBar = tk.Scrollbar(clientsFrame)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
tkDisplay = tk.Text(clientsFrame, height=15, width=40)
tkDisplay.pack(side=tk.LEFT, fill=tk.Y, padx=(5,0))

#tkDisplay.insert(tk.END, "User 1\n")
scrollBar.config(command=tkDisplay.yview)
tkDisplay.config(yscrollcommand=scrollBar.set, background="#F4F6F7", highlightbackground="grey", state="disabled")
clientsFrame.pack(side=tk.BOTTOM, pady=(5, 10))

window.mainloop()
