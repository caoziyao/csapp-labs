# coding: utf-8

from lang.fe import parser
# from lang.mid.expression import IRExpression
from lang.mid import IRTree


def parse_code(code):
    """
    :param code:
    :return:
    """
    t = parser.parse(code)
    return t


def main():
    root = parse_code('def main() { a = 1 + 2 }')
    # root = parse_code('b = a + 23')


    print('-----fe------')
    print(root)

    # qs = []
    e = IRTree()
    qs = e.gen_three(root)

    print('-----ir------')
    for q in qs:
        print(q)


if __name__ == '__main__':
    main()
