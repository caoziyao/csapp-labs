# coding: utf-8
from src.tokenizer import EnumType

# 状态机
class Tokenizer(object):
    pass


class Token(object):
    def __init__(self, token_type, token_value):
        super(Token, self).__init__()
        # 用表驱动发处理 if
        d = {
            ':': EnumType.colon,
            ',': EnumType.comma,
            '{': EnumType.braceLeft,
            '}': EnumType.braceRight,
            '[': EnumType.bracketLeft,
            ']': EnumType.bracketRight,
        }

        if token_type == EnumType.auto:
            self.type = d[token_value]
        else:
            self.type = token_type

        self.value = token_value


    def __repr__(self):
        s = 'type: {}, len: {}, value: {}'.format(self.type, len(str(self.value)), self.value)
        s = '"{}"'.format(self.value)
        return s