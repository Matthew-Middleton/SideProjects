# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 19:19:49 2019

@author: Matthew Middleton
"""
#import wiringpi
from sys import getsizeof
from time import sleep
import wiringpi

class RaspPiIO:
    
    def __init__(self):
        self = self
        #number of bytes in string representation of data
        self.__data_size = 0
    
    """Creates a list from the given lists and calculates the increment between
    each data point by the test time, time_to_run.
    Return: a list whose first index is the test time increment, delta_t
            it's second index is the string of mag_field_x
            third index is the string of mag_field_y
            fourth index is the string of mag_field_z"""
    def sort_input_lists(self, time_to_run = int, mag_field_x = list,
                        mag_field_y = list, mag_field_z = list):
        
        self.__data_size = 0
        #calculates delta_t: delta_t is the time by which each test should be
        #run for based of the total number of data_points-1
        #we chose data_points-1 to account for starting at time=0
        delta_t = time_to_run/(len(mag_field_x)-1)
        
        #makes a string out of each data list and adds the number of bytes to 
        #a field which can be accessed later via a getter, data_size()
        mag_x_str = ' '.join(map(str, mag_field_x))
        self.__data_size += getsizeof(mag_x_str) - getsizeof('')
        
        mag_y_str = ' '.join(map(str, mag_field_y))
        self.__data_size += getsizeof(mag_y_str) - getsizeof('')
        
        mag_z_str = ' '.join(map(str, mag_field_z))
        self.__data_size += getsizeof(mag_z_str) - getsizeof('')
        
        #create an array where each index holds a string
        str_list = []
        str_list.append(str(delta_t))
        str_list.append(mag_x_str)
        str_list.append(mag_y_str)
        str_list.append(mag_z_str)
        return str_list
    
    """Writes data with UART TxD port on Raspery Pi
        '~' signals that the data is starting transmission
        '/' signals that the next data is being sent
        '!' signals that the data is stopping transmission"""
    def output_to_TxD(self, data = list):
        #make a string to allow for multiple data types(strings, int, and float)
        
        wiringpi.wiringPiSetup()
        #opens the Raspberry Pi's UART port, w/ a data transfer rate of
        #115200 bits/s
        serial = wiringpi.serialOpen('/dev/ttyS0', 115200)
        #sleep a few seconds to make sure the port opens and sets connections
        #properly
        sleep(2)
        #signals to start data transmission, uses char 1
        wiringpi.serialPuts(serial, chr(1).encode('ascii'))
        wiringpi.serialPuts(serial, data[0].encode('ascii'))
        for index in range(1, len(data), 1):
            #signals that the next data is being sent, uses char 2
            wiringpi.serialPuts(serial, chr(2).encode('ascii'))
            #write the string data, as ascii, to the Raspberry Pi
            wiringpi.serialPuts(serial, data[index].encode('ascii'))
        #signals that data transmission is ending, uses char 4
        wiringpi.serialPuts(serial, chr(4).encode('ascii'))
        #closes the serial port
        wiringpi.serialClose(serial)
        return
    
    #getter for data size
    def data_size(self):
        return self.__data_size
       
"""send string of each list, start bits, bits for flag sigaling x,y, or z, stop bits 
10 min long period scale down time date to 10 min ~35 ms ignore date, 
use time granularity of 6 (6 digits after 0)""" 
