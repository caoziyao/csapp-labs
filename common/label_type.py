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
    forstart = 0    # for start
    forend = 1      # for end
