# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/23 
@desc:
python3 testmain.py parse
"""
from zy.src.parser import parser

import unittest
from tests.test_case.base import BaseCase


class TestParse(BaseCase):

    def test_parser(self):
        s = parser.parse('a = 1')

    @unittest.skip("I don't want to run this case.")
    def test_divide(self):
        """test_divide"""
        # 跳过该测试
        self.assertEqual(2, 2)

    @unittest.skipIf(False, "I don't want to run this case.")
    def test_condition(self):
        """test_condition"""
        # 第一个参数为 True 跳过该测试
        self.assertEqual(2, 2)
