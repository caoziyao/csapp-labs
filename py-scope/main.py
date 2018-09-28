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
        var b = 134;
        var a = 1;
        if (b > 10)
        {
            print "aaa"
            print "cccc"

            print b
        }
        else
        {
            print "bbb"
        }

        var a = 2;
        a = a + 1;
        print a;
    :return:
    """
    codes = """
        var b = 134;
        if (b > 10)
        {
            print "1"
            print "2"
        }
        else
        {
            print "3"
        };
        
        var a = 1;
        while ( a < 3 ) 
        {
            print "4"
            a = a + 1
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
