# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/20 
@desc:
"""
from src.lexer import lexer
from src.parser import parser
from src.middle.instr import myinstr

def parse_test():
    while True:
        try:
            s = input('calc > ')
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s)
        print(result)

def main():
    # lexer.input('5 + 2 * 3')
    # for t in lexer:
    #     print(t)

    # # parse_test()
    # s = parser.parse('5 + 2 * 3 - 1 + 6 - 3 * 2')
    s = parser.parse('a = 2 ')
    # s = parser.parse('print "sds"')
    print(s)
    #
    c = myinstr(s)
    print(c)
    # # lexer_test()

if __name__ == '__main__':
    main()
