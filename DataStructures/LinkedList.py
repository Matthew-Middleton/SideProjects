#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Matthew Middleton
#
# Created:     18/04/2018
# Copyright:   (c) Matthew Middleton 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class Node:
    def __init__(self, element):
        self.element = element
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self,element):
        """Appends the given element to the end of the list"""
        node = Node(element)
        if self.head is None:
            self.head = node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = node
        return

    def place(self, prev_node, element):
        """Sets the element after the given node"""
        if(prev_node is None):
            print("Previous node is None")
        node = Node(element)
        node.next = prev_node.next
        prev_node.next = node
        return

    def push(self, element):
        """Sets the element at the head of the list"""
        node = Node(element)
        node.next = self.head
        self.head = node
        return

    def length(self):
        """Returns the size of the list"""
        node = self.head
        x = 0
        while(node):
            node = node.next
            x += 1
        return x

    def printList(self):
        """Prints the elements in the list from head to tail"""
        node = self.head
        while(node):
            print(node.element)
            node = node.next
#while(node) is equivalent to while(node is not None)
