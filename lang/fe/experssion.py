# coding: utf-8

from enum import Enum, unique


# 数据结构
@unique
class Kind(Enum):
    number = 0  # 0-9
    plus = 1  # +
    times = 2
    minus = 3
    div = 4
    operator = 5  # 操作符 +-*/
    is_more_then = 6  # >
    is_less_then = 7  # <

    id = 21  # id
    assignment = 22  # 赋值
    string = 23  # string
    var = 24  # var
    true = 25  # true
    false = 26  # false
    k_if = 27  # if
    kwhile = 28  # while
    kwhile_start = 29  # while start
    kdef = 30  # def
    kdef_name = 31  # def start
    kdef_end = 32  # def end

    undefind = 101  # undefind
    # condition = 102  # if else

    print = 103  # print

    # register todo
    mov = 201
    ldrb = 202
    ldr = 203
    strb = 204
    str = 205

    push = 206
    pop = 207

    call = 208
    ret = 209

    jmp = 210
    jmpn = 211
    jmpz = 212
    jmpo = 213

    comp = 214
    cjmp = 215


class Number(object):

    def __init__(self, value):
        self.type = Kind.number  # enum Kind
        self.value = value
        self.left = None
        self.right = None

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        # for child in self.children:
        return ret


class TRUE(object):

    def __init__(self, value):
        self.type = Kind.true  # enum Kind
        self.value = value
        self.left = None
        self.right = None

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        # for child in self.children:
        return ret


class FALSE(object):

    def __init__(self, value):
        self.type = Kind.false  # enum Kind
        self.value = value
        self.left = None
        self.right = None

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        # for child in self.children:
        return ret


class ID(object):

    def __init__(self, value):
        self.type = Kind.id  # enum Kind
        self.value = value
        self.left = None
        self.right = None

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        # for child in self.children:
        return ret


class VAR(object):

    def __init__(self):
        self.type = Kind.var  # enum Kind
        self.value = 'var'
        self.left = None
        self.right = None

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        # for child in self.children:
        return ret


class UNDEFIND(object):

    def __init__(self):
        self.type = Kind.undefind  # enum Kind
        self.value = 'undefind'
        self.left = None
        self.right = None

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        # for child in self.children:
        return ret


class STRING(object):

    def __init__(self, value):
        self.type = Kind.string  # enum Kind
        self.value = value
        self.left = None
        self.right = None

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        # for child in self.children:
        return ret


class PRINT(object):

    def __init__(self, value):
        self.type = Kind.print  # enum Kind
        self.value = value
        self.left = None
        self.right = None

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        # for child in self.children:
        return ret


########################

class Node(object):

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.type.name) + "\n"
        ret += self.left.__str__(level + 1)
        ret += self.right.__str__(level + 1)
        return ret


class BinOp(Node):

    def __init__(self, left, right):
        self.type = Kind.operator  # enum Kind
        self.left = left  # class Exp
        self.right = right  # class Exp


class ExprPlus(Node):

    def __init__(self, left, right):
        self.type = Kind.plus
        self.left = left  # class Exp
        self.right = right  # class Exp


class ExprMinus(Node):

    def __init__(self, left, right):
        self.type = Kind.minus
        self.left = left  # class Exp
        self.right = right  # class Exp


class ExprTimes(Node):

    def __init__(self, left, right):
        self.type = Kind.times
        self.left = left  # class Exp
        self.right = right  # class Exp


class ExprDiv(Node):

    def __init__(self, left, right):
        self.type = Kind.div
        self.left = left  # class Exp
        self.right = right  # class Exp


# class ExprAssignment(Node):
#
#     def __init__(self, left, right):
#         self.type = Kind.assignment
#         self.left = left  # class Exp
#         self.right = right  # class Exp


class ExprPrint(Node):

    def __init__(self, left, right):
        self.type = Kind.print
        self.left = left  # class Exp
        self.right = right  # class Exp


class ExprVar(Node):

    def __init__(self, left, right):
        self.type = Kind.var
        self.left = left  # class Exp
        self.right = right  # class Exp


class ExprCondition(Node):
    """
    if
    """

    def __init__(self, condition, left, right):
        self.type = Kind.k_if
        self.condition = condition
        self.left = left  # class Exp
        self.right = right  # class Exp

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.type.name) + "\n"
        ret += self.condition.__str__(level + 1)
        ret += self.left.__str__(level + 1)
        ret += self.right.__str__(level + 1)
        return ret


class ExprWhile(Node):
    """ while """

    def __init__(self, condition, body):
        self.type = Kind.kwhile
        self.condition = condition
        self.body = body  # class Exp

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.type.name) + "\n"
        ret += self.condition.__str__(level + 1)
        ret += self.body.__str__(level + 1)
        return ret


class ExprIsMoreThen(Node):

    def __init__(self, left, right):
        self.type = Kind.is_more_then
        self.left = left  # class Exp
        self.right = right  # class Exp


class ExprIsLessThen(Node):

    def __init__(self, left, right):
        self.type = Kind.is_less_then
        self.left = left  # class Exp
        self.right = right  # class Exp


class ExprDef(Node):

    def __init__(self, func_name, args, body):
        self.type = Kind.kdef
        self.func_name = func_name
        self.args = args
        self.body = body


class ExprCall(Node):

    def __init__(self, func_name, args):
        self.type = Kind.call
        self.func_name = func_name
        self.args = args
