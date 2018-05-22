#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Copyright 2018(c). All rights reserved.
#
# This is free software; you can do what the LICENCE file allows you to.
# Author: Ing. Oraldo Jacinto Simon

from calculate import CalculateRelativeSize as Calculate
from texttable import Texttable, get_color_string as color, bcolors

class Main(object):
    def __init__(self):
        '''Shows a table in console with the output of relatives sizes ranges

        '''
        calculate = Calculate()
        values = calculate.get_relative_size_ranges()
        table = Texttable()
        table.set_cols_align(["l", "l", "l","l", "l", "l"])
        table.set_cols_valign(["m", "m", "m","m", "m", "m"])
        table.set_cols_dtype(['t', 'f', 'f', 'f', 'f','f'])
        table.set_precision(4)
        head = ['',
            color(bcolors.GREEN,"VS"),
            color(bcolors.GREEN,"S"),
            color(bcolors.GREEN,"M"),
            color(bcolors.GREEN,"L"),
            color(bcolors.GREEN,"VL")
        ]
        rows = []
        rows.append(head)
        [rows.append(element) for element in values]
        table.add_rows(rows)
        print(table.draw() + "\n")
