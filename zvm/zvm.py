# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/12/4 
@desc:
"""
import sched
import time
from zvm.cpu.cpu import CPU
from graphics.graphics import Graphics

scheduler = sched.scheduler(time.time, time.sleep)


class ZVM(object):

    def __init__(self):
        self.frame = 60
        self.init_cpu()
        self.init_graphics()

    def init_cpu(self):
        self.cpu = CPU()

    def init_graphics(self):
        self.grap = Graphics(self.cpu)

    def run_task(self):
        """
        run run_task
        :return:
        """
        for i in range(10000):
            pass
            # self.cpu.run()

        self.grap.draw()
        scheduler.enter(1 / self.frame, 1, self.run_task)

    def run(self):
        """
        run zvm
        :return:
        """
        scheduler.enter(1 / self.frame, 1, self.run_task)
        scheduler.run()
