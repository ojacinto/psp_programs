#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Copyright 2018(c). All rights reserved.
#
# This is free software; you can do what the LICENCE file allows you to.
# Author: Ing. Oraldo Jacinto Simon

class Node(object):
    '''A node is a object with:
    'One or more attributes (your elements)'
    'An additional attribute: Pointer to next equal to Null or None'

    '''
    def __init__(self, element):
        # Attribute's node
        self.__element = element
        # Pointer that will join the nodes
        self.__next = None

    def getElement(self):
        '''Get element's node

        '''
        return self.__element
