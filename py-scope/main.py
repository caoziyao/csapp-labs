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
from src.vm.register import VM
from src.ir.three_address import IRTree
from src.gen.register_vm.gen_register_vm import CodeRen


def run():
    print('------run-------')
    os.system('make')
    os.system('make run')


def main():
    """
     if (11 > 10)
        {
            print "aaa"
            print "ccc"
        }
        else
        {
            print "bbb"
        }$

            var a = 2 * 2 + 3 * 5 + 2;
        print "abdd";
    :return:
    """
    codes = """
        if (11 > 10)
        {
            print "aaa"
            print "cccc"
        }
        else
        {
            print "bbb"
        }
       
    """
    lines = codes.split(';')

    asms = []
    for l in lines:
        code = l.strip()
        if code == '':
            continue

        lexer.input(code)
        for t in lexer:
            print(t)

        a2 = parser.parse(code)

        tree = IRTree(a2)
        ir = tree.gen()

        g = CodeRen(ir)
        asm = g.gen()

        asms.extend(asm)


    print('asm', asms)
    vm = VM(asms)
    vm.run()

if __name__ == '__main__':
    main()
