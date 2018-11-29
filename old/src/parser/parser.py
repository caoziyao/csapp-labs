# coding: utf-8

from src.tokenizer.enum_token import Sign

# 语法分析器
# 这些 Token 将被 Parser（语法分析器）接收并进行进一步处理。
# Parser 处理结果称之为 Syntax Tree （语法树）

def pop_list(stack):
    """

    :param stack:
    :return:
    """
    l = []
    last = stack[-1]
    while True:
        if isinstance(last, list):
            l.append(stack.pop(-1))
            last = stack[-1]
        else:
            # if last.value != '[':
            if last.sub_type != Sign.bracketLeft:
                l.append(stack.pop(-1))
            else:
                stack.pop(-1)
                break
            last = stack[-1]
    # while last.value != '[':
    #     l.append(stack.pop(-1))
    #     last = stack[-1]
    # stack.pop(-1)
    l.reverse()
    return l


def parsed_ast_stack(token_list):
    """
    token: Enum
    用栈解析 ast
    """
    l = []
    i = 0
    while i < len(token_list):
        token = token_list[i]
        i += 1
        if token.value == ']':
            list_token = pop_list(l)
            l.append(list_token)
        else:
            l.append(token)
    return l

class Parser(object):

    def __init__(self, token_list):
        self.token_list = token_list
        self.current_token = None

    def parse(self):

        token_list = self.token_list
        ast = parsed_ast_stack(token_list)

        return ast


def parse_token(token_list):

    parser = Parser(token_list)
    ast = parser.parse()
    print('ast', ast)
    return ast
