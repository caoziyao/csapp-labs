# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/26 
@desc:
进程
"""

from enum import Enum, unique


class ProcessStatus(Enum):
    new = 0
    ready = 1
    waiting = 2
    running = 3
    terminated = 4


class Process(object):

    def __init__(self):
        self.status = ''  # 状态

        self.counter = ''  # 当前执行位置

        # image
        self.data = ''  # 数据段
        self.stack = ''  # 数据
        self.heap = ''  # 堆
        self.text = ''  # 代码
