# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/20 
@desc:
"""
# from lang.lexer import lexer
# from lang.parser import parser
# from vm import VM
# from backend.ir.three_address import IRTree
# from backend.gen import CodeRen
# from lang.common import Kind


from parser_descent.lexical_analysis import lexical_analysis
from parser_descent.syntax_analysis import syntax_analysis
from backend.ir.three_address import IRTree
from backend.gen.gen_register_vm import CodeRen

def exper_test():
    """
    :return:
    """
    s1 = 'a = (1 - 2) * 3 * (4 + 5) '
    t1 = lexical_analysis(s1)
    root = syntax_analysis(t1)
    print('expr', root)

    return root


def for_test():
    s2 = 'for ( a = 1; a < 3; a = a + 2)  { b = 3 }'
    t2 = lexical_analysis(s2)
    root = syntax_analysis(t2)
    print('expr', root)

    return root


def main():
    root = exper_test()

    ir = IRTree(root)
    ts = ir.gen()

    for t in ts:
        print(t)

    gen = CodeRen()
    b = gen.gen(ts)

    print(b)

if __name__ == '__main__':
    main()

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
#
#
# def compiler(code):
#     lexer.input(code)
#     for t in lexer:
#         # print(t)
#         pass
#
#     # 语法树
#     root = parser.parse(code)
#
#     # s = Sematic(root)
#     # s.sem()
#
#     # 中间代码
#     tree = IRTree(root)
#     ir = tree.gen()
#
#     # 代码生成
#     g = CodeRen(ir)
#     asm = g.gen()
#
#     return asm, root.type
#
#
# def main():
#     with open('c.lan', 'r') as f:
#         s = f.read()
#         lines = s.split(';')
#         asms, func = [], []
#
#         for l in lines:
#             code = l.strip()
#             if code == '':
#                 continue
#
#             asm, kind = compiler(code)
#             if kind == Kind.kdef:
#                 func.extend(asm)
#             else:
#                 asms.extend(asm)
#
#         asms = func + ['start:'] + asms
#         vm = VM(asms)
#         vm.run()


# if __name__ == '__main__':
#     main()
