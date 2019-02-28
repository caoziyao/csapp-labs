# coding: utf-8


from lang.fe.lexer import lexer
from lang.fe.parser import parser


def atest1():
    # Test it out
    # t = parser.parse('a + 4')
    t = parser.parse('a * 4 + a * 2 * b')
    # t = parser.parse('if ( 3 + 4 ) { 1 +  2 } else { 4 + 5 }')
    # t = parser.parse('if ( a = 3 + 4 ) { 1 +  2 }')
    # t = parser.parse('a = 3 + 4')
    # t = parser.parse('a = []')
    # t = parser.parse('a [ 2 ]')
    print(t)


def main():
    atest1()


if __name__ == '__main__':
    main()
