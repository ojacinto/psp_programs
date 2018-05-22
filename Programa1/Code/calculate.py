#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Copyright 2018(c). All rights reserved.
#
# This is free software; you can do what the LICENCE file allows you to.
# Author: Ing. Oraldo Jacinto Simon

from listaSE import ListSE
import math

class CalculateAveraging(object):
    '''Calculate the averaging and the standard deviation of the list of
    numbers loaded from the file `numeros.txt`'

    '''

    def __init__(self):
        # Attribute's node
        fichero = open("numeros2.txt", "r")
        result = fichero.read()
        cadena = result.split('\n')
        fichero.close()
        # Remove the last element ''
        cadena.pop()
        numeros = ListSE()
        # Insert each number as an element of the ListSE.
        for element in cadena:
            numeros.insertNodeLast(float(element))
        self.numeros = numeros

    def get_avg(self):
        '''Get the average of all the elements in the list

        '''
        iterator = True
        values = {}
        total = 0
        n = 0
        temp = self.numeros.getFirst()
        while(iterator):
            total += temp.getElement()
            n += 1
            values[n] = temp.getElement()
            if temp == self.numeros.getLast():
                iterator = False
            else:
                temp = self.numeros.nextElement(temp)
            avg = total / n
        return {'values': values, 'count': n,'total': total, 'avg': avg}

    def get_standard_desviation(self):
        '''Get intermediate values

        '''
        result = self.get_avg()
        avg = result['avg']
        count = result['count']
        n = result['count']- 1
        list_values = []
        inter_values = {}
        count = 0
        total_inter = 0
        for index, value in result['values'].items():
            intermediate = math.pow((avg-value),2)
            count += 1
            list_values.append([count, value, intermediate])
            total_inter += intermediate
        inter_values['values'] = list_values
        inter_values['count'] = count
        inter_values['summation'] = result['total']
        inter_values['avg'] = round(avg, 3)
        inter_values['total_intermediate'] = round(total_inter, 3)
        inter_values['standard_desviation'] = round(math.sqrt(total_inter/n), 2)
        return inter_values
