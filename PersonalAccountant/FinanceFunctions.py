#-------------------------------------------------------------------------------
# Name:        FinanceFunctions
# Purpose:     To model a personal accountant and manage personal finances.
#              no security is being planned for implementation currently
#
# Author:      Matthew Middleton
#
# Created:     11/04/2018
# Copyright:   (c) Matthew Middleton 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class FinanceFunctions:

    def __init__(self):
        self.data = []

    def getBankInfo(self,filename=''):
    #To get bank info from a file
        fileCopy = []
        try:
            file = open(name, 'r')
            for inst in file:
                fileCopy.append(inst)
        except IOError:
            print("Error accessing",self.filename)
        return fileCopy

    def setBankInfo(self, name=''):
        #Take new(initial) bank info and make a file out of it
