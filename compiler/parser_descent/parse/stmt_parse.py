# coding: utf-8
"""
"""

from .parse_expr import ExprParse
from .parse_array import ArrayExpr
from compiler.parser_descent.token_list import TokenList
from compiler.common.tokentype import Type
from compiler.common.expression import (Number, ID, ExpAdd, ExpTimes, ExpAssgin, ExpDiv, ExpSub, ExpLessThen, \
                                        ExpMoreThen, String)


class StmtParse(object):

    def __init__(self, tokens):
        """
        tokens: TokenList
        :param tokens:
        """
        self.tokens = tokens

    def stmt_left(self):
        """
        a = b
        :return:
        """
        tokens = self.tokens

        _id = tokens.get_token()
        id_type = _id.type
        id_val = _id.value

        if id_type == Type.id:
            left = ID(id_val)
        else:
            raise Exception('stmt_left')

        return left

    def valid_stmt(self, assign):
        """
        :return:
        """
        kind = assign.type
        value = assign.value

        if kind != Type.assign:
            raise Exception('expect = but {}'.format(value))

    def parse_expr(self):
        """

        :return:
        """
        tokens = self.tokens
        right = ExprParse(tokens).parse_expr()

        return right

    def parse_array(self):
        """

        :return:
        """
        tokens = self.tokens
        right = ArrayExpr(tokens).parse_arr()

        return right

    def parse_stmt(self):
        """
        a = 1 + 2 * 3
        # 1 < 2
        # a > 3
        :param token_list:
        :return:
        """
        tokens = self.tokens

        # left
        left = self.stmt_left()

        # =
        assign = tokens.get_token()
        self.valid_stmt(assign)

        # right
        n = tokens.current()
        if n.type == Type.bracketLeft:
            res = self.parse_array()
        else:
            res = self.parse_expr()

        root = ExpAssgin(left, res)

        return root

    # def parse_stmt(self):
    #     """
    #     a = 1 + 2 * 3
    #     1 < 2
    #     a > 3
    #     :param token_list:
    #     :return:
    #     """
    #     tokens = self.tokens
    #
    #     a = tokens.get_token()
    #
    #     # id
    #     assign = tokens.get_token()  # =
    #     kind = assign.type
    #     value = assign.value
    #
    #     if a.type == Type.number:
    #         left = Number(a.value)
    #     elif a.type == Type.id:
    #         left = ID(a.value)
    #     elif a.type == Type.string:
    #         left = String(a.value)
    #     else:
    #         raise Exception('unknnow')
    #
    #     if kind == Type.assign:
    #
    #         n = tokens.current()
    #
    #         if n.type == Type.bracketLeft:
    #             res = ArrayExpr(tokens).parse_arr()
    #
    #
    #         else:
    #             res = ExprParse(tokens).parse_expr()
    #
    #         root = ExpAssgin(left, res)
    #     elif kind == Type.less_then:
    #         # res = self.parse_expr()
    #         res = ExprParse(tokens).parse_expr()
    #         root = ExpLessThen(left, res)
    #     elif kind == Type.more_then:
    #         # res = self.parse_expr()
    #         res = ExprParse(tokens).parse_expr()
    #         root = ExpMoreThen(left, res)
    #     else:
    #         raise Exception('expect = but {}'.format(value))
    #
    #     return root
