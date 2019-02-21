# coding: utf-8

class TokenList(object):

    def __init__(self, tokens):
        # self.index = 0
        self.tokens = tokens

    def current(self):

        if self.isend():
            t = None
        else:
            # t = self.tokens[self.index]
            t = self.tokens[0]

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
        # return self.index == self.size()
        return len(self.tokens) == 0

    def get_token(self):
        """
        :return:
        """
        # t = self.tokens[self.index]
        # self.index += 1

        t = self.tokens[0]
        self.tokens = self.tokens[1:]
        return t

    def lookahead(self):
        """
        :return:
        """
        if self.isend():
            t = None
        else:
            # t = self.tokens[self.index + 1]
            t = self.tokens[1]

        return t