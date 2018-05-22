#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Copyright 2018(c). All rights reserved.
#
# This is free software; you can do what the LICENCE file allows you to.
# Author: Ing. Oraldo Jacinto Simon

from calculate import CalculateAveraging
from texttable import Texttable, get_color_string as color, bcolors

class main(object):
    def __init__(self):
        '''Shows a table in console with the output of the standard 'deviation
        calculation'

        '''
        calculate = CalculateAveraging()
        result = calculate.get_standard_desviation()
        values = result['values']
        count = result['count']
        total = result['summation']
        avg = result['avg']
        intermediate = result['total_intermediate']
        desviation = result['standard_desviation']
        table = Texttable()
        table.set_cols_align(["c", "c", "c"])
        table.set_cols_valign(["t", "m", "b"])
        head = [
            color(bcolors.GREEN,"n"),
            color(bcolors.GREEN,"The numbers in X"),
            color(bcolors.GREEN,"Intermediate value=(Xi-Xavg)^2")]
        summary = [
            color(bcolors.BLUE,"Total"),
            color(bcolors.RED,"Xi=%d" % total),
            color(bcolors.RED,intermediate)]
        label = ['n=%d' % count, color(bcolors.BLUE,'Xavg = Xi/n'),
            color(bcolors.BLUE,'Standard Desviation')]
        result_final = ['', color(bcolors.RED,avg),
            color(bcolors.RED,desviation)]
        rows = []
        rows.append(head)
        [rows.append(element) for element in values]
        rows.append(summary)
        rows.append(label)
        rows.append(result_final)
        table.add_rows(rows)
        print(table.draw() + "\n")
