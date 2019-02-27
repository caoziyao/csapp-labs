# coding: utf-8

from compiler.common.tokentype import Type
from compiler.common.expression import Array


class ArrayExpr(object):

    def __init__(self, tokens):
        """
        tokens: TokenList
        :param tokens:
        """
        self.tokens = tokens

    def parse_arr(self):
        """
        todo array
        :return:
        """
        tl = self.tokens
        tokens = tl.tokens[1:-1]

        l = []
        for i in tokens:
            if i.type == Type.number:
                l.append(i)
        root = Array(l)

        return root
