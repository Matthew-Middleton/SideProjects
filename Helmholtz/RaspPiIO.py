# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 19:19:49 2019
@author: Matthew Middleton
"""
import serial
from sys import getsizeof
import time

class RaspPiIO:
    #holds last instance of sort_input_lists() data
    data = []
    #bytes in string representation of data
    data_size = 0
    
    def __init__(self, data = []):
        self = self
        self.data = data
    
    """Creates a list by placing all indeces from lists next to each
    other"""
    def sort_input_lists(self, time_date = list, mag_field_x = list,
                        mag_field_y = list, mag_field_z = list):
        #resets data and data_size to empty
        self.data = []
        
        #create iterables for each list
        dates = iter(time_date)
        mag_x = iter(mag_field_x)
        mag_y = iter(mag_field_y)
        mag_z = iter(mag_field_y)
        #iterate through all items in the lists assuming they're of
        #the same size. Also, captures the total byte count of elements w/in
        #each set
        for index in range(0, len(time_date), 1):
            temp = next(dates)
            hold = temp.isoformat(' ')
            self.data_size += getsizeof(hold) - getsizeof('')
            self.data.append(hold)
            
            temp = next(mag_x)
            hold = str(temp)
            self.data_size += getsizeof(hold) - getsizeof('')
            self.data.append(hold)
            
            temp = next(mag_y)
            hold = str(temp)
            self.data_size += getsizeof(hold) - getsizeof('')
            self.data.append(hold)
            
            temp = next(mag_z)
            hold = str(temp)
            self.data_size += getsizeof(hold) - getsizeof('')
            self.data.append(hold)
        return
    
    """Writes data with UART TxD port on Raspery Pi"""
    def output_to_TxD(self, list_data = data):
        #NOTE: XOFF = 0x13
        #NOTE: XON = 0x11
        tx_size = 1
        #make a string to allow for floats, objects, and other types
        to_write = ' '.join(map(str, list_data))
        #opens port to Raspberry Pi's serial IO port(Tx,Rx)
        pi = serial.Serial(port="/dev/ttyAMA0", baudrate=9600, xonxoff=True)
        time.sleep(2)
        print(pi.name)
        tx_size = pi.write(to_write.encode(encoding = 'ascii'))
        print("Total size written to pi_boi is {}".format(tx_size))
        time.sleep(2)
        pi.close()
        return
      
