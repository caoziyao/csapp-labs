# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/11/30 
@desc:
"""

irmov = [
    0x21, 'irmov {} {}'
]

regfile = {
    0x21: {
        'mode': 'xx',
        'name': 'irmov',
        'length': 2,
        'syntax': 'irmov {} {}',
    }
}
