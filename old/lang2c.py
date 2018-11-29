# coding: utf-8


"""
lang 汇编 转换为 c 语言
[['add', '1', ['+', '1', '2']], ['mul', '2', '3', '4']]
"""
from src.utils import log

class CProcess(object):
    def __init__(self):
        pass

    def include(self):
        t = """
            #include <stdio.h>
        """
        return t

    def main(self, code):
        t = """
            int main() {
                {}
                return 0;
            }
        """.format(code)

        return t


def lang2c(asm):
    cp = CProcess()
    res = []
    i = 0
    while i < len(asm):
        item = asm[i]
        i += 1
        if isinstance(item, list):
            e = lang2c(item)
            res.append(e)
        else:
            if item == '+':
                e, offset = add_end(asm, i)
                i += offset - 1
                res.extend(e)
            elif item == '*':
                e, offset = mul_end(asm, i)
                i += offset - 1
                res.extend(e)
            else:
                # error
                pass

    return res


def main():
    asm = [['add', '1', '2'], ['mul', '2', '3', '4']]
    c = lang2c(asm)
    log('c', c)

if __name__ == '__main__':
    main()