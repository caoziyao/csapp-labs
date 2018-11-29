# coding: utf-8

from src.tokenizer.enum_token import Type, Keyword, Sign
from src.generate_ir.compiler_compiler import Expression, VarExpression

"""
[ var a = 1]
[ var b = 2 + 4]
"""
def is_leaf(exp):

    l = exp.node
    for item in l:
        if isinstance(item, list):
            return False

    return True


def process_var(exp, node, i):
    first = VarExpression(node[:i - 1])
    exp.first = first

    secode = VarExpression(node[i:])
    exp.second = secode

    if not is_leaf(exp.first):
        first.is_leaf = False
        var_expression_end(exp.first, exp.first.node)

    if not is_leaf(exp.second):
        secode.is_leaf = False
        var_expression_end(exp.second, exp.second.node)

def var_expression_end(exp, node):


    i = 0

    while i < len(node):
        t = node[i]
        i += 1
        if isinstance(t, list) and len(node) != 1:
            continue
        if isinstance(t, list) and len(node) == 1:
            var_expression_end(exp, node[0])
        elif t.sub_type == Sign.equal:
            process_var(exp, node, i)
            exp.op = Sign.equal
            break
        elif t.sub_type == Sign.add:
            process_var(exp, node, i)
            exp.op = Sign.add
            break
        elif t.sub_type == Sign.sub:
            process_var(exp, node, i)
            exp.op = Sign.sub
            break
        elif t.sub_type == Sign.mul:
            process_var(exp, node, i)
            exp.op = Sign.mul
            break
        elif t.sub_type == Sign.div:
            process_var(exp, node, i)
            exp.op = Sign.div
            break

    return exp





def expression_end(node):

    first = node[0]
    if first.type == Type.keyword:
        if first.sub_type == Keyword.k_var:
            var_exp = VarExpression(node[1:])
            var_exp = var_expression_end(var_exp, var_exp.node)
            return var_exp
    print('error end')

def lookup(root):
    stack = [root]
    while stack:
        current = stack.pop(0)
        print(current.data)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

def proecess_leaf():
    pass

def ouput_ir_code(exp):

    stack = [exp]
    res = []
    n = 0
    m = n + 1
    while stack:
        current = stack.pop(0)
        if current.first.is_leaf:
            if not current.second.is_leaf:
                ident = current.first.node[0]
                op = current.op.name
                s = '${} -> {} {} ${}'.format(n, ident, op,  m)
                n += 1
                m = n + 1
                res.append(s)
        else:
            stack.append(current.first)

        if current.second.is_leaf:
            if not current.first.is_leaf:
                ident = current.second.node[0]
                op = current.op.name
                s = '${} -> {} {} ${}'.format(n, ident, op , m)
                n += 1
                m = n + 1
                res.append(s)
        else:
            stack.append(current.second)

        if current.second.is_leaf and current.first.is_leaf:
            ident1 = current.first.node[0]
            ident2 = current.second.node[0]
            op = current.op.name
            s = '${} -> {} {} {}'.format(n, ident1, op, ident2)
            n += 1
            m = n + 1
            res.append(s)

    res.reverse()
    print('res', res)
    return res


def generate_ir(ast):

    l = []
    for node in ast:
        token = node[0]
        if token.type == Type.keyword and token.sub_type == Keyword.k_var:
            var_exp = expression_end(node)
            var_exp.is_leaf = False
            l.append(var_exp)

    r = []
    for each in l:
        code = ouput_ir_code(each)
        r.append(code)

    return r