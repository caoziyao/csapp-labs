# coding: utf-8

"""
把 AST 转为 自己的汇编语法（中间语言），优化
[[['+', '1', '2'], ['*', '2', '3', '4']]]
"""
from src.utils import log

def add_end(code, index):
    """
    code: ['+', '1', '2']
    index: 1
    """
    offset = 3
    res = ['add']
    i = index
    while i < len(code):
        c = code[i]
        i += 1
        if isinstance(c, list):
            e = transform_asm(c)
            res.append(e)
        else:
            res.append(c)
    return res, offset


def mul_end(code, index):
    """
    code: ['*', '1', '2']
    index: 1
    """
    offset = 4
    res = ['mul']
    i = index
    while i < len(code):
        c = code[i]
        i += 1
        res.append(c)

    return res, offset


def transform_asm(ast):

    res = []
    i = 0
    while i < len(ast):
        item = ast[i]
        i += 1
        if isinstance(item, list):
            e = transform_asm(item)
            res.append(e)
        else:
            if item == '+':
                e, offset = add_end(ast, i)
                i += offset - 1
                res.extend(e)
            elif item == '*':
                e, offset = mul_end(ast, i)
                i += offset - 1
                res.extend(e)
            else:
                # error
                pass

    return res



def asm_add_end(code, index):
    """
    code: ['+', '1', '2']
    index: 1
    """
    offset = 3
    res = 'add '
    i = index
    while i < len(code):
        c = code[i]
        i += 1
        if isinstance(c, list):
            e = format_asm(c)
            res += e
        else:
            res += c + ' '
    return res, offset


def asm_mul_end(code, index):
    """
    code: ['+', '1', '2']
    index: 1
    """
    offset = 4
    res = 'mul '
    i = index
    while i < len(code):
        c = code[i]
        i += 1
        res += c + ' '

    return res, offset

def format_asm(asm):
    """
    asm: [['add', '1', '2'], ['mul', '2', '3', '4']]
    """
    line = ''
    i = 0
    while i < len(asm):
        item = asm[i]
        i += 1
        if isinstance(item, list):
            e = format_asm(item)
            line += e + '\n'
        else:
            if item == 'add':
                e, offset = asm_add_end(asm, i)
                i += offset - 1
                line += e + '\n'
            elif item == 'mul':
                e, offset = asm_mul_end(asm, i)
                i += offset - 1
                line += e + '\n'
            else:
                # error
                pass

    return line

def main():
    ast = [['+', '1', '2'], ['*', '2', '3', '4']]
    asm = transform_asm(ast)
    log('asm', asm)

    r = format_asm(asm)
    log('r', r)


if __name__ == '__main__':
    main()