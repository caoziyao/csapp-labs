# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/23 
@desc:
"""

import ply.yacc as yacc
from .parse_calculation import *
from .parse_assignment import *
from .parse_print import *

parser = yacc.yacc()