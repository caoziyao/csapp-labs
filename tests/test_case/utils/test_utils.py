# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/20 
@desc:
"""
# from zy.src.commont.utils import is_space
#
# import unittest
# from tests.test_case.base import BaseCase
#
# class TestLexter(BaseCase):
#
#     def test_is_space(self):
#         """test_demo"""
#         test_items = [
#             {
#                 'data': ' ',
#                 'expect': True
#             },
#             {
#                 'data': '\n',
#                 'expect': True
#             },
#             {
#                 'data': 'a',
#                 'expect': False
#             },
#         ]
#
#         for item in test_items:
#             data = item.get('data', '')
#             expect = item.get('expect', '')
#             self.assertEqual(is_space(data), expect)
#
#
#     @unittest.skip("I don't want to run this case.")
#     def test_divide(self):
#         """test_divide"""
#         # 跳过该测试
#         self.assertEqual(2, 2)
#
#     @unittest.skipIf(False, "I don't want to run this case.")
#     def test_condition(self):
#         """test_condition"""
#         # 第一个参数为 True 跳过该测试
#         self.assertEqual(2, 2)
