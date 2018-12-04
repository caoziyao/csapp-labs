# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/12/4 
@desc:
"""
from isa.cpu import CPU


def asm_test():
    a = bytearray([0x21, 0x02, 0x09])  # b'210209'  # irmovq  $9  %rdx
    cpu = CPU()
    cpu.load_memory(a)

    cpu.run()


def main():
    asm_test()


if __name__ == '__main__':
    main()
