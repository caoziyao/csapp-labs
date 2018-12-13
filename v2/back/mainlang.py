# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/20
@desc:
"""
from v2.back.lang.src.lexer import lexer
from v2.back.lang.src.parser import parser
from v2.back.vm import VM
from v2.back.lang.src.ir.three_address import IRTree
from v2.back.lang.src.gen.register_vm.gen_register_vm import CodeRen
from v2.back.lang.src.common.expression import Kind


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

    # 语法树
    root = parser.parse(code)

    # s = Sematic(root)
    # s.sem()

    # 中间代码
    tree = IRTree(root)
    ir = tree.gen()

    # 代码生成
    g = CodeRen(ir)
    asm = g.gen()

    return asm, root.type


def main():
    with open('c.lan', 'r') as f:
        s = f.read()
        lines = s.split(';')
        asms, func = [], []

        for l in lines:
            code = l.strip()
            if code == '':
                continue

            asm, kind = compiler(code)
            if kind == Kind.kdef:
                func.extend(asm)
            else:
                asms.extend(asm)

        asms = func + ['start:'] + asms
        vm = VM(asms)
        vm.run()


if __name__ == '__main__':
    main()
