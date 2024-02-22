#Real-Time Chat Application with Pickling:

#Develop a simple real-time chat application where multiple clients can communicate with each other via a central server using sockets. 
#Messages sent by clients should be pickled before transmission. The server should receive pickled messages, unpickle them, and broadcast them to all connected clients.


#Requirements:
#Implement separate threads for handling client connections and message broadcasting on the server side.
#Ensure proper synchronization to handle concurrent access to shared resources (e.g., the list of connected clients).
#Allow clients to join and leave the chat room dynamically while maintaining active connections with other clients.
#Use pickling to serialize and deserialize messages exchanged between clients and the server.

import socket
import threading
from pickling import pickleIncomingData, unpickleData
from server import receive

HOST = '127.0.0.1'
PORT = 8888
clients = {}

def manageClientConnection(client_socket, client_address):
    """Function to handle communication with all clients connected to the server."""
    while True:
        try:
            clientData = receive(client_socket)
            if not clientData:
                break
            clientMessage = unpickleData(clientData)
            if clientMessage == 'exit':
                break
            clientBroadcast(client_socket, clientMessage)
        except Exception as err:
            print("Error:", err)
            break
    client_socket.close()

def clientBroadcast(cliSocket, receivedMessage):
    """Broadcasts a received message from a client to all the other connected clients."""
    clientSenderID = None
    for idOfClient, indvClient in clients.items():
        if indvClient == cliSocket:
            clientSenderID = idOfClient
            break
    for idOfClient, indvClient in clients.items():
        if indvClient != cliSocket:
            try:
                indvClient.send(pickleIncomingData(f"Client {clientSenderID}: {receivedMessage}"))
            except Exception as err:
                print("Error:", err)

def startChat(host, port):
    """Function to start the server and listen for clients for chatting."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print('Server started. Listening for connections...')

    while True:
        cliSocket, cliAddr = server_socket.accept()
        clients[cliAddr] = cliSocket

        print('Client connected:', cliAddr)

        cliThread = threading.Thread(target=manageClientConnection, args=(cliSocket, cliAddr))
        cliThread.start()

def main():
    startChat(HOST, PORT)

if __name__ == '__main__':
    main()
