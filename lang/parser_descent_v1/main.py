# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/20 
@desc:
"""

from src.lexer import lexer
from src.parser import parse


def main():
    # codes = '3 + 4 * 5'
    codes = '3 + 1 * 5'
    tokens = lexer(codes)
    parse(tokens)

if __name__ == '__main__':
    main()