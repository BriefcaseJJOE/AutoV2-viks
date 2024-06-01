from ReadWriteMemory import ReadWriteMemory
from reader_config import PROCESS_ID,BASE_ADDRESS,OFFSETS_X,OFFSETS_Y,OFFSETS_PETS
import ctypes


class Reader():
    """
    taking process id(PID) from task manager to identify which process 
    the func is reading 
    (using process by name maybe confusing if multiple process of the same app is
    running )
    configuration Via reader_config
    """
    def __init__(self) :
        self.rwm = ReadWriteMemory()
        self.process = self.rwm.get_process_by_id(PROCESS_ID)  #application's process iD
        self.base_address = BASE_ADDRESS
        self.process.open()         #open.() to open the process with query 
        
    def read_x(self):
        #process.read for reading value in PTR address
        #else it we return PTR addresss instead
        self.ptr_x = self.process.read(self.process.get_pointer(self.base_address,offsets=OFFSETS_X))
        signed_number = ctypes.c_long(self.ptr_x).value
        return signed_number


    def read_y(self):
        
        self.ptr_y = self.process.read(self.process.get_pointer(self.base_address,offsets=OFFSETS_Y))
        
        return self.ptr_y
    

    def read_pets(self):
        self.pets = self.process.read(self.process.get_pointer(self.base_address,offsets=OFFSETS_PETS))
        
        return self.pets
    
    def update(self):
        self.ptr_x = self.process.read(self.process.get_pointer(self.base_address,offsets=OFFSETS_X))
        signed_number = ctypes.c_long(self.ptr_x).value
        self.ptr_y = self.process.read(self.process.get_pointer(self.base_address,offsets=OFFSETS_Y))

        return [signed_number , self.ptr_y]