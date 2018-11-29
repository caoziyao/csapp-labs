# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/23 
@desc:
"""

import ply.yacc as yacc
from zy.src.parser.parse_calc import *
from zy.src.parser.parse_print import *
from zy.src.parser.parse_condition import *
from zy.src.parser.parse_statement import *
from zy.src.parser.parse_while import *
from zy.src.parser.parse_def import *

parser = yacc.yacc()
