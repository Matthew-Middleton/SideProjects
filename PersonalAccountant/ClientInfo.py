#-------------------------------------------------------------------------------
# Name:        ClientInfo
# Purpose:     To store client info; needs encryption
#
# Author:      Matthew Middleton
#
# Created:     11/04/2018
# Copyright:   (c) Matthew Middleton 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class ClientInfo:
    def __init__(self, name='Client', account=00000000000, routing=000000000, total=0.0):
        self.__name = name
        self.__account = account
        self.__routing = routing
        self.__total = total
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_account(self, account):
        self.__account = account
    def get_account(self):
        return self.__account
    def set_routing(self, routing):
        self.__routing = routing
    def get_routing(self):
        return self.__routing
    def set_total(self, total):
        self.__total = total
    def get_total(self):
        return self.__total

