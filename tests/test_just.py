# coding: utf-8


from unittest import skip, skipIf
from tests.base_test import BaseTest


class TestJustTest(BaseTest):

    def test_just_test(self):
        self.assertEqual(3, 3)

    @skip('skip')
    def test_just_skip(self):
        self.assertEqual(3, 3)

    @skipIf(True, 'if ture skip')
    def test_just_skipif(self):
        self.assertEqual(3, 3)
