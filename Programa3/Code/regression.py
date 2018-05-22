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

class CalculateRegression(object):
    '''Calculate the linear regression parameters B0 and B1 correlation
       'coefficients r and r 2 for a set of n pairs of data given an estimated'
       'proxy size E, calculate an improved prediction P, where P = B0+B1*E'

    '''


    def __init__(self, url):
        fichero = open(url, "r")
        # Build a list that contains each of the rows in Table1 as history
        history = [eval(line.replace('/n', '')) for line in fichero.readlines()]
        fichero.close()
        # Number of data points
        self.n = len(history)
        # Build a linked list for each test where each node contains a list of
        # two real numbers that corresponds to the columns required by the test.
        self.test1 = ListSE()
        self.test2 = ListSE()
        self.test3 = ListSE()
        self.test4 = ListSE()
        self.tests = []
        for col in history:
            self.test1.insertNodeLast([col[1], col[3]])
            self.test2.insertNodeLast([col[1], col[4]])
            self.test3.insertNodeLast([col[2], col[3]])
            self.test4.insertNodeLast([col[2], col[4]])
        self.tests.append(self.test1)
        self.tests.append(self.test2)
        self.tests.append(self.test3)
        self.tests.append(self.test4)

    def get_quantities(self, listaSE):
        '''Return a dict() with the calculate the next ∑ for each pair of values
        'of "x" and "y": where x and y are the values stored in each node of a'
        'ListSE.'

        'Example:'
        'Node1   Node2   Node3'
        '[1,2]-->[3,4]-->[4,5]'
        'In Node1: x = 1, y = 2 and so on all the nodes that follow'

        '''
        x = 0
        y = 0
        sum_x = 0
        x_avg = 0
        y_avg = 0
        sum_y = 0
        sum_square_x = 0
        sum_square_y = 0
        sum_mult_xy = 0
        n = 0
        iterator = True
        values = {}
        if listaSE:
            temp = listaSE.getFirst()
            while(iterator):
                x, y = temp.getElement()
                x = float(x)
                y = float(y)
                sum_x += x
                sum_y += y
                mult = x*y
                sum_square_x += math.pow(x, 2)
                sum_square_y += math.pow(y, 2)
                sum_mult_xy += mult
                n +=1
                values[n] = temp.getElement()
                if temp == listaSE.getLast():
                    iterator = False
                else:
                    temp = listaSE.nextElement(temp)
            x_avg = sum_x/n
            y_avg = sum_y/n
        return dict(
             values=values,
             count=n,
             sum_x=sum_x,
             x_avg=x_avg,
             y_avg=y_avg,
             sum_y=sum_y,
             sum_square_x=sum_square_x,
             sum_square_y=sum_square_y,
             sum_mult_xy=sum_mult_xy)

    def calculate_pending_B1(self, listaSE):
        '''Calculate the slope (B1) by means of the relationship:
        'B1 = (∑xy - (n*x_avg*y_avg)) / ∑x^2 - (n*x_avg^2)'

        '''
        values = self.get_quantities(listaSE)
        sum_mult_xy = values['sum_mult_xy']
        n = values['count']
        x_avg = values['x_avg']
        y_avg = values['y_avg']
        sum_square_x = values['sum_square_x']
        x_avg_square = math.pow(x_avg, 2)
        n = values['count']
        B1 = (sum_mult_xy - (n*x_avg*y_avg)) / (sum_square_x - (n*x_avg_square))
        return round(B1, 9)

    def calculate_intercept_B0(self, listaSE):
        '''Calculate the intercept (B0) by means of the relationship:
        'B0 = y_avg - B1*x_avg'

        '''
        values = self.get_quantities(listaSE)
        y_avg = values['y_avg']
        B1 = self.calculate_pending_B1(listaSE)
        x_avg = values['x_avg']
        return round(y_avg - (B1*x_avg), 9)

    def coefficient_correlation_r(self, listaSE):
        '''Calculate the correlation coefficient r by means of the
        'relationship:'
        'r = (n∑xy) - ((∑x)(∑y))) / sqrt(((n*∑x^2)-(∑x)^2) ((n*∑y^2)-(∑y)^2))

        '''
        values = self.get_quantities(listaSE)
        n = values['count']
        sum_mult_xy = values['sum_mult_xy']
        sum_x = values['sum_x']
        sum_y = values['sum_y']
        sum_square_x = values['sum_square_x']
        sum_x_square = math.pow(sum_x, 2)
        sum_square_y = values['sum_square_y']
        sum_y_square = math.pow(sum_y, 2)
        square_x = (n*sum_square_x) - math.pow(sum_x, 2)
        square_y = (n*sum_square_y) - math.pow(sum_y, 2)
        r = (n*(sum_mult_xy) - (sum_x*sum_y)) / (math.sqrt(square_x*square_y))
        return round(r, 9)

    def coefficient_square_r(self, listaSE):
        '''Returns the square of r

        '''
        return round(math.pow(self.coefficient_correlation_r(listaSE), 2), 9)

    def improved_prediction_P(self, listSE, E=None):
        '''Calculate an improved prediction P given an estimated proxy size E:
        'where: E=386'
        'P = B0 - B1*E'

        '''
        E = E if E else 386
        B0 = self.calculate_intercept_B0(listSE)
        B1 = self.calculate_pending_B1(listSE)
        return round(B0 + (B1*E), 7)

    def get_regression_linear(self):
        '''Returns a list() with linear regression parameters

        '''
        result = []
        number = 0
        for tests in self.tests:
            values = []
            number += 1
            test = 'Test%d' % number
            values.append(test)
            values.append(self.calculate_intercept_B0(tests))
            values.append(self.calculate_pending_B1(tests))
            values.append(self.coefficient_correlation_r(tests))
            values.append(self.coefficient_square_r(tests))
            values.append(self.improved_prediction_P(tests))
            result.append(values)
        return result
