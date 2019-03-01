# coding: utf-8
from lang.base.kind import Kind


class QuadLabel(object):

    def __init__(self, op, label):
        self.op = op
        self.label = label

    def __str__(self, level=0):
        ret = 'tag: {}'.format(self.label)
        return ret
