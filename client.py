import socket   

def connectServ(host, port):
    """function to connect to server when it is listening for clients"""
    try:
        cliSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliSocket.connect((host, port))
        return cliSocket
    except Exception as err:
        print(f"Error when connecting to server: {err}")
        return None

def send(cliSocket, data):
    """function to send data to server"""
    try:
        cliSocket.sendall(data)
        print("Data sent to Server!")
    except Exception as err:
        print(f"Error sending data: {err}")

def receive(cliSocket):
    try:
        serverData = cliSocket.recv(4096)
        return serverData
    except Exception as err:
        print(f"Error when recieving data: {err}")
        return None

def close(cliSocket):
    """function to close connection to server"""
    try:
        cliSocket.close()
    except Exception as err:
        print(f"Error during closing: {err}")
