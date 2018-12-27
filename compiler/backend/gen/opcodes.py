# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/12/27 
@desc:
"""


class Opcodes(object):

    def __init__(self, code=0, name='', testFlag=0, mode=None):
        self.testFlag = testFlag
        self.mode = mode
        self.name = name
        self.code = code
        self.a = code
        self.b = code
        self.c = code


    def opmode(self):

        self.opmode = {
            'mov' : ''
        }

# opcodes = {
#     0: Opcodes(0, 'mov', 0, 'ab'),
# }
