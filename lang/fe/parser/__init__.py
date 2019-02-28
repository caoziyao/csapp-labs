# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/23 
@desc:
"""
from ply.yacc import yacc

from lang.fe.lexer import tokens
# from lang.fe.lexer import
from lang.fe.parser.parse_calc import *
from lang.fe.parser.parse_if import *
from lang.fe.parser.parse_statement import *
from lang.fe.parser.parse_array import *
# from lang.fe.parser.parse_print import *
# from lang.fe.parser.parse_condition import *
# from lang.fe.parser import *
# from lang.fe.parser import *
# from lang.fe.parser.parse_def import *

parser = yacc()
