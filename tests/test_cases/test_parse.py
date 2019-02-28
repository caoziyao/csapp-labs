# coding: utf-8

from unittest import skip, skipIf
from tests.base_test import BaseTest
from lang.fe.parser import parser


class TestParse(BaseTest):

    def test_parse(self):
        parser.parse('a * 4 + a * 2 * b')
        parser.parse('a = 3 + 4')

    def test_parse_if(self):
        parser.parse('if ( 3 + 4 ) { 1 +  2 } else { 4 + 5 }')
        parser.parse('if ( 3 + 4 ) { 1 +  2 }')

    def test_parse_array(self):
        t = parser.parse('a = []')
        t = parser.parse('a[ 2 ]')

    def test_func(self):
        parser.parse('def main() { a + 2 }')
        parser.parse('def main(a) { a + 2 }')
