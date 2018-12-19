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
    forloop = 0    # for loop
    fordone = 1      # for done

    whilestart = 2  # while start
    whileend = 3    # while end

    kdef_name = 4   # def name