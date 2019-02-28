# coding: utf-8

from lang.fe import parser
from lang.mid.expression import IRExpression


def parse_code(code):
    """
    :param code:
    :return:
    """
    t = parser.parse(code)
    return t


def main():
    root = parse_code('def main() { a = 1 + 2 }')
    print(root)

    # e = IRExpression()
    #
    # qs = []
    # e.gen_expression(root, qs)
    #
    # for q in qs:
    #     print(q)


if __name__ == '__main__':
    main()
