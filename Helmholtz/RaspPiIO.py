# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 19:19:49 2019

@author: Matthew Middleton
"""
from datetime import datetime
import serial

class RaspPiIO:
    def __init__(self):
        self = self
    
    def sort_input_lists(self, timedate = list, mag_field_x = list,
                        mag_field_y = list, mag_field_z = list):
        #to retrieve timedate as unix time use: 
        #datetime.fromtimestamp(timedate[i]) were i 
        #is the index you wish to access
        timedate.sort()
        mag_field_x.sort()
        mag_field_y.sort()
        mag_field_z.sort()
        data_list = list(timedate)
        data_list.append(mag_field_x)
        data_list.append(mag_field_y)
        data_list.append(mag_field_z)
        return data_list

    def output_from_TxD(self, timedate = list, mag_field_x = list,
                        mag_field_y = list, mag_field_z = list):
        #to use 
        port = serial.Serial("/dev/ttyAMA0", baudrate=9600)
        return
        
