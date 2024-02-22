#Implement a client-server file transfer application where the client sends a file to the server using sockets. 
#Before transmitting the file, pickle the file object on the client side. On the server side, receive the pickled file object, unpickle it, and save it to disk.


#Requirements:
#The client should provide the file path of the file to be transferred.
#The server should specify the directory where the received file will be saved.
#Ensure error handling for file I/O operations, socket connections, and pickling/unpickling.

from pickling import unpickleData
from server import start, receive, close
import os

HOST = '127.0.0.1'
PORT = 8888
SAVEDIRECTORY = os.path.dirname(os.path.realpath(__file__))

def saveFileFromClient(clientFileData, SAVEDIRECTORY):
    """Unpickles data recieved from client then saves data into a new file called Question1ReceievedData.txt"""
    try:
        fileFromClient = SAVEDIRECTORY + "\\Question1RecievedData.txt"
        with open(fileFromClient, 'wb') as file:
            file.write(clientFileData)
            print(f"File saved at: {fileFromClient}")
    except Exception as err:
        print(f"Error: {err}")

def main():
    """In this case main is starting the server to listen for clients and then saving the data if sucessfully unpicked"""
    connection, socket = start(HOST, PORT)
    if connection is not None:
        clientFileData = receive(connection)
        if clientFileData:
            unpickledData = unpickleData(clientFileData)
            if unpickledData:
                saveFileFromClient(unpickledData, SAVEDIRECTORY)

    close(connection, socket)

if __name__ == "__main__":
    main()

r"""
Server listening for incoming connections...
Connection established with ('127.0.0.1', 63523)
File saved at: C:\Users\thedr\OneDrive\Documents\Python BTP405\Activity3\Question1RecievedData.txt
"""