# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/12/10 
@desc:
"""

class TokenList(object):

    def __init__(self, tokens):
        self.index = 0
        self.tokens = tokens

    def current(self):

        if self.isend():
            t = None
        else:
            t = self.tokens[self.index]

        return t

    def size(self):
        """
        :return:
        """
        return len(self.tokens)

    def isend(self):
        """
        :return:
        """
        return self.index == self.size()

    def get_token(self):
        """
        :return:
        """
        t = self.tokens[self.index]
        self.index += 1
        return t

    def lookahead(self):
        """
        :return:
        """
        if self.isend():
            t = None
        else:
            t = self.tokens[self.index + 1]

        return t