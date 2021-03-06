# coding: utf-8

from compiler.parser_descent.lexical_analysis import lexical_analysis
from compiler.parser_descent.syntax_analysis import syntax_analysis
from compiler.backend.ir.three_address import IRTree
from compiler.backend.gen.gen_register_vm import CodeRen
from vm.vm_register import VM


def exper_test():
    """
    :return:
    """
    # s1 = 'a = (10 + 1) * 1 * (3 + 1) '
    s1 = 'a = 1 + 2 * 4'
    # s1 = 'a = 12'
    # s1 = 'a < 2'
    t1 = lexical_analysis(s1)

    print('token_list', t1)
    # root = syntax_analysis(t1)
    # print('expr', root)
    #
    # return root


def for_test():
    s2 = 'for ( a = 1; a < 19; a = a + 1)  { b = a * 2 }'
    t2 = lexical_analysis(s2)
    root = syntax_analysis(t2)
    print('expr', root)

    return root


def if_test():
    s2 = 'if ( 9 < 4)  { b = 3 } else { b = 2 }'
    t2 = lexical_analysis(s2)
    root = syntax_analysis(t2)
    print('expr', root)

    return root


def arr_test():
    s2 = 'a = [1, 3, 14]'
    t2 = lexical_analysis(s2)
    print('t2', t2)
    root = syntax_analysis(t2)
    print('expr', root)

    # return root


def main():
    root = arr_test()

    # quads = []
    # ir = IRTree(quads)
    # ir.gen(root)
    #
    # print('========')
    # for t in quads:
    #     print(t)
    # #
    # gen = CodeRen()
    # bs = gen.gen(quads)
    #
    # print('========')
    # for b in bs:
    #     print(b)
    #
    # vm = VM(bs)
    # r, m = vm.run()
    #
    # print('========')
    # print(m)


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
