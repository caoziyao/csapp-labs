# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/25 
@desc:
"""


class Section(object):

    def __init__(self):
        self.section_data = []
        self.section_txt = []
        self.template = """
global start
section .text

start:
   {text}

exit:
    mov     rax, 0x2000001 ; exit
    mov     rdi, 0
    syscall
section .data
    {data}
        """

    def statement(self, code):
        self.section_data.append(code)

    def commit(self, code):
        self.section_txt.append(code)

    def gen(self):
        t = self.template.format(
            text='\n'.join(self.section_txt),
            data='\n'.join(self.section_data),
        )
        with open('bin/main.s', 'w') as f:
            f.write(t)