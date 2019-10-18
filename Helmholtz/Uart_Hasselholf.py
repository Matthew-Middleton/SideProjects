# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 19:19:49 2019
Updated on Wed Oct 9 17:43:59 2019
@author: Matthew Middleton
"""
import wiringpi
from time import sleep

class UartHasselholf:
    
    def __init__(self):
        self = self
    
    """Creates a list from the given lists and calculates the increment between
    each data point by the test time, time_to_run.
    Return: a list whose first index is the test time increment, delta_t
            it's second index is the string of mag_field_x
            third index is the string of mag_field_y
            fourth index is the string of mag_field_z"""
    def sort_input_lists(self, time_to_run = float, mag_field_x = list,
                        mag_field_y = list, mag_field_z = list):
        list_length = len(mag_field_x)
        #calculates delta_t: delta_t is the time by which each test should be
        #run for based of the total number of data_points-1
        #we chose data_points-1 to account for starting at time=0
        delta_t = float(time_to_run)/(list_length-1)
        mag_x_str = ''
        mag_y_str = ''
        mag_z_str = ''
        #makes a string out of each data list where each data value
        #has a precision of 6
        for index in range(0, list_length, 1):
            mag_x_str += '{:.6f}'.format(mag_field_x[index])
            mag_x_str += ' '
            mag_y_str += '{:.6f}'.format(mag_field_y[index])
            mag_y_str += ' '
            mag_z_str += '{:.6f}'.format(mag_field_z[index])
            mag_z_str += ' '
        
        #create an array where each index holds a string
        str_list = []
        str_list.append('{0:.6f}'.format(delta_t))
        str_list.append(mag_x_str)
        str_list.append(mag_y_str)
        str_list.append(mag_z_str)
        return str_list
    
    """Writes data with UART TxD port on Raspery Pi
        ascii 1 signals that the data is starting transmission
        ascii 2 signals that the next data is being sent
        ascii 4 signals that the data is stopping transmission"""
    def output_to_MC(self, data = list):
        
        wiringpi.wiringPiSetup()
        #opens the Raspberry Pi's UART port, w/ a data transfer rate of
        #115200 bits/s
        serial = wiringpi.serialOpen('/dev/ttyS0', 115200)
        #sleep a few seconds to make sure the port opens and sets connections
        #properly
        sleep(2)
       #signals to start data transmission, uses start of header char
        wiringpi.serialPuts(serial, chr(1).encode('ascii'))
        wiringpi.serialPuts(serial, data[0].encode('ascii'))
        for index in range(1, len(data), 1):
            #signals that the next data is being sent, uses start of text char
            wiringpi.serialPuts(serial, chr(2).encode('ascii'))
            #write the string data, as ascii, to the Raspberry Pi
            wiringpi.serialPuts(serial, data[index].encode('ascii'))
        #signals that data transmission is ending, uses end of transmission char
        wiringpi.serialPuts(serial, chr(4).encode('ascii'))
        #closes the serial port
        wiringpi.serialClose(serial)
        return
    
