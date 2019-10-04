# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 19:19:49 2019

@author: Matthew Middleton
"""
#import wiringpi
from sys import getsizeof

class RaspPiIO:
    
    def __init__(self):
        self = self
        #number of bytes in string representation of data
        self.__data_size = 0
    
    """Creates a list by placing all indeces from lists next to each
    other, returning said list whose elements are string represenations of the
    data"""
    def sort_input_lists(self, time_date, mag_field_x,
                        mag_field_y, mag_field_z):
        self.__data_size = 0;
        td_str = ''
        mag_x_str = ''
        mag_y_str = ''
        mag_z_str = ''
        #create iterables for each list
        dates = iter(time_date)
        mag_x = iter(mag_field_x)
        mag_y = iter(mag_field_y)
        mag_z = iter(mag_field_z)
        #iterate through all items in the lists assuming they're of
        #the same size. Also, captures the total byte count of elements w/in
        #each set; the data of each element is to be considered a string
        for index in range(0, len(time_date), 1):
            #advances the iterator
            temp = next(dates)
            #makes a string object, in this case in ISO time format
            hold = temp.isoformat('T')
            #adds the size of the string hold and subtracts the base size of
            #a string object, then adds 1 for the space
            self.__data_size += getsizeof(hold) - getsizeof('') + 1
            #concatenates iso format datetime object to string, then adds
            #a space
            td_str += hold
            td_str += ' '
            
            temp = next(mag_x)
            print(temp)
            hold = str(temp)
            self.__data_size += getsizeof(hold) - getsizeof('') + 1
            mag_x_str += hold
            mag_x_str += ' '
            
            temp = next(mag_y)
            print(temp)
            hold = str(temp)
            self.__data_size += getsizeof(hold) - getsizeof('') + 1
            mag_y_str += hold
            mag_y_str += ' '
            #z data takes on y data for some reason
            temp = next(mag_z)
            print(temp)
            hold = str(temp)
            self.__data_size += getsizeof(hold) - getsizeof('') + 1
            mag_z_str += hold
            mag_z_str += ' '
            
        #create an array where each index holds a string
        str_list = []
        str_list.append(td_str)
        str_list.append(mag_x_str)
        str_list.append(mag_y_str)
        str_list.append(mag_z_str)
        return str_list
    
    """Writes data with UART TxD port on Raspery Pi"""
    def output_to_TxD(self, time_date = str, mag_field_x = str, mag_gield_y =str):
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
    
    #getter for data size
    def data_size(self):
        return self.__data_size
    
        
        
        
        
"""send string of each list, start bits, bits for flag sigaling x,y, or z, stop bits"""
