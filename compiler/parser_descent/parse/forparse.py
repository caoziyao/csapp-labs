# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/12/10 
@desc:
"""

from compiler.common.tokentype import Type
from compiler.parser_descent.parse.stmt_parse import StmtParse
from compiler.common.expression import ExpFor


class ForParse(object):

    def __init__(self, tokens):
        self.tokens = tokens
        self.stm_parse = StmtParse(tokens)

    def parse_for(self):
        """
        for ( a = 1; a < 3; a = a + 2  )  { print "adwf" }
        :param token_list:
        :return:
        """
        e = ExpFor()
        tokens = self.tokens

        tokens.get_token()  # for
        t = tokens.get_token()  # (
        kind = t.type
        value = t.value
        #
        if kind != Type.parenthesesLeft:
            raise Exception('expect ( but {}'.format(value))

        e.init_stmt = self.stm_parse.parse_stmt()  # expert
        t = tokens.get_token()  # ;
        if t.type != Type.semicolon:
            raise Exception('expect ;(1) but {}'.format(t.value))

        e.test_expr = self.stm_parse.parse_stmt()  # expert
        t = tokens.get_token()  # ;
        if t.type != Type.semicolon:
            raise Exception('expect 2(2s) but {}'.format(t.value))

        e.update_stmt = self.stm_parse.parse_stmt()  # expert
        t = tokens.get_token()  # )
        if t.type != Type.parenthesesRight:
            raise Exception('expect ) but {}'.format(t.value))

        t = tokens.get_token()  # {
        if t.type != Type.braceLeft:
            raise Exception('expect { but {}'.format(t.value))

        e.code = self.stm_parse.parse_stmt()  # expert
        t = tokens.get_token()  # }
        if t.type != Type.braceRight:
            raise Exception('expect } but {}'.format(t.value))

        return e
        #     # for ( ; ; ;) {}
        #     match(t, 'for')  # for
        #     match(t, '(')  # (
        #     optexpr()  #
        #     match(t, ';')  # ;
        #     optexpr()  #
        #     match(t, ';')  # ;
        #     optexpr()  #
        #     match(t, ';')  # ;
        #     match(t, ')')  # )
        #     match(t, '{')  # {
        #     optexpr()  #
        #     match(t, '}')  # }
        #
        # elif kind == Type.id:
        #     optexpr()

        # tokens.get_token()  # id
        # assign = tokens.get_token()  # =
        # kind = assign.type
        # value = assign.value

        # if kind == Type.assign:
        #     # expr = exprself.parse_expr()
        # else:
        #     raise Exception('expect = but {}'.format(value))
        #
        # print('expr', expr)
