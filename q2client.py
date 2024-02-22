#Distributed Task Queue with Pickling:

#Create a distributed task queue system where tasks are sent from a client to multiple worker nodes for processing using sockets. 
#Tasks can be any Python function that can be pickled. Implement both the client and worker nodes. 
#The client sends tasks (pickled Python functions and their arguments) to available worker nodes, and each worker node executes the task and returns the result to the client.

#Requirements:
#Implement a protocol for serializing and deserializing tasks using pickling.
#Handle task distribution, execution, and result retrieval in both the client and worker nodes.
#Ensure fault tolerance and scalability by handling connection errors, timeouts, and dynamic addition/removal of worker nodes.

from pickling import pickleIncomingData, unpickleData
from client import connectServ, send, receive, close

HOST = '127.0.0.1'
PORT = 8888

def send_task(task, HOST, PORT):
    """function to send tasks to connect to worker to send task"""
    try:
        with connectServ(HOST, PORT) as cliSocket:
            pickled_task = pickleIncomingData(task)
            if pickled_task:
                send(cliSocket, pickled_task)
            
            response = receive(cliSocket)
            if response:
                result = unpickleData(response)
                return result
            close(cliSocket)
    except Exception as err:
        print(f"Error when executing task: {err}")
        return None
    
def main():
    """executes functions"""
    task = {'function': 'multiply', 'args': (2, 3)}
    result = send_task(task, HOST, PORT)
    print(f"Worker result after function executed: {result}")

if __name__ == "__main__":
    main()


r"""
Data sent to Server!
Worker result after function executed: 6
"""