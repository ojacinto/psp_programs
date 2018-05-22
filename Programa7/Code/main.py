#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Copyright 2018(c). All rights reserved.
#
# This is free software; you can do what the LICENCE file allows you to.
# Author: Ing. Oraldo Jacinto Simon


from texttable import Texttable, get_color_string as color, bcolors
from calculater import CalculateRequeriments as Requeriments

class Main(object):
    def __init__(self):
        '''Show results

        '''
        calculate = Requeriments()
        values = calculate.calculate_all_values()
        labels = ["r","r^2","Significance","B0","B1","P","Range","UPI(70%)","LIP(70%)"]
        table = Texttable()
        table.set_cols_align(["c", "c","c"])
        table.set_cols_valign(["m","m","m"])
        table.set_cols_dtype(['t','t','f'])
        table.set_cols_width([15 for i in range(3)])
        table.set_precision(9)
        label = [
            color(bcolors.GREEN,"Test"),
            color(bcolors.GREEN,"Parameter"),
            color(bcolors.GREEN,"Expected Value")]
        rows = []
        rows.append(label)
        number = 0
        for item in values:
            number += 1
            text = 'Test%d' % number
            for pos in range(9):
                rows.append([text, labels[pos], item[pos]])
        table.add_rows(rows)
        print(table.draw() + "\n")
