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
from parser_descent.stmt_parse import StmtParse


class ForParse(object):

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

    def parse_for(self):
        """
        for ( a = 1; a < 3; a = a + 2  )  { print "adwf" }
        :param token_list:
        :return:
        """
        tokens = self.tokens

        tokens.get_token()  # for
        t = tokens.get_token()  # (
        kind = t.type
        value = t.value
        #
        if kind != Type.parenthesesLeft:
            raise Exception('expect ( but {}'.format(value))

        self.stm_parse.parse_stmt()  # expert
        t = tokens.get_token()  # ;
        if t.type != Type.semicolon:
            raise Exception('expect 1; but {}'.format(t.value))

        self.stm_parse.parse_stmt()  # expert
        t = tokens.get_token()  # ;
        if t.type != Type.semicolon:
            raise Exception('expect 2; but {}'.format(t.value))

        self.stm_parse.parse_stmt()  # expert
        t = tokens.get_token()  # )
        if t.type != Type.parenthesesRight:
            raise Exception('expect ) but {}'.format(t.value))

        t = tokens.get_token()  # {
        if t.type != Type.braceLeft:
            raise Exception('expect { but {}'.format(t.value))

        self.stm_parse.parse_stmt()  # expert

        t = tokens.get_token()  # {
        if t.type != Type.braceRight:
            raise Exception('expect { but {}'.format(t.value))

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
