# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/12/13 
@desc:
"""

from enum import Enum, unique


#
# @unique
# class Keywords(Enum):
#
#     var = 1         # var
#     true = 2        # true
#     false = 3       # false
#     kif = 4         # if
#     kwhile = 5      # while
#     kdef = 7        # def
#     print = 8       # print
#     call = 9        # call
#     kfor = 10       # for
#     kelse = 11      # else
#
#     undefind = 100  # undefind


class Keywords(object):
    var = 'var'
    true = 'true'
    false = 'false'
    kif = 'if'
    kwhile = 'while'
    kdef = 'def'
    print = 'print'
    call = 'call'
    kfor = 'for'
    kelse = 'else'

    undefind = 'undefind'  # undefind

    @staticmethod
    def keywords():
        """
        get keywords
        :return:
        """
        ks = [k for k in Keywords.__dict__ if not k.startswith('_')]
        ks.remove('keywords')

        values = [getattr(Keywords, k) for k in ks]
        return values
