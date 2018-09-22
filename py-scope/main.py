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

def lexer_test():
    # data = '''
    #     a_abc if_ if
    #     3 + 4 * 10
    #       + -20 *2
    #     '''
    data = '''
            var a = 2
            a == false
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
    # lexer_test()
    # parse_test()
    # s = parser.parse('1+2+4')
    s = parser.parse('a = 1')
    print(s)
    # lexer_test()

if __name__ == '__main__':
    main()
