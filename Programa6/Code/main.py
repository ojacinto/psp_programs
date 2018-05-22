#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Copyright 2018(c). All rights reserved.
#
# This is free software; you can do what the LICENCE file allows you to.
# Author: Ing. Oraldo Jacinto Simon

from search import Searchtdistribution as Search
from texttable import Texttable, get_color_string as color, bcolors

class Main(object):
    def __init__(self):
        '''Shows a table Integrate Numerically the Student’s t-distribution
        'probability density 'function ( t-distribution pdf) using Simpson’s'
        'rule. The total' 'probability' is the area of the function (the integral)'
        'from -t to t. The total probability is p'

        '''
        search = Search("history.txt")
        values = search.search_all_t()
        table = Texttable()
        table.set_cols_align(["l", "c", "c"])
        table.set_cols_valign(["m", "m", "m"])
        table.set_cols_dtype(['f', 'i', 'f'])
        table.set_precision(6)
        label = [
            color(bcolors.GREEN,"Test"),'',
            color(bcolors.GREEN,"Expected Values")]
        head = [
            color(bcolors.GREEN,"p"),
            color(bcolors.GREEN,"dof"),
            color(bcolors.GREEN,"t")]
        rows = []
        rows.append(label)
        rows.append(head)
        [rows.append(element) for element in values]
        table.add_rows(rows)
        print(table.draw() + "\n")
