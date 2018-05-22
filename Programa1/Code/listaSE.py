#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Copyright 2018(c). All rights reserved.
#
# This is free software; you can do what the LICENCE file allows you to.
# Author: Ing. Oraldo Jacinto Simon

from node import Node

class ListSE(object):
    '''A simply linked list is a set of zero or more nodes:
    'It has two attributes or labels, node first, last node'
    'Every listSE: The first node equal to the last one and this must be None'

    '''
    def __init__(self):
        # First element
        self.__first = None
        # Last element
        self.__last = None

    def getEmpty(self):
        '''Return true if the list has elements

        '''
        if self.__first == None:
            return True

    def getFirst(self):
        '''Get the first element

        '''
        if self.getEmpty():
            print ('Empty List')
        else:
            return self.__first

    def printFirst(self):
        '''Print the first element in the list

        '''
        element = self.getFirst()
        if element is not None:
            print (element.getElement())

    def getLast(self):
        '''Get the last element

        '''
        if self.getEmpty():
            print ('Empty List')
        else:
            return self.__last

    def nextElement(self, element):
        '''Return the next element

        '''
        return element.__next

    def printLast(self):
        '''Print the last element in the list

        '''
        element = self.getLast()
        if element is not None:
            print (element.getElement())


    def insertNodeStart(self, element):
        '''Insert a node at the top of the list

        '''
        new_element = Node(element)
        if self.getEmpty():
            self.__first = self.__last = new_element
        else:
            new_element.__next = self.__first
            self.__first = new_element

    def insertNodeLast(self, element):
        '''Insert a node at the end of the list

        '''
        new_element = Node(element)
        if self.getEmpty():
            self.__first = self.__last = new_element
        else:
            self.__last.__next = new_element
            self.__last = new_element

    def removeTheOne(self):
        '''Remove the one

        '''
        self.__first = None
        self.__last = None
        print ('Item removed now the list is empty')
        return True


    def removeFirst(self):
        '''Remove the first element's list

        '''
        if self.getEmpty():
            print ('Empty list is impossible to eliminate')
        elif self.__first == self.__last:
            self.removeTheOne()
        else:
            temp = self.__first
            self.__first = self.__first.__next
            temo = None
            print ('The first element has been removed')

    def romoveLast(self):
        '''Remove the last element's list

        '''
        if self.Empty():
            print ('Empty list is impossible to eliminate')
        elif self.__first == self.__last:
           self.removeTheOne()
        else:
            iterator = True
            temp = self.__first
            while(iterator):
                if temp.__next == self.__last:
                    temp2 = self.__last
                    self.__last = temp
                    temp2 = None
                    iterator = False
                    print ('The last element has been removed')
                else:
                    temp = temp.__next

    def printAllElements(self):
        '''Print all elements in the list

        '''
        if self.getEmpty():
            print ('Empty list')
        else:
            iterator = True
            temp = self.__first
            while(iterator):
                print (temp.getElement())
                if temp == self.__last:
                    iterator = False
                else:
                    temp = temp.__next
