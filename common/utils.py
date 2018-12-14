# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/24 
@desc:
"""
from common.tokentype import Type

def is_leaf(node):
    """

    :param node:
    :return:
    """
    _type = node.type

    if _type in [Type.number, Type.id]:
        return True
    else:
        return False
