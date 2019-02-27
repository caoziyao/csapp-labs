# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/12/20 
@desc:
"""

from compiler.common.tokentype import Type
from compiler.parser_descent.parse.stmt_parse import StmtParse
from compiler.common.expression import ExpIf


class IfParse(object):

    def __init__(self, tokens):
        self.tokens = tokens
        self.stm_parse = StmtParse(tokens)

    def parse_if(self):
        """
        if ( 1 < 4)  { b = 3 } else { b = 2 }
        :param token_list:
        :return:
        """
        e = ExpIf()
        tokens = self.tokens

        tokens.get_token()  # if

        # (
        t = tokens.get_token()
        if t.type != Type.parenthesesLeft:
            raise Exception('expect ( but {}'.format(t.value))

        # expert
        e.test_expr = self.stm_parse.parse_stmt()

        # )
        t = tokens.get_token()
        if t.type != Type.parenthesesRight:
            raise Exception('expect ) but {}'.format(t.value))

        # {
        t = tokens.get_token()
        if t.type != Type.braceLeft:
            raise Exception('expect { but {}'.format(t.value))

        # expert
        e.if_stmt = self.stm_parse.parse_stmt()

        # }
        t = tokens.get_token()
        if t.type != Type.braceRight:
            raise Exception('expect } but {}'.format(t.value))

        # else
        t = tokens.get_token()
        if t.value != 'else':
            raise Exception('expect else but {}'.format(t.value))

        # {
        t = tokens.get_token()
        if t.type != Type.braceLeft:
            raise Exception('expect { but {}'.format(t.value))

        # expert
        e.else_stmt = self.stm_parse.parse_stmt()

        # }
        t = tokens.get_token()
        if t.type != Type.braceRight:
            raise Exception('expect } but {}'.format(t.value))

        return e
