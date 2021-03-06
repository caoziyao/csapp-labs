# coding: utf-8

from compiler.common.tokentype import Type
from compiler.common.expression import Number, ID, ExpAdd, ExpTimes, ExpAssgin, ExpDiv, ExpSub, ExpLessThen, \
    ExpMoreThen, String


class ExprParse(object):

    def __init__(self, tokens):
        """
        tokens: TokenList
        :param tokens:
        """
        self.tokens = tokens

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
            # return value
            return Number(value)
        elif kind == Type.id:
            return ID(value)
        elif kind == Type.parenthesesLeft:
            value = self.parse_expr()
            tokens.get_token()
            # return value
            return value
        else:
            raise Exception('expect number but {}'.format(value))

    def parse_term(self):
        """
        term -> term * factor | term / factor | factor
        :return:
        """
        tokens = self.tokens

        left = self.parse_factor()

        t = tokens.current()
        if t is None:
            return left

        root = left
        kind = t.type
        value = t.value

        while kind in [Type.times, Type.div]:
            tokens.get_token()

            if kind == Type.times:
                right = self.parse_factor()
                # res *= right
                root = ExpTimes(root, right)
            elif kind == Type.div:
                right = self.parse_factor()
                # left /= right
                root = ExpDiv(root, right)

            t = tokens.current()
            if t is None:
                break

            kind = t.type
            value = t.value

        # if t is not None:
        #     raise Exception('expect */ but {} {}'.format(kind, value))

        return root

    def parse_expr(self):
        """
        1 + 2 * 3
        表达式 expr ::= term { (+|-) term }*
        :return:
        """
        tokens = self.tokens

        left = self.parse_term()

        t = tokens.current()
        if t is None:
            return left

        root = left
        kind = t.type
        value = t.value
        while kind in [Type.add, Type.sub]:
            tokens.get_token()

            if kind == Type.add:
                right = self.parse_term()
                # res += right
                root = ExpAdd(root, right)
            elif kind == Type.sub:
                right = self.parse_term()
                # res -= right
                root = ExpSub(root, right)

            t = tokens.current()
            if t is None:
                break

            kind = t.type
            value = t.value

        return root

