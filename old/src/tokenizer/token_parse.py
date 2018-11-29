# coding: utf-8

"""
词法分析器
把 字符串 解析 token 列表
语素 + 类型
"""
from src.tokenizer.enum_token import Token, Type, String, Sign,\
    Number, Keyword, Identifier
from src.utils.util import read_file, log


def number_end(code):
    digits = '0123456789'
    end = 0
    for offset, char in enumerate(code):
        if char not in digits:
            end = offset
            break
    return end - 1


def keyword_set_end(code):
    """
    解析 set 关键字
    code： set a 1
    """
    digits = '0123456789'
    i = 3
    num_of_arg = 2
    arg = 0
    var = ''
    num = ''
    res = ['set']
    var_end = False
    num_end = False
    while i < len(code):
        c = code[i]
        i += 1
        if arg == num_of_arg:
            break
        if c.isalpha():
            var += c
        elif c in digits:
            num += c
        elif c == ' ':
            continue
        else:
            if var_end == False:
                var_end = True
                res.append(var)
            if num_end == False:
                num_end = True
                res.append(num)
            arg += 1

    if var == '' or num == '':
        log('error keyword_set_end')
        return 1
    else:
        return i - 3, res


def keyword_end(code):
    if code[:3] == 'set':
        end, res = keyword_set_end(code)
        return end, res
    else:
        return 1


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
            if code[offset + 1] == '"':
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


def pre_process(code):
    # 把输入串预处理一下。预处理主要滤掉空格，跳过注释、换行符等。
    code = code.strip()

    return code


def variable_end(code, index):
    """
        code = "abc"
        index = 1
        """
    s = ''
    offset = index
    while offset < len(code):
        c = code[offset]
        if c == ' ':
            # 找到了字符串的结尾
            # s = code[index:offset]
            return s, offset
        else:
            s += c
            offset += 1

    print('error')


def keyword_ident_end(code):
    for k_key in Keyword.__members__.keys():
        key = k_key.split('_')[-1]
        len_key = len(key)
        k = code[:len_key]
        if k == key and code[len_key] == ' ':
            return len_key, Keyword[k_key]

    i = 0
    while i < len(code):
        c = code[i]
        i += 1
        if c == ' ':
            return i-1, Identifier.ident

    print('error keyword_ident_end')


# 状态机
# 状态机不断从源代码（即一个字符串）中读入一个一个字符，读到不同的字符将使状态机的状态从一个状态变化到另外一个状态。
class Tokenizer(object):
    def __init__(self, source):
        self.source = source
        self.status = Type.normal
        self.token_list = []

    def lexical_analysis(self):
        length = len(self.source)
        tokens = []
        code = self.source
        digits = '0123456789'
        spaces = ' \n\t\r'
        # 当前下标
        i = 0
        while i < length:
            # 先看看当前应该处理啥
            c = code[i]
            i += 1
            # 空白符号要跳过
            if c in spaces:
                continue
            elif c in ':,{}[]+-*/=':
                # 处理 6 种单个符号
                t = Token(c, Sign.auto)
                tokens.append(t)
            elif c == '"':
                # 处理字符串
                s, offset = string_end(code, i)
                i = offset + 1
                t = Token(s, String.string)
                tokens.append(t)
            elif c in digits:
                # 处理数字
                end = number_end(code[i - 1:])
                n = code[i - 1:i + end]
                i += end
                #   "name\"e": "abc"
                t = Token(n, Number.number)
                tokens.append(t)
            else:
                # keyword or identifier
                end, _type = keyword_ident_end(code[i - 1:])
                n = code[i - 1:i + end - 1]
                i += end
                t = Token(n, _type)
                tokens.append(t)

        return tokens

    def read_next(self):
        pass


def token_list(code):
    # 预处理
    source = pre_process(code)

    ter = Tokenizer(source)
    token_list = ter.lexical_analysis()
    print('token_list', token_list)
    return token_list


def token_parse_test():
    path = 'main.lang'
    code = read_file(path)
    ts = token_list(code)
    log('ts', ts)


def main():
    token_parse_test()


if __name__ == '__main__':
    main()
