#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Copyright 2018(c). All rights reserved.
#
# This is free software; you can do what the LICENCE file allows you to.
# Author: Ing. Oraldo Jacinto Simon

import sys
sys.path.append('/home/oraldo/src/maestria/ISW/Programa1/Code')
sys.path.append('/home/oraldo/src/maestria/ISW/Programa5/Code')
from listaSE import ListSE
from calculatep import CalculateIntegrateSimpsonRule as Calculate
import math

class Searchtdistribution(object):
    '''Find the value of t for which integrating the Student’s t -distribution
    'probability density function from 0 to t gives a result of p.'

    '''


    def __init__(self, url):
        fichero = open(url, "r")
        # Build a dictionary that contains the input tables
        history = [eval(line.replace('/n', '')) for line in fichero.readlines()]
        fichero.close()
        self.values_table = ListSE()
        # Storing values in a ListSE.
        for record in history:
            self.values_table.insertNodeLast(record)
        self.cal_isr = Calculate("../../Programa5/Code/history.txt")

    def search_t(self, p1, dof):
        '''Search for t from p using a statistical approximation method

        '''
        t, d = 1.0, 0.5
        p0 = 0
        E = 0.0000001
        found = False
        p_ini = self.cal_isr.get_integral_value(t, dof, 10)
        posit = True if p_ini > p1 else False
        while (not found):
            p0 = self.cal_isr.get_integral_value(t, dof, 30)
            error = p0 - p1
            if abs(error) < E or error == 0:
                found = True
            else:
                # If the error sign changes
                if (posit and error < 0) or (not posit and error > 0):
                    d /= 2
                    posit = True if error > 0 else False
                if p0 < p1:
                    t += d
                else:
                    t -= d
        return t


    def search_all_t(self):
        '''Search all value's t per element in <listaSE>.

        '''
        res_t = 0
        result = []
        iterator = True
        if self.values_table:
            temp = self.values_table.getFirst()
            while (iterator):
                p, dof = temp.getElement()
                res_t = self.search_t(p, dof)
                if res_t:
                    result.append([p, dof, res_t ])
                else:
                    print('Error: Value not found')
                if temp == self.values_table.getLast():
                    iterator = False
                else:
                    temp = self.values_table.nextElement(temp)
        return result
