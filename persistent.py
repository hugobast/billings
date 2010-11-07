import pickle

def Batch():

    try:
        batch = pickle.Unpickler(open('batch.p', 'rb')).load()
    except:
        return None
    return batch
