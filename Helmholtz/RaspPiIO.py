# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 19:19:49 2019

@author: Matthew Middleton
"""
import serial
import time

class RaspPiIO:
    #holds last instance of sort_input_lists() parameters
    data = []
    
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
            self.data.append(temp.isoformat(' '))
            temp = next(mag_x)
            self.data.append(str(temp))
            temp = next(mag_y)
            self.data.append(str(temp))
            temp = next(mag_z)
            self.data.append(str(temp))
        return
    
    """Writes data with UART TxD port on Raspery Pi"""
    def output_to_TxD(self, list_data = data):
        #NOTE: XOFF = 0x13
        #NOTE: XON = 0x11
        tx_size = 1
        #make a string to allow for floats, objects, and other types
        to_write = ' '.join(map(str, list_data))
        pi = serial.Serial(port="/dev/ttyAMA0", baudrate=9600, xonxoff=True)
        #wait for serial lines to open and sync up
        time.sleep(2)
        print(pi.name)
        #transmitting bytes
        while(tx_size):
            tx_size = pi.write(to_write)
            time.sleep(2)
        pi.close()
        return
    
    
    
    
