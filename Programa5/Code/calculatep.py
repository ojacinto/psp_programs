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

class CalculateIntegrateSimpsonRule(object):
    '''Integrate Numerically the Student’s t-distribution probability density
    'function ( t-distribution pdf) using Simpson’s rule. The total'
    'probability' is the area of the function (the integral) from -t to t.'
    'We will take advantage of the symmetry of the function and only'
    'integrate from 0 to t.'

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

    def get_factorial(self, val):
        '''Calculate factorial's val minus one

        '''
        for num in range(2, val):
            val *= num
        return val

    def get_gamma(self, val):
        '''Calculate gamma value, if value is int(): gamma = (val - 1)! else
        'gamma = (val-1)gamma(x-1) where gamma(1) = 1 and gamma(1/2) = sqrt(Pi)'

        '''
        result = 0
        val -= 1
        if isinstance(val, int) :
            return self.get_factorial(val)
        else:
            result = val
            new_val = 0
            while val > 0:
                new_val = val - 1
                if new_val > 0:
                    result *= new_val
                val -= 1
        # Always the value is not integer the division between two will end
        # after the comma comes a 5. By subtracting one always until reaching
        # zero always the ultim value will be 1/2 = sqrt(Pi).
        return result * math.sqrt(math.pi)

    def not_divisible_by_2(self, val):
        if val%2 != 0:
            val = float(val)
        return val

    def get_function_Xi(self, Xi, dof, gamma_num, gamma_denom):
        '''When numerically integrating the t-distribution probability density
        'function with Simpson’s rule, use the following function'
        'F0(x) = ((1 + (Xi)^2 / dof)^-(dof+1)/2 )'
        'F(x)= ( (gamma*(dof+1)/2) / (((dof*Pi)^1/2)*((gamma*dof)/2)) * F0 )'

        '''
        F0, gamma, F1 = 0, 0, 0
        Pi = math.pi
        base_F0 = 1 + (math.pow(Xi, 2)/dof)
        # It is necessary to convert to float because otherwise it takes only
        # the whole division part and discards the places after the comma
        exp_more = float(dof+1)
        exp = -(exp_more / 2)
        F0 = math.pow(base_F0, exp)
        F = gamma_num / (math.pow(dof*Pi, 0.5) * gamma_denom) * F0
        return F

    def get_integral_value(self, val, dof, num_seg):
        '''Calculate the total probability p: is the area of the function (the
        'integral)' 'from -t to t.'
        'p = W/3 [F(0) + ∑4*F(iW)] +∑2*F(iW) F(t)'

        '''
        val_ini, sum_Fx_by_2, sum_Fx_by_4, val_end = 0, 0, 0, 0
        Xi, sum_terms, p = 0, 0, 0
        W = val/num_seg
        dof_more_one = self.not_divisible_by_2(dof+1)
        dof = self.not_divisible_by_2(dof)
        gamma_num = self.get_gamma(dof_more_one/2)
        gamma_denom = self.get_gamma(dof/2)
        for i in range(0, num_seg):
           sum_2, sum4 = 0, 0
           Xi = i * W
           if i == 0:
               val_ini = self.get_function_Xi(Xi, dof, gamma_num, gamma_denom)
           elif i%2 == 0 and i != 0:
               sum_2 = self.get_function_Xi(Xi, dof, gamma_num, gamma_denom)
               sum_Fx_by_2 += 2 * sum_2
           else:
               sum_4 = self.get_function_Xi(Xi, dof, gamma_num, gamma_denom)
               sum_Fx_by_4 += 4 * sum_4
        val_end = self.get_function_Xi(val, dof, gamma_num, gamma_denom)
        sum_terms = val_ini + sum_Fx_by_2 + sum_Fx_by_4 + val_end
        p = sum_terms * (W/3)
        return p

    def get_total_probability_p(self):
        '''Calculate for all values of <listaSE> the total probability

        '''
        p, p0, p1 = 0, 0, 0
        E = 0.0000001
        result = []
        iterator = True
        if self.values_table:
            temp = self.values_table.getFirst()
            while (iterator):
                t, dof = temp.getElement()
                # num_seg = 10
                p0 = round(self.get_integral_value(t, dof, 10), 5)
                # num_seg = 20
                p1 = round(self.get_integral_value(t, dof, 20), 5)
                if abs(p0 - p1) < E:
                     p = p1
                else:
                   print('Error: The absolute value |%f-%f| > %f' % (p0,p1,E))
                label = '0 to {t}'.format(t=t)
                result.append([label, dof, p])
                if temp == self.values_table.getLast():
                    iterator = False
                else:
                    temp = self.values_table.nextElement(temp)
        return result
