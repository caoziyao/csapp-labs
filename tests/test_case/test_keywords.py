# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/12/20 
@desc:
"""

from tests.test_case.base import BaseCase
from compiler.common import Keywords


class TestKeywords(BaseCase):

    def test_keywords(self):
        """
        :return:
        """
        print(Keywords.keywords())