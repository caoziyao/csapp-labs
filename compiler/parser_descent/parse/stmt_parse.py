# coding: utf-8
"""
"""

from .parse_expr import ExprParse
from .parse_array import ArrayExpr
from compiler.parser_descent.token_list import TokenList
from compiler.common.tokentype import Type
from compiler.common.expression import Number, ID, ExpAdd, ExpTimes, ExpAssgin, ExpDiv, ExpSub, ExpLessThen, \
    ExpMoreThen, String


class StmtParse(object):

    def __init__(self, tokens):
        """
        tokens: TokenList
        :param tokens:
        """
        self.tokens = tokens

        

    def parse_stmt(self):
        """
        a = 1 + 2 * 3
        1 < 2
        a > 3
        :param token_list:
        :return:
        """
        tokens = self.tokens

        a = tokens.get_token()

        # id
        assign = tokens.get_token()  # =
        kind = assign.type
        value = assign.value

        if a.type == Type.number:
            left = Number(a.value)
        elif a.type == Type.id:
            left = ID(a.value)
        elif a.type == Type.string:
            left = String(a.value)
        else:
            raise Exception('unknnow')

        if kind == Type.assign:

            n = tokens.current()

            if n.type == Type.number:
                res = ExprParse(tokens).parse_expr()
            elif n.type == Type.bracketLeft:
                res = ArrayExpr(tokens).parse_arr()

            else:
                raise Exception('expect [] exper but {}'.format(value))

            root = ExpAssgin(left, res)
        elif kind == Type.less_then:
            # res = self.parse_expr()
            res = ExprParse(tokens).parse_expr()
            root = ExpLessThen(left, res)
        elif kind == Type.more_then:
            # res = self.parse_expr()
            res = ExprParse(tokens).parse_expr()
            root = ExpMoreThen(left, res)
        else:
            raise Exception('expect = but {}'.format(value))

        return root
