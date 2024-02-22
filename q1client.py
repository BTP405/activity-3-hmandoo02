#Implement a client-server file transfer application where the client sends a file to the server using sockets. 
#Before transmitting the file, pickle the file object on the client side. On the server side, receive the pickled file object, unpickle it, and save it to disk.


#Requirements:
#The client should provide the file path of the file to be transferred.
#The server should specify the directory where the received file will be saved.
#Ensure error handling for file I/O operations, socket connections, and pickling/unpickling.

from pickling import pickleIncomingData
from client import connectServ, send, close

HOST = '127.0.0.1'
PORT = 8888

def sendFileToServer(path, server_address, server_port):
    """function to send specified file to the server"""
    try:
        with connectServ(server_address, server_port) as socket:
            with open(path, 'rb') as file:
                clientFileData = file.read()
                pickledData = pickleIncomingData(clientFileData)

            if pickledData:
                send(socket, pickledData)
        close(socket)
    except Exception as err:
        print(f"An error occurred: {err}")


def main():
    """asking user to enter file path for file then sending to server"""
    path = input("Enter the file path: ")
    sendFileToServer(path, HOST, PORT)

if __name__ == "__main__":
    main()

r"""
Enter the file path: C://Users//thedr//OneDrive//Documents//Python BTP405//Activity3//Question1Test.txt
Data sent to Server!

"""