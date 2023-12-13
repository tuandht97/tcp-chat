"""Server for Multithreaded (asynchronous) Chat Application."""
from socket import AF_INET, socket, SOCK_STREAM    #SOCK_STREAM used to create TCP protocols AF_INET= Address from the internet
from threading import Thread


def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Hãy nhập tên đội của mình bên dưới và nhấn Enter để bắt đầu.", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    name = client.recv(BUFSIZ).decode("utf8") #Bytes sent in UTF-8 format
    welcome = 'Chào mừng đội thi %s đến với cuộc thi Hành trình khám phá tri thức! \n Gõ {quit} để thoát.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))#Prints if user has left the app
            break

def handle_error(sock, error):
    """Handles socket error and removes the socket from the list of clients."""
    print("Socket error:", error)
    sock.close()
    if sock in clients:
        clients.remove(sock)
        
    
def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""

    for sock in clients:
        try:
            sock.send(bytes(prefix, "utf8") + msg)
        except socket.error as e:
            # Handle the error (e.g., remove the socket from the list of clients)
            handle_error(sock, e)


        
clients = {}
addresses = {}

HOST = ''
PORT = 33000 #Random port no used
BUFSIZ = 1024 # No of bytes that can be sent in a message stored in buffersize
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR) # Used to bind the IP Address and port no of a new client

if __name__ == "__main__":
    SERVER.listen(5) # Max 5 connections will be accepted by multiple clients
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()