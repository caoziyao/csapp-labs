# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/12/5 
@desc:
"""

import unittest
from tests.test_case.base import BaseCase
from graphics.graphics import Graphics


class TestGraphics(BaseCase):

    @unittest.skipIf(True, "I don't want to run this case.")
    def test_drawchar(self):
        """
        :return:
        """
        t = '8'
        g = Graphics()

        while True:
            g.draw_char(t)
