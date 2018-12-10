# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/20 
@desc:
"""

# from parser_descent.src.lexer import lexer
# from parser_descent.src.parse import parse
from parser_descent.lexical_analysis import lexical_analysis
from parser_descent.syntax_analysis import syntax_analysis


def main():
    # tokens = lexer(codes)
    # parse(tokens)
    # s = 'position = inital + rate * 60'
    s = 'a = (1 - 2) * 2 * (2 + 3) '
    # s = 'for ( a = 1; a < 3; a = a + 2  )  { print "adwf" }'
    tokens = lexical_analysis(s)
    syntax_analysis(tokens)


if __name__ == '__main__':
    main()
