#Real-Time Chat Application with Pickling:

#Develop a simple real-time chat application where multiple clients can communicate with each other via a central server using sockets. 
#Messages sent by clients should be pickled before transmission. The server should receive pickled messages, unpickle them, and broadcast them to all connected clients.


#Requirements:
#Implement separate threads for handling client connections and message broadcasting on the server side.
#Ensure proper synchronization to handle concurrent access to shared resources (e.g., the list of connected clients).
#Allow clients to join and leave the chat room dynamically while maintaining active connections with other clients.
#Use pickling to serialize and deserialize messages exchanged between clients and the server.

import threading
from pickling import pickleIncomingData, unpickleData
from client import connectServ, send, receive

HOST = '127.0.0.1'
PORT = 8888

def receive_messages(cliSocket):
    """function to receive messages from server"""
    while True:
        try:
            messageData = receive(cliSocket)
            if not messageData:
                break
            messageFromServer = unpickleData(messageData)
            print(messageFromServer)
        except Exception as err:
            print("Error:", err)
            break

def send_messages(cliSocket):
    """function to send messages to server"""
    while True:
        try:
            messageToServer = input()
            send(cliSocket, pickleIncomingData(messageToServer))
            if messageToServer == 'exit':
                break
        except Exception as err:
            print("Error:", err)
            break

def start_client(host, port):
    """function to start connect to server as well as threading"""
    cliSocket = connectServ(host, port)
    if cliSocket is None:
        return

    receive_thread = threading.Thread(target=receive_messages, args=(cliSocket,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(cliSocket,))
    send_thread.start()

def main():
    start_client(HOST, PORT)

if __name__ == '__main__':
    main()
