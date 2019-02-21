# coding: utf-8
"""
descent_parsing 递归下降
算法基本思想
每个非终结符构造一个分析函数
用前看符号指导产生式规则的规则
"""
from compiler.common.tokentype import Type
from compiler.parser_descent.parse.stmt_parse import StmtParse
from compiler.parser_descent.parse.forparse import ForParse
from compiler.parser_descent.token_list import TokenList
from compiler.parser_descent.parse.ifparse import IfParse
from compiler.parser_descent.token_list import TokenList
from compiler.common.tokentype import Type
from compiler.common.expression import (Number, ID, ExpAdd, ExpTimes, ExpAssgin, ExpDiv, ExpSub, ExpLessThen, \
                                        ExpMoreThen, String)


def parse_if(tokens):
    """
    tokens: TokenList
    :param tokens:
    :return:
    """
    p = IfParse(tokens)
    root = p.parse_if()

    return root


def parse_for(tokens):
    """
    tokens: TokenList
    :param tokens:
    :return:
    """
    p = ForParse(tokens)
    root = p.parse_for()

    return root


def parse_keyword(tokens):
    """
    tokens: TokenList
    :param tokens:
    :return:
    """
    t = tokens.current()
    kind = t.type
    value = t.value
    if value == 'for':
        root = parse_for(tokens)
    elif value == 'if':
        root = parse_if(tokens)

    else:
        raise Exception('unkonw kw')

    return root


def parse_stmt(tokens):
    """
    tokens: TokenList
    :param tokens:
    :return:
    """
    parse = StmtParse(tokens)
    root = parse.parse_stmt()
    return root


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
        root = parse_stmt(tokens)
    elif kind == Type.keyword:
        root = parse_keyword(tokens)
    else:
        raise Exception('unknow syntax_analysis')

    return root
