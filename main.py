# coding: utf-8


from lang.fe.lexer import lexer
from lang.fe.parser import parser


def atest1():
    # Test it out
    t = parser.parse('3 + 4')
    print(t)


def main():
    atest1()


if __name__ == '__main__':
    main()
