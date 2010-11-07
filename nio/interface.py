import ctypes
import struct
import time
import thread


CONNECTPS = 1
DISCONNECTPS =2
SENDKEY =3
WAIT =4
COPYPS =5
SEARCHPS =6
COPYPSTOSTR =8
SETSESSIONPARAMETERS =9
QUERYSESSIONS = 10
COPYOIA = 13
COPYSTRTOPS = 15
QUERYSESSIONSTATUS = 22
ENTER = '@E'
NEXTPAGE = '@8'
NEXT = '@b'
SEARCH = '@6'
CLEAR = '@5'
SAVE = '@9'


class MonoState(object):
    
    mono_state = {}
    def __init__(self):
        self.__dict__ = self.mono_state

class Singleton(object):

    def __new__(type):
        if not '_instance' in type.__dict__:
            type._instance = object.__new__(type)
        return type._instance

class ThreadedSingleton(object):
    
    __lock_object = thread.allocate_lock()
    __instance = None

    def __new__(cls, *args, **kwargs):

        cls.__lock_object.acquire()
        if not cls.__instance or type(cls.__instance) != cls:
            time.sleep(5)
            cls.__instance = object.__new__(cls, *args, **kwargs)
        cls.__lock_object.release()
        return cls.__instance

    def destroy(self):
        ThreadedSingleton.__instance = None
    

class WinHLLAPI(Singleton):
  
    def __init__(self):
    
        self.is_connected = False
        self._whlla = ctypes.windll.whlapi32.WinHLLAPI
    
    def connect(self):
        self.query_sessions()
        ret = self.call(CONNECTPS, self._session_id, 1)['ret'].value
        if ret != 0:
            self.is_connected = False
            print 'Error connection!'
        else:
            self.is_connected = True
            self.ps = self.get_ps()
            print 'Connected.'
  
    def disconnect(self):
        if self.call(DISCONNECTPS)['ret'].value != 0:
            print 'Error disconnection!'
        else:
            self.is_connected = False
            print 'Disconnected.'

    def get_ps(self):
        if not self.is_connected:
            self.connect()
        return self.call(COPYPS, "", self._row * self._col)['dat'].value

    def set_text(self, text, pos):
        if not self.is_connected:
            self.connect()
        position = self.convert_position(pos[0], pos[1])
        self.call(COPYSTRTOPS, text, len(text), position)

    def get_text(self, pos):
        if not self.is_connected:
            self.connect()
        position = self.convert_position(pos[0], pos[1]) - 1
        return self.ps[position:position + pos[2]]
        
    def wait(self):
        if not self.is_connected:
            self.connect()
            self.call(WAIT)

    def command(self, key_code):

        if not self.is_connected:
            self.connect()
        initial_state = self.copy_oia()[:75]
        self.call(SENDKEY, key_code, len(key_code))

        while initial_state != self.copy_oia()[:75]:
            time.sleep(0.05)

        self.ps = self.get_ps()

    def query_sessions(self):
    
        result = self.call(QUERYSESSIONS, "", 288)['dat']
        self._size = struct.unpack('h', result[10:12])[0]
        self._session_id = chr(ord(result[1]))
        if self._size == 1920:
            self._row, self._col = (24, 80)

    def copy_oia(self):
        if not self.is_connected:
            self.connect()
        return self.call(COPYOIA, "", 103)['dat'].value

    def convert_position(self, row, col):
        if not self.is_connected:
            self.connect()
        return self._col * (row - 1) + col
 
    def call(self, function, data = "", length = 0, position = 0):
    
        fun = ctypes.c_int(function)
        lng = ctypes.c_int(length)
        pos = ctypes.c_int(position)
        dat = ctypes.create_string_buffer(data, length)
            
        self._whlla(ctypes.byref(fun), dat, ctypes.byref(lng), ctypes.byref(pos))
        return {'fun': fun, 'dat': dat, 'lng': lng, 'ret': pos}

