# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/20 
@desc:
"""
import os
from src.lexer import lexer
from src.parser import parser
from src.semantic import semantic_analyzer
from src.gen.register_vm import gen_register_vm as gen
from src.vm.register import VM


def parse_test():
    while True:
        try:
            s = input('calc > ')
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s)
        print(result)


def atest1():
    # lexer.input('5 + 2 * 3')
    # for t in lexer:
    #     print(t)

    # lexer.input('if (2 > 1) {a = 2} else {a = 1}')
    # for t in lexer:
    #     print(t)

    # # parse_test()
    # s = parser.parse('5 + 2 * 3 - 1 + 6 - 3 * 2')
    # a1 = parser.parse('var a')
    a2 = parser.parse('var a')
    ret = semantic_analyzer(a2)
    a2 = parser.parse('var b')
    ret = semantic_analyzer(a2)

    # a2 = parser.parse('a = 2')
    a2 = parser.parse('if (2 > 1) {a = 2} else {1 + 2}')
    ret = semantic_analyzer(a2)
    # s = parser.parse('print "sds"')
    print(a2)
    # print(a2)

    # ret = semantic(a1)

    # print('ret', ret)

    # c = myinstr(s)
    # print(c)
    # # lexer_test()


def run():
    print('------run-------')
    os.system('make')
    os.system('make run')


def parse_txt():
    pass


def main():
    # s = parser.parse('print "hello js"')
    # ret = semantic_analyzer(s)
    # print(s)

    # lexer.input('if (2 > 6) { print "abc" } else { print "cdf" }')
    # for t in lexer:
    #     print(t)

    # gen(ret)
    # run()
    # a2 = parser.parse('var a')
    # ret = semantic_analyzer(a2)
    # a2 = parser.parse('if (9 > 6) { print "ddfe" } else { print "cdf" }')

    # s = parser.parse('print "hello js"')
    # ret = semantic_analyzer(s)
    # print(s)
    # a = """
    #  if (0 > 1)  {
    #         print "ddfe"
    #     }
    #     else {
    #         print "cdf"
    #     };
    #
    # """
    codes = """
        var a = 1;
        if (a > 1)  { 
            print "ddfe" 
        } 
        else { 
            print "cdf" 
        };
    """
    lines = codes.split(';')

    asm = []
    for l in lines:
        # print(code.split(';'))
        code =  l.strip()
        if code  == '':
            continue

        lexer.input(code)
        for t in lexer:
            print(t)

        a2 = parser.parse(code)
        print('a', a2)

        ir = semantic_analyzer(a2)

        a = gen(ir)
        asm.extend(a)

    print('asm', asm)
    vm = VM(asm)
    vm.run()

        # s = parser.parse('print "hello js"')
        # print(a2)
        # ir = semantic_analyzer(a2)
        # a3 = gen_register_vm(ir)
        # print(a3)
        #
        # print('----run---')
        # vm = VM(a3)
        # vm.run()
        #
        # print('----run over----')
        # ret = semantic_analyzer(s)
        # print('ret', ret)


if __name__ == '__main__':
    main()
