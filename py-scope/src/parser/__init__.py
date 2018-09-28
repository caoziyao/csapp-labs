# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/23 
@desc:
"""

import ply.yacc as yacc
from src.parser.parse_calc import *
from src.parser.parse_print import *
from src.parser.parse_condition import *
from src.parser.parse_statement import *
# from src.parser.v1.parse_calculation import *
# from src.parser.v1.parse_assignment import *
# from src.parser.v1.parse_print import *
# from src.parser.v1.parse_condition import *

parser = yacc.yacc()