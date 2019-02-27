# coding: utf-8

import unittest
from tests.test_case.base import BaseCase

class TestDemoCase(BaseCase):

    def test_demo(self):
        """test_demo"""
        # print('test_demo')
        pass

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
