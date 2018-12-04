# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/23 
@desc:
"""

import ply.yacc as yacc
from lang.src.parser.parse_calc import *
from lang.src.parser.parse_print import *
from lang.src.parser.parse_condition import *
from lang.src.parser.parse_statement import *
from lang.src.parser.parse_while import *
from lang.src.parser.parse_def import *

parser = yacc.yacc()
