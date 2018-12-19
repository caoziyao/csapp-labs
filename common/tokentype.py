# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/20 
@desc:
"""

from enum import Enum, unique

@unique
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
    assign = 11              # =
    sub = 12                # -
    times = 13              # *
    div = 14                # /
    add = 15                # +
    more_then = 16          # >
    less_then = 17          # <
    id = 18                 # identifier abc 标志符
    parenthesesLeft = 19    # (
    parenthesesRight = 20   # )
    semicolon = 21          # ;
    goto = 22               # goto


class Token():
    def __init__(self, token_type=None, value=None, symbol_idx=None):
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
        self.symbol_idx = symbol_idx

    def __repr__(self):
        if self.symbol_idx is not None:
            s = '({} {}: {} )'.format(self.symbol_idx, self.value, self.type)
        else:
            s = '({}: {})'.format(self.value, self.type)
        # s = '"{}"'.format(self.value)
        return s