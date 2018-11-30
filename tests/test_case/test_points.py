# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/11/30 
@desc:
"""

import unittest
from tests.test_case.base import BaseCase
from vm.assembler import points


class TestPoints(BaseCase):

    def test_byte(self):
        t = {
            0:      b'00000000',
            1:      b'00000001',
            2:      b'00000010',
            127:    b'01111111',
            128:    b'00000000',
            129:    b'00000001',
            -1:     b'10000001',
            -2:     b'10000010',
            -127:   b'11111111',
        }
        for n, expect in t.items():
            self.assertEqual(points.byte_point(n), expect, msg='test byte_point {} {}'.format(n, expect))

    def test_short(self):
        t = {
            0:      b'0000000000000000',
            1:      b'0000000000000001',
            2:      b'0000000000000010',
            -1:     b'1000000000000001',
        }
        for n, expect in t.items():
            self.assertEqual(points.short_point(n), expect, msg='test short_point {} {}'.format(n, expect))

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
