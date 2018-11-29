# coding: utf-8
import os
import sys

def before():
    t = """global start
start:
$$

        """
    return t

def runx86(xasm):
    nasm = 'nasm -f macho test.s'
    gcc = 'ld -o test test.o'
    with open('test.s', 'wb') as f:
        xasm = xasm.encode()
        f.write(xasm)
        # os.system(nasm)
        # os.system(gcc)


def process_set(line):
    a = line[1]
    num = line[2]
    t = 'push eax {}'.format(num)
    return t

def asm2x86(asm):
    t = before()
    body = []
    for line in asm:
        if isinstance(line, list):
            for k in line:
                if k == 'set':
                    code = process_set(line)
                    body.append(code)
                    break
    l = '\n'
    for b in body:
        l += b + '\n'
    print('aa', l)
    new_t = t.replace('$$', l)
    print(new_t)
    return new_t

if __name__ == '__main__':
    asm = [['set', 'a', '1'], ['set', 'b', '2', '2']]
    b = asm2x86(asm)
    runx86(b)
    # print(b)
    pass