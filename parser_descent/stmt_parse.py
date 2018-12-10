# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/12/10 
@desc:
"""

from parser_descent.src.token import Type
from parser_descent.src.expression import ExpInt, ExpAdd, ExpTimes, Kind, ExpDiv
from parser_descent.token_list import TokenList


class StmtParse(object):

    def __init__(self, tokens):
        """
        tokens: TokenList
        :param tokens:
        """
        self.tokens = tokens

    def valid_keyword(self, token, name):
        """

        :param name:
        :return:
        """
        kind = token.type
        value = token.value

        if kind == Type.keyword and value == name:
            return True
        else:
            return False

    def parse_factor(self):
        """
        factor -> digit | ( expr )
        :return:
        """
        tokens = self.tokens

        t = tokens.get_token()
        kind = t.type
        value = t.value

        if kind == Type.number:
            return value
        elif kind == Type.parenthesesLeft:
            value = self.parse_expr()
            tokens.get_token()
            return value
        else:
            raise Exception('expect number but {}'.format(value))

    def parse_term(self):
        """
        term -> term * factor | term / factor | factor
        :return:
        """
        tokens = self.tokens

        res = self.parse_factor()

        t = tokens.current()
        if t is None:
            return res

        kind = t.type
        value = t.value

        while kind in [Type.times, Type.div]:
            tokens.get_token()

            if kind == Type.times:
                right = self.parse_factor()
                res *= right
            elif kind == Type.div:
                right = self.parse_factor()
                res /= right

            t = tokens.current()
            if t is None:
                break

            kind = t.type
            value = t.value

        # if t is not None:
        #     raise Exception('expect */ but {} {}'.format(kind, value))

        return res

    def parse_expr(self):
        """
        1 + 2 * 3
        表达式 expr ::= term { (+|-) term }*
        :return:
        """
        tokens = self.tokens

        res = self.parse_term()

        t = tokens.current()
        if t is None:
            return res

        kind = t.type
        value = t.value
        while kind in [Type.add, Type.sub]:
            tokens.get_token()

            if kind == Type.add:
                right = self.parse_term()
                res += right
            elif kind == Type.sub:
                right = self.parse_term()
                res -= right

            t = tokens.current()
            if t is None:
                break

            kind = t.type
            value = t.value

        # if t is not None:
        #     raise Exception('expect +- but {} {}'.format(kind, value))

        return res

    def parse_stmt(self):
        """
        a = 1 + 2 * 3
        :param token_list:
        :return:
        """
        tokens = self.tokens

        tokens.get_token()  # id
        assign = tokens.get_token()  # =
        kind = assign.type
        value = assign.value

        if kind == Type.assign:
            expr = self.parse_expr()
        else:
            raise Exception('expect = but {}'.format(value))

        print('expr', expr)
