#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Copyright 2018(c). All rights reserved.
#
# This is free software; you can do what the LICENCE file allows you to.
# Author: Ing. Oraldo Jacinto Simon

from regression import CalculateRegression as Calculate
from texttable import Texttable, get_color_string as color, bcolors


class Main(object):
    def __init__(self):
        '''Shows a table in console with the output of linear regression
        'parameters'

        '''
        calculate = Calculate("history.txt")
        values = calculate.get_regression_linear()
        table = Texttable()
        table.set_cols_align(["c", "c", "c","c", "c", "c"])
        table.set_cols_valign(["m", "m", "m","m", "m", "m"])
        table.set_cols_dtype(['t', 'f', 'f', 'f', 'f','f'])
        table.set_cols_width([10, 15, 10, 10, 10, 10])
        head = [
            color(bcolors.GREEN,"Test"),
            color(bcolors.GREEN,"Expected Values"), '', '', '', '']
        parameters = ['',
            color(bcolors.GREEN,"B0"),
            color(bcolors.GREEN,"B1"),
            color(bcolors.GREEN,"r"),
            color(bcolors.GREEN,"r^2"),
            color(bcolors.GREEN,"P")]
        rows = []
        rows.append(head)
        rows.append(parameters)
        [rows.append(element) for element in values]
        table.add_rows(rows)
        print(table.draw() + "\n")
