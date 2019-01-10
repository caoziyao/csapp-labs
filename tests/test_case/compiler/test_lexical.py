# coding: utf-8


import unittest
from tests.test_case.base import BaseCase
from compiler.parser_descent.lexical_analysis import lexical_analysis


class TestLexicalCase(BaseCase):

    def test_exper(self):
        """test_exper"""
        s1 = 'a = 1 + 2 '
        t1 = lexical_analysis(s1)
        print('t1', t1)

        s2 = 'a = []'
        t2 = lexical_analysis(s2)
        print('t2', t2)

    def test_for(self):
        s2 = 'for ( a = 1; a < 19; a = a + 1)  { b = a * 2 }'
        t2 = lexical_analysis(s2)

        print('t2', t2)

    def test_if(self):
        s2 = 'if ( 9 < 4)  { b = 3 } else { b = 2 }'
        t2 = lexical_analysis(s2)
        print('t2', t2)
