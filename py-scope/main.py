# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/20 
@desc:
"""
from src.calclex import lexer
from src.calc_parser import parser

def lexer_test():
    data = '''
        3 + 4 * 10
          + -20 *2
        '''

    # Give the lexer some input
    lexer.input(data)

    for tok in lexer:
        print(tok)

    # Tokenize
    # while True:
    #     tok = lexer.token()
    #     if not tok:
    #         break  # No more input
    #     print(tok)

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
    parse_test()

if __name__ == '__main__':
    main()
