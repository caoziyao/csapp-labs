# coding: utf-8

from enum import Enum, unique



@unique
class Type(Enum):
    normal = 0          # 初始状态
    keyword = 1         # while if
    sign = 2            # +-*/={}[]
    identifier = 3      # 函数名，变量名，参数名
    number = 4          # 1234567890
    string = 5          # "hello lang"
    annotation = 6      # 注释
    space = 7           # 空格
    newline = 8         # 回车
    endsymbol = 9       # 终止符


@unique
class Keyword(Enum):
    """关键字"""
    auto = 0            # all
    k_var = 1           # var
    k_while = 2         # while
    k_if = 3            # if
    k_def = 4           # def
    k_elif = 5          # elif
    k_else = 6          # else
    k_when = 7          # when
    k_for = 8           # for
    k_try = 9           # try
    k_except = 10       # except
    k_null = 11         # null
    k_return = 12       # return
    k_continue = 13     # continue


@unique
class Sign(Enum):
    """符号"""
    auto = 0            # all
    colon = 1           # :
    comma = 2           # ,
    braceLeft = 3       # {
    braceRight = 4      # }
    bracketLeft = 5     # [
    bracketRight = 6    # ]
    number = 7          # 169
    string = 8          # "name"
    add = 9             # +
    sub = 10            # -
    mul = 11            # *
    div = 12            # /
    equal = 13          # =


@unique
class Identifier(Enum):
    """标示符
    则具体而言，就是用户定义的变量、函数定义中的函数名和参数名、被调用函数的函数名等等这些东西。
    """
    ident = 1


@unique
class String(Enum):
    """string"""
    string = 1


@unique
class Number(Enum):
    """number"""
    number = 1


# 语素 + 类型
class Token(object):
    def __init__(self, token_value, token_type):
        # 用表驱动发处理 if
        sign = {
            ':': Sign.colon,
            ',': Sign.comma,
            '{': Sign.braceLeft,
            '}': Sign.braceRight,
            '[': Sign.bracketLeft,
            ']': Sign.bracketRight,
            '+': Sign.add,
            '-': Sign.sub,
            '*': Sign.mul,
            '/': Sign.div,
            '=': Sign.equal,
        }

        keyword = {
            'var': Keyword.k_var,
            'while': Keyword.k_while,
            'if': Keyword.k_if,
            'else': Keyword.k_else,
        }

        if isinstance(token_type, Sign):
            self.type = Type.sign
            self.sub_type = sign[token_value]
        elif isinstance(token_type, Keyword):
            self.type = Type.keyword
            self.sub_type = keyword[token_value]
        elif isinstance(token_type, Identifier):
            self.type = Type.identifier
            self.sub_type = Identifier.ident
        elif isinstance(token_type, String):
            self.type = Type.string
            self.sub_type = String.string
        elif isinstance(token_type, Number):
            self.type = Type.number
            self.sub_type = Number.number
        else:
            print('undefined token type')

        self.value = token_value


    def __repr__(self):
        # s = 'type: {}, len: {}, value: {}'.format(self.type, len(str(self.value)), self.value)
        s = '"{}"'.format(self.value)
        return s


# # 关键字
# class KeyWord(object):
#     def __init__(self, key_type, key_value):
#         d = {
#             'set': EnumKeyWord.set
#         }
#         self.key = key_type
#         self.value = key_value
#
