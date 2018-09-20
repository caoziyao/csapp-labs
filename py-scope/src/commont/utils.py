# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/20 
@desc:
"""


def is_space(char):
    """
    \r\n\t
    :param char:
    :return:
    """
    c = char
    if c in ' \r\n\t':
        return True
    else:
        return False
