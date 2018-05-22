#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Copyright 2018(c). All rights reserved.
#
# This is free software; you can do what the LICENCE file allows you to.
# Author: Ing. Oraldo Jacinto Simon

import sys
sys.path.append('/home/oraldo/src/maestria/ISW/Programa1/Code')
from listaSE import ListSE
import math

class CalculateRelativeSize(object):
    '''Calculate relative size ranges for very small, small, medium, large, and
    'and very large ranges using standard deviation of an assumed log-normal'
    'distribution of sizes.'

    '''


    def __init__(self):
        fichero = open("history.txt", "r")
        # Build a dictionary that contains the input tables
        history = [eval(line.replace('/n', '')) for line in fichero.readlines()]
        # Storing in a list of lists the tables where each record is a list
        items_tabla1 = history[0]['table1']
        items_tabla2 = history[1]['table2']
        fichero.close()
        self.tables = []
        self.t_names = ['LOC/Method', 'Pgs/Chapter']
        self.table1 = ListSE()
        self.table2 = ListSE()
        # Storing each table in a ListSE.
        for record in items_tabla1:
            self.table1.insertNodeLast(record)
        for record in items_tabla2:
            self.table2.insertNodeLast(record)
        self.tables.append(self.table1)
        self.tables.append(self.table2)


    def calculate_standard_desviation(self, ListaSE):
        '''Returns a dictionary with the initial parameters for the calculation:

        '''
        name = ''
        Xi = 0
        ln_Xi = 0
        list_loc_lnXi = []
        avg = 0
        standar_deviation = 0
        total_lnXi = 0
        square_ln_avg = 0
        total_square = 0
        standard_desviation = 0
        n = 0
        iterator = True
        if ListaSE:
            temp = ListaSE.getFirst()
            while (iterator):
                if len(temp.getElement()) == 3:
                    name, size, count_method = temp.getElement()
                    size = float(size)
                    Xi = size/count_method
                else:
                    name, pages = temp.getElement()
                    Xi = float(pages)
                ln_Xi = math.log(Xi)
                total_lnXi += ln_Xi
                n +=1
                list_loc_lnXi.append([n, name, Xi, ln_Xi])
                if temp == ListaSE.getLast():
                    iterator = False
                else:
                    temp = ListaSE.nextElement(temp)
            avg = total_lnXi / n
            for item in list_loc_lnXi:
                count, name, loc, lnXi = item
                square_ln_avg = math.pow((lnXi- avg), 2)
                total_square += square_ln_avg
                item.append(square_ln_avg)
            standard_desviation = math.sqrt(total_square/(n-1))
            return dict(
                values=list_loc_lnXi,
                total_lnXi=total_lnXi,
                total_square=total_square,
                avg=avg,
                standard_desviation = standard_desviation,
                n=n)

    def calculate_log_range(self, ListaSE):
        '''Calculate the logarithmic ranges:

        '''
        ln_VS = 0
        ln_S = 0
        ln_M = 0
        ln_L = 0
        ln_VL = 0
        values = self.calculate_standard_desviation(ListaSE)
        standard_desviation = values['standard_desviation']
        avg = values['avg']
        n = values['n']
        ln_VS = avg - (2*standard_desviation)
        ln_S = avg - standard_desviation
        ln_M = avg
        ln_L = avg + standard_desviation
        ln_VL = avg + (2*standard_desviation)
        return dict(ln_VS=ln_VS, ln_S=ln_S, ln_M=ln_M, ln_L=ln_L, ln_VL=ln_VL)

    def calculate_antilog(self, ListaSE):
        '''Convert the natural log values back to their original form by calculating
        'the anti-logarithm by calculating e to the power of the log value to'
        'determine the midpoints of the size ranges'

        '''
        VS = 0
        S = 0
        M = 0
        L = 0
        VL = 0
        values = self.calculate_log_range(ListaSE)
        e = math.e
        VS = round(math.pow(e, values['ln_VS']), 4)
        S = round(math.pow(e, values['ln_S']), 4)
        M = round(math.pow(e, values['ln_M']), 4)
        L = round(math.pow(e, values['ln_L']), 4)
        VL = round(math.pow(e, values['ln_VL']), 4)
        return dict(VS=VS, S=S, M=M, L=L, VL=VL)


    def get_relative_size_ranges(self):
        '''Return a dict() with relative_size_ranges

        '''
        result = []
        for index in range(0, len(self.t_names)):
            values = []
            values.append(self.t_names[index])
            relatives = self.calculate_antilog(self.tables[index])
            values.append(relatives['VS'])
            values.append(relatives['S'])
            values.append(relatives['M'])
            values.append(relatives['L'])
            values.append(relatives['VL'])
            result.append(values)
        return result
