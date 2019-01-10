# coding: utf-8

from compiler.common.tokentype import Type
from compiler.common.expression import Number, ID, ExpAdd, ExpTimes, ExpAssgin, ExpDiv, ExpSub, ExpLessThen, \
    ExpMoreThen, String


class ArrayExpr(object):

    def __init__(self, tokens):
        """
        tokens: TokenList
        :param tokens:
        """
        self.tokens = tokens

    def parse_arr(self):
        """
        []
        表达式 expr ::= term { (+|-) term }*
        :return:
        """
        tokens = self.tokens
        root = None

        return root
