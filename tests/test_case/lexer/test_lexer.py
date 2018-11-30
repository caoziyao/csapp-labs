# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/20 
@desc:
python3 testmain.py lexer
"""

import unittest
from tests.test_case.base import BaseCase
from zy.src.lexer import lexer


class TestLexter(BaseCase):

    def test_lexer(self):
        data = '''
                var a = 2
                a == false
        '''
        # Give the lexer some input
        lexer.input(data)

        for tok in lexer:
            print(tok)

    def test_lexer2(self):

        lexer.input('print "sds" ')
        for t in lexer:
            print(t)

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
