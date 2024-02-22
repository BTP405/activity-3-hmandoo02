import socket

def start(host, port):
    """function to start the server when it is listening for clients"""
    try:
        serSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serSocket.bind((host, port))
        serSocket.listen(1)
        print("Server listening for incoming connections...")

        conn, address = serSocket.accept()
        print(f"Connection established with {address}")

        return conn, serSocket

    except Exception as err:
        print(f"Error when starting server: {err}")
        return None, None

def receive(connection):
    """function to recieve data from client"""
    try:
        clientData = connection.recv(4096)
        return clientData
    except Exception as err:
        print(f"Error when recieving data: {err}")
        return None

def send(connection, data):
    """function to send data to server"""
    try:
        connection.sendall(data)
        print("Data sent to Client!")
    except Exception as err:
        print(f"Error sending data: {err}")


def close(conn, server_socket):
    """function to start the server when it is listening for clients"""
    try:
        conn.close()
        server_socket.close()
    except Exception as err:
        print(f"Error during closing: {err}")
