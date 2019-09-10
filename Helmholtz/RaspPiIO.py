# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 19:19:49 2019

@author: Matthew Middleton
"""
import datetime
import array

class RaspPiIO:
    def __init__(self):
        self = self
        
    def sortInputArrays(timedate = [], mag_field_x = [],
                        mag_field_y = [], mag_field_z = []):
        
        return

    """makes the list, items, heap ordered
    for implementing heap sort"""
    def heapify(self, items, size = int, index = int):
        
        largest = index
        left = 2*index+1 #left child node
        right = 2*index+2 #right child node
        #left child exists and is greater than current root
        if(left<size and items[index]<items[left]):
            largest = left
        #right child exists and is greater than root
        if(right<size and items[largest]<items[right]):
            largest = right
        #child, left or right, is greater than parent
        if(largest>index):
        #swap child node with parent node
            items[index], items[largest] = items[largest], items[index]
            #heapify the root
            self.heapify(items, size, largest)
        return 

    def heap_sort(self, items):
        size = len(items)
        for i in range(size, -1, -1):
            self.heapify(items, size, i)
            
        for i in range(size-1, 0, -1):
            items[i], items[0] = items[0], items[i]
            self.heapify(items, i, 0)
        return
    

        