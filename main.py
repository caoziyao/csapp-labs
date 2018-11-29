# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/20 
@desc:
"""
import os
from zy.src.lexer import lexer
from zy.src.parser import parser
from zy.src.semantic.semantic import Sematic
from zy.src.vm.register import VM
from zy.src.ir.three_address import IRTree
from zy.src.gen.register_vm.gen_register_vm import CodeRen
from zy.src.common.expression import Kind


#
#
# def mtest():
#     while True:
#         try:
#             s = input('cal > ')
#         except EOFError:
#             break
#
#
#
# def main():
#     """
#         var b = 134;
#         print b;
#         if (b > 10)
#         {
#             print "1"
#             print "2"
#         }
#         else
#         {
#             print "3"
#         };
#
#         var a = 1;
#         while ( a < 3 )
#         {
#             print "4"
#             a = a + 1
#         }
#     :return:
#     var a = 2;
#
#      def (a) {
#             print a
#         }
#     """
#     codes = """
#
#          def abc ( ) {
#             print "hello"
#         };
#
#         call abc;
#         call abc;
#     """
#     lines = codes.split(';')
#
#     asms = []
#     asms_func = []
#     for l in lines:
#         code = l.strip()
#         if code == '':
#             continue
#
#         asm, kind = compiler(code)
#         if kind == Kind.kdef:
#             asms_func.extend(asm)
#         else:
#             asms.extend(asm)
#
#     asms = asms_func + ['start:'] + asms
#     print('asm', asms)
#     vm = VM(asms)
#     vm.run()


def compiler(code):
    lexer.input(code)
    for t in lexer:
        # print(t)
        pass

    root = parser.parse(code)

    # s = Sematic(root)
    # s.sem()

    tree = IRTree(root)
    ir = tree.gen()

    g = CodeRen(ir)
    asm = g.gen()

    return asm, root.type


def main():
    with open('c.lan', 'r') as f:
        s = f.read()
        lines = s.split(';')
        asms = []
        asms_func = []
        for l in lines:
            code = l.strip()
            if code == '':
                continue

            asm, kind = compiler(code)
            if kind == Kind.kdef:
                asms_func.extend(asm)
            else:
                asms.extend(asm)

        asms = asms_func + ['start:'] + asms
        vm = VM(asms)
        vm.run()


if __name__ == '__main__':
    main()
