# coding: utf-8

"""
把 字符串 解析 token 列表
"""
from src.tokenizer import EnumType
from src.tokenizer import Token
from src.utils import read_file, log


def number_end(code):
    digits = '0123456789'
    end = 0
    for offset, char in enumerate(code):
        if char not in digits:
            end = offset
            break
    return end - 1


def string_end(code, index):
    """
    code = "abc"
    index = 1
    """
    s = ''
    offset = index
    while offset < len(code):
        c = code[offset]
        if c == '"':
            # 找到了字符串的结尾
            # s = code[index:offset]
            return s, offset
        elif c == '\\':
            # 处理转义符号 '\'
            if code[offset+1] == '"':
                s += '"'
                offset += 2
            else:
                # 这是一个错误， 非法转义符号
                pass
        else:
            s += c
            offset += 1

    print('error')
    # 程序出错，没找到 引号"


def json_tokens(code):
    length = len(code)
    tokens = []

    spaces = '\n\t\r'
    digits = '0123456789'
    # 当前下标
    i = 0
    while i < length:
        # 先看看当前应该处理啥
        c = code[i]
        i += 1
        # 空白符号要跳过
        if c in spaces:
            continue
        elif c in ':,{}[]':
            # 处理 6 种单个符号
            t = Token(EnumType.auto, c)
            tokens.append(t)
        elif c == '"':
            # 处理字符串
            s, offset = string_end(code, i)
            i = offset + 1
            t = Token(EnumType.string, s)
            tokens.append(t)
        elif c in digits:
            # 处理数字
            end = number_end(code[i-1:])
            n = code[i-1:i+end]
            i += end
            #   "name\"e": "abc"
            t = Token(EnumType.number, n)
            tokens.append(t)
            pass
        else:
            # 出错了
            pass

    # def __repr__(self):
    #     return
    print('token', tokens)

def main():
    path = 'test.json'
    code = read_file(path)
    ts = json_tokens(code)
    log('ts', ts)


if __name__ == '__main__':
    main()