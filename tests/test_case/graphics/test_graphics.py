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

    def test_draw(self):
        """

        :return:
        """
        t = ['1', '2', '3']
        g = Graphics()

