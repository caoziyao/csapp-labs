# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/23 
@desc:
"""
from src.common.expression import Kind


# 递归实现前序、中序、后序遍历
def pre_order(node):
    if node:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)


def mid_order(node):
    if node:
        pre_order(node.left)
        print(node.value)
        pre_order(node.right)


class Section(object):

    def __init__(self):
        self.section_data = []
        self.section_txt = []
        self.template = """
        global start
        section .text
        
        start:
           {text}
           
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
            f.write(t.strip())


def gen_div(left, right):
    t = left / right
    return t


def gen_times(left, right):
    t = left * right
    return t


def gen_plus(left, right):
    t = left + right
    return t


def gen_minus(left, right):
    t = left - right
    return t


def gen_number(node):
    t = node.value
    print('mov   eax, {}'.format(t))
    return t


def gen_assignment(left, right):
    t = '{} = {}'.format(str(left), str(right))
    print('mov   [{}], {}'.format(left, right))
    return t


def gen_id(node):
    t = node.value
    print('.db {}'.format(t))
    return t


def is_leaf(node):
    """

    :param node:
    :return:
    """
    if (node.left is None) and (node.right is None):
        return True
    else:
        return False


def post_order(node):
    root = {
        Kind.plus: gen_plus,
        Kind.minus: gen_minus,
        Kind.times: gen_times,
        Kind.div: gen_div,
        Kind.assignment: gen_assignment,
    }
    leaf = {
        Kind.number: gen_number,
        Kind.id: gen_id,
    }

    if node:
        left = post_order(node.left)
        right = post_order(node.right)

        kind = node.type
        if is_leaf(node):
            f = leaf[kind]
            t = f(node)
        else:
            f = root[kind]
            t = f(left, right)

        return t


def gen_section_assignment(left, right, section):
    s = section
    s.commit('mov [{}] rbx'.format(left))


def gen_section_num(node, section):
    s = section
    value = node.value
    s.commit('mov rbx {}'.format(value))
    return value


def gen_section_id(node, section):
    s = section
    value = node.value
    s.statement('var{}  db ?'.format(value))
    return value


def gen_section(node, section):
    """
    section .data
    :return:
    """
    if node:
        left = gen_section(node.left, section)
        right = gen_section(node.right, section)

        kind = node.type
        if kind == Kind.assignment:
            gen_section_assignment(left, right, section)

        elif kind == Kind.id:
            t = gen_section_id(node, section)
            return t

        elif kind == Kind.number:
            t = gen_section_num(node, section)
            return t
        else:
            pass
        # return t


def myinstr(ast):
    """

    :return:
    """
    section = Section()
    t = post_order(ast)
    gen_section(ast, section)
    section.gen()
    return t
