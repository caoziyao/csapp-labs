# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/12/6 
@desc:
descent_parsing 递归下降
算法基本思想
每个非终结符构造一个分析函数
用前看符号指导产生式规则的规则
"""
from parser_descent.src.token import Type
from parser_descent.src.expression import ExpInt, ExpAdd, ExpTimes, Kind, ExpDiv
from parser_descent.stmt_parse import StmtParse
from parser_descent.forparse import ForParse
from parser_descent.token_list import TokenList


def syntax_analysis(token_list):
    """
    :param token_list:
    :return:
    """
    tokens = TokenList(token_list)
    t = tokens.current()
    kind = t.type
    value = t.value

    if kind == Type.id:
        parse = StmtParse(tokens)
        parse.parse_stmt()
    elif kind == Type.keyword and value == 'for':
        p = ForParse(tokens)
        p.parse_for()
