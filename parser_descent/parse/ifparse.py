# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/12/20 
@desc:
"""

from common.tokentype import Type
from parser_descent.parse.stmt_parse import StmtParse
from common.expression import ExpIf


class IfParse(object):

    def __init__(self, tokens):
        self.tokens = tokens
        self.stm_parse = StmtParse(tokens)

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
