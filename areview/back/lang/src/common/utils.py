# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/24 
@desc:
"""

def is_leaf(node):
    """

    :param node:
    :return:
    """
    if (node.left is None) and (node.right is None):
        return True
    else:
        return False