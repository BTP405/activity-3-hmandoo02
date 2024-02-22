#Distributed Task Queue with Pickling:

#Create a distributed task queue system where tasks are sent from a client to multiple worker nodes for processing using sockets. 
#Tasks can be any Python function that can be pickled. Implement both the client and worker nodes. 
#The client sends tasks (pickled Python functions and their arguments) to available worker nodes, and each worker node executes the task and returns the result to the client.

#Requirements:
#Implement a protocol for serializing and deserializing tasks using pickling.
#Handle task distribution, execution, and result retrieval in both the client and worker nodes.
#Ensure fault tolerance and scalability by handling connection errors, timeouts, and dynamic addition/removal of worker nodes.

from pickling import pickleIncomingData, unpickleData
from server import start, receive, send, close

HOST = '127.0.0.1'
PORT = 8888

def multiply(num1, num2):
    """Multiply 2 numbers"""
    return num1 * num2

def executeWorkerTask(task):
    """function to execute function and return result of function"""
    try:
        function_name = task['function']
        args = task['args']
        functionResult = globals()[function_name](*args)
        return functionResult
    except Exception as err:
        print(f"Error when executing task: {err}")
        return None

def main():
    """recieves data from client to put into function then executes function then sends back to client"""
    connection, server_socket = start(HOST, PORT)
    if connection is not None:
        dataFromClient = receive(connection)
        if dataFromClient:
            unpickedTask = unpickleData(dataFromClient)
            if unpickedTask:
                functionResult = executeWorkerTask(unpickedTask)
                pickledFunctionResult = pickleIncomingData(functionResult)
                if pickledFunctionResult:
                    send(connection, pickledFunctionResult)

    close(connection, server_socket)

if __name__ == "__main__":
    main()


r"""
Server listening for incoming connections...
Connection established with ('127.0.0.1', 50093)
Data sent to Client!
"""
