import pickle

def pickleIncomingData(data):
    """function to pickle data"""
    try:
        pickledData = pickle.dumps(data)
        return pickledData
    except Exception as err:
        print(f"Error while pickling: {err}")
        return None

def unpickleData(pickledData):
    """function to unpickle data"""
    try:
        unpickedData = pickle.loads(pickledData)
        return unpickedData
    except Exception as err:
        print(f"Error while unpickling: {err}")
        return None
