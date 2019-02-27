# coding: utf-8

from zvm.cpu.cpu import CPU
from zvm.zvm import ZVM


def asm_test():
    a = bytearray([0x21, 0x02, 0x09])  # b'210209'  # irmovq  $9  %rdx
    cpu = CPU()
    cpu.load_memory(a)

    cpu.run()


def lang_test():
    zvm = ZVM()
    zvm.run_forever()


def main():
    # zvm = ZVM()
    # zvm.run()
    lang_test()


if __name__ == '__main__':
    main()
