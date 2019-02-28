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

    array = 33  # array
    array_access = 34  # array

    undefind = 101  # undefind
    # condition = 102  # if else

    print = 103  # print

    # # register todo
    # mov = 201
    # ldrb = 202
    # ldr = 203
    # strb = 204
    # str = 205
    #
    # push = 206
    # pop = 207
    #
    # call = 208
    # ret = 209
    #
    # jmp = 210
    # jmpn = 211
    # jmpz = 212
    # jmpo = 213
    #
    # comp = 214
    # cjmp = 215