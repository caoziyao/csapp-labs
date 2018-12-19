# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/12/13 
@desc:
"""

from enum import Enum, unique


@unique
class LabelType(Enum):

    label = 0

    forloop = 1    # for loop
    fordone = 2      # for done

    whilestart = 3  # while start
    whileend = 4    # while end

    kdef_name = 5   # def name