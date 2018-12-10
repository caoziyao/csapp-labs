# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/20 
@desc:
"""
from parser_descent.lexical_analysis import lexical_analysis
from parser_descent.syntax_analysis import syntax_analysis


def exper_test():
    """
    :return:
    """
    s1 = 'a = (3 - 5) * 2 * (2 + 3) '
    t1 = lexical_analysis(s1)
    syntax_analysis(t1)


def for_test():
    s2 = 'for ( a = 1; a = 3; a = 5 + 2)  { b = 3 }'
    t2 = lexical_analysis(s2)
    syntax_analysis(t2)


def main():
    for_test()


if __name__ == '__main__':
    main()
