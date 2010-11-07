import time
from wx import *
from threading import *
import nio.interface

workerdone_event_type = NewEventType()
EVT_WORKERDONE = PyEventBinder(workerdone_event_type, 1)

def fake_thread():
    for i in range(10):
        time.sleep(1)


class WorkerDoneEvent(PyCommandEvent):

    def __init__(self, event_type, id, data):

        PyCommandEvent.__init__(self, event_type, id)
        self.data = data

class Worker(Thread):

    def __init__(self, callback_window, to_thread):
        
        Thread.__init__(self)
        self.callback_window = callback_window
        self.to_thread = to_thread
        #Disconnect PS only one connection per thread
        self.hllapi = nio.interface.WinHLLAPI()
        self.hllapi.disconnect()
        self.setDaemon(True)
        self.start()

    def run(self):
        
        self.to_thread()
        event = WorkerDoneEvent(workerdone_event_type, self.callback_window.GetId(), None)
        self.callback_window.GetEventHandler().ProcessEvent(event)
        #Disconnect PS only one connection per thread
        self.hllapi.disconnect()
        
