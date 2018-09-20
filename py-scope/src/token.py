# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/20 
@desc:
"""

from enum import Enum


class Type(Enum):
    auto = 0                # auto 的时候, c 是 : , { } [] 其中之一, 要自己判断
    colon = 1               # :
    comma = 2               # ,
    braceLeft = 3           # {
    braceRight = 4          # }
    bracketLeft = 5         # [
    bracketRight = 6        # ]
    keyword = 7             # true false null
    number = 8              # 123
    string = 9              # "name"
    var = 10                # var


class Token():
    def __init__(self, token_type=None, value=None):
        d = {
            ':': Type.colon,
            ',': Type.comma,
            '{': Type.braceLeft,
            '}': Type.braceRight,
            '[': Type.bracketLeft,
            ']': Type.bracketRight,
            'var': Type.var,
        }
        if token_type == Type.auto:
            self.type = d[value]
        else:
            self.type = token_type

        self.value = value

    def __repr__(self):
        s = 'type: {}, len: {}, value: {}'.format(self.type, len(str(self.value)), self.value)
        s = '"{}"'.format(self.value)
        return s