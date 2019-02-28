# coding: utf-8


from lang.base.kind import Kind

class QuadAssign(object):

    def __init__(self, arg1=None, arg2=None):
        super(QuadAssign, self).__init__()
        self.op = Kind.var
        self.arg1 = arg1
        self.arg2 = arg2

    def __str__(self, level=0):
        ret = '{} {} {}'.format(self.arg1, self.op.name, self.arg2)
        return ret
