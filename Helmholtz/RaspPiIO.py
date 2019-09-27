# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 19:19:49 2019

@author: Matthew Middleton
"""
import wiringpi
from sys import getsizeof

class RaspPiIO:
    
    def __init__(self, data = []):
        self = self
        #holds last instance of sort_input_lists() data
        self.data = data
        #bytes in string representation of data
        self.data_size = 0
    
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
        #each set; the data of each element is to be considered a string
        for index in range(0, len(time_date), 1):
            #advances the iterator
            temp = next(dates)
            #makes a string object, in this case in ISO time format
            hold = temp.isoformat('T')
            #adds the size of the string hold and subtracts the base size of
            #a string object
            self.data_size += getsizeof(hold) - getsizeof('')
            #adds the string to the list
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
    def output_to_TxD(self, list_data = list):
        #make a string to allow for multiple data types(strings, int, and float)
        to_write = ' '.join(map(str, list_data))
        wiringpi.wiringPiSetup()
        #opens the Raspberry Pi's UART port, w/ a data transfer rate of
        #115200 bits/s
        serial = wiringpi.serialOpen('/dev/ttyS0', 115200)
        #write the string data, as ascii, to the Raspberry Pi
        wiringpi.serialPuts(serial, to_write.encode('ascii'))
        #closes the serial port
        wiringpi.serialClose(serial)
        return
    
    
    
"""send string of each list, start bits, bits for flag sigaling x,y, or z, stop bits"""
