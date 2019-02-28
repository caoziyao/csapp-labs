# coding: utf-8


from lang.base.kind import Kind


class QuadExpr(object):

    def __init__(self, op, result, x, y):
        self.op = op
        self.result = result
        self.x = x
        self.y = y

    def __str__(self, level=0):
        ret = '{} {} {} {}'.format(self.result, self.x, self.op.name, self.y)
        return ret
