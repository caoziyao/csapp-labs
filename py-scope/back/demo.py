# coding: utf-8

"""
2 个函数
分别用递归和栈的方式从 token 列表解析为 ast
"""
import operator
from token_list import token_list
from token_parser import parse

vars = {}

def parsed_ast(token_list):
    """
    递归解析 ast
    """
    ts = token_list
    token = ts[0]
    del ts[0]
    if token == '[':
        exp = []
        while ts[0] != ']':
            t = parsed_ast(ts)
            exp.append(t)
        # 循环结束, 删除末尾的 ']'
        del ts[0]
        return exp
    else:
        # token 需要 process_token / parsed_token
        return token


def pop_list(stack):
    l = []
    while stack[-1] != '[':
        l.append(stack.pop(-1))
    stack.pop(-1)
    l.reverse()
    return l


def parsed_ast_stack(token_list):
    """
    用栈解析 ast
    """
    l = []
    i = 0
    while i < len(token_list):
        token = token_list[i]
        i += 1
        if token == ']':
            list_token = pop_list(l)
            l.append(list_token)
        else:
            l.append(token)
    return l

def apply(code, vars):
    res = ''
    m = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.itruediv,
    }
    cs = code.split('\n')
    token = []
    for c in cs:
        c = c.strip()
        if c != '':
            t = token_list(c)
            token.extend(t)

    tokens = parsed_ast_stack(token)

    for t in tokens:
        if t[0] == 'set':
            t2 = t[1]
            t3 = t[2]
            d = {
                t2: t3,
            }
            vars.update(d)
        else:
            symbol = t[0]
            oper = m[symbol]
            res = 1
            for index, value in enumerate(t[1:]):
                # value = int(value)
                value = vars[value]
                if index == 0:
                    res = value
                else:
                    res = oper(res, value)
    return res


def main():
    test_items = [
        ("""
         [set a 1]
         [set b 2]
         [+ a b]
         """, 3),
        ("""
            [set a 1]
            [set b 2]
            [set c 6]
            [+ a c]
            """, 7),
        ("""
        [set a 1]
        [set b 2]
        [set c 6]
        [set e 6]
        [set g 4]
        [+ a b c e g]
        """, 19),
    ]
    for t in test_items:
        code, expected = t
        u = apply(code, vars)
        e = "test_apply ERROR, ({})".format(code)
        assert u == expected, e

    print('测试 apply 成功')


if __name__ == '__main__':
    main()

