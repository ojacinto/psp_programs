#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Copyright 2018(c). All rights reserved.
#
# This is free software; you can do what the LICENCE file allows you to.
# Author: Ing. Oraldo Jacinto Simon

import sys
sys.path.append('/home/oraldo/src/maestria/ISW/Programa3/Code')
sys.path.append('/home/oraldo/src/maestria/ISW/Programa5/Code')
sys.path.append('/home/oraldo/src/maestria/ISW/Programa6/Code')
from regression import CalculateRegression as Regression
from calculatep import CalculateIntegrateSimpsonRule as Calculatep
from search import Searchtdistribution as Search
import math

class CalculateRequeriments(object):
    '''Calculate the following requirements:

    '•calculate the correlation between two variables x and y'
    '•calculate the significance of that correlation'
    '•calculate the linear regression parameters B0 and B1 for a set of n'
    ' pairs of data,'
    '• given an estimate E, calculate an improved prediction P, where: '
    '  P = B0 - B1*E'
    '• calculate the 70% prediction interval for that estimate'

    '''

    def __init__(self):
        self.regre = Regression("../../Programa3/Code/history.txt")
        self.test1 = self.regre.test1
        self.test2 = self.regre.test2
        self.tests = self.regre.tests[0:2]
        self.n = self.regre.n
        self.cal_insr = Calculatep("../../Programa5/Code/history.txt")
        self.t = Search("../../Programa6/Code/history.txt")


    def get_correlation_significance(self, listaSE):
        '''Calculate the significance (the tail area) as 1 - 2 * p

        '''
        dof = 0
        r = self.regre.coefficient_correlation_r(listaSE)
        r_square = self.regre.coefficient_square_r(listaSE)
        t = (abs(r)*math.sqrt(self.n-2))/ math.sqrt(1-r_square)
        dof = self.n - 2
        p = self.cal_insr.get_integral_value(t, dof, 70)
        sig = 1 - (2 * p)
        return dict(sig=sig, r=r, r_square=r_square)

    def get_sumatorias(self, listaSE, B0, B1, xavg):
        '''Calculate this equations:
        'res1 = ∑(yi-B0-B1Xi)^2)'
        'res2 = ∑(Xi-Xavg)^2'

        '''
        rest1, rest2, sum_rest1, sum_rest2 = 0, 0, 0, 0
        iterator = True
        if listaSE:
            temp = listaSE.getFirst()
            while (iterator):
                x, y = temp.getElement()
                x = float(x)
                y = float(y)
                rest1 = y - B0 -(B1*x)
                rest2 = x - xavg
                sum_rest1 += math.pow(rest1, 2)
                sum_rest2 += math.pow(rest2, 2)
                if temp == listaSE.getLast():
                    iterator = False
                else:
                    temp = listaSE.nextElement(temp)
        return sum_rest1, sum_rest2


    def get_desviation_standard(self, listaSE):
        '''The formula for calculating the standard deviation term is:
        'sigma = sqrt(1/(n-2)*∑(yi-B0-B1Xi)^2)'

        '''
        sum_y, sum_x, B1, B0, sigma, sumatoria = 0, 0, 0, 0, 0, 0
        n = self.n
        res = self.regre.get_quantities(listaSE)
        x_avg = res['x_avg']
        B1 = self.regre.calculate_pending_B1(listaSE)
        B0 = self.regre.calculate_intercept_B0(listaSE)
        p = self.regre.improved_prediction_P(listaSE)
        sumatoria, sum_xless_avg  = self.get_sumatorias(listaSE, B0, B1, x_avg)
        mult = math.pow(n-2, -1)*sumatoria
        sigma = math.sqrt(mult)
        return dict(sigma=sigma, n=n, sum_x=sum_x,x_avg=x_avg, B1=B1, B0=B0,
                    p=p, sum_xless_avg=sum_xless_avg)

    def get_range_70(self, listaSE):
        '''Calculate the Range for a 70% interval
        'Range = t(0.35, dof)sigma*sqrt(1+1/n+((E-Xavg)^2/(∑(Xi-Xavg)^2))'

        '''
        desviation = self.get_desviation_standard(listaSE)
        sigma = desviation['sigma']
        sum_xless_avg = desviation['sum_xless_avg']
        x_avg = desviation['x_avg']
        n = self.n
        E = 386
        p70 = 0.35
        t = self.t.search_t(p70, self.n-2)
        num = round(math.pow(E-x_avg, 2), 2)
        suma = 1 + math.pow(n, -1) + num/sum_xless_avg
        raiz = math.sqrt(suma)
        range_r = t*sigma*raiz
        return range_r

    def get_UPI_70(self, listaSE, p):
        '''Calculate the UPI as P + Range(70%)

        '''
        return p + self.get_range_70(listaSE)

    def get_LIP_70(self, listaSE, p):
        '''Calculate the LPI as P - Range(70%)

        '''
        return p - self.get_range_70(listaSE)

    def calculate_all_values(self):
        '''Return a list() of list with the values expected:
        'r, r^2, significance, B0, B1, _range, upi, lip'

        '''
        result = []
        for test in self.tests:
            correlation = self.get_correlation_significance(test)
            r = correlation['r']
            r_square = correlation['r_square']
            significance = correlation['sig']
            res = self.get_desviation_standard(test)
            B0 = res['B0']
            B1 = res['B1']
            p = res['p']
            range_r = self.get_range_70(test)
            upi = self.get_UPI_70(test, p)
            lip = self.get_LIP_70(test, p)
            result.append([r, r_square, significance, B0, B1, p, range_r, upi, lip])
        return result
