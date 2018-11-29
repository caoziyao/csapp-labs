# coding: utf-8
from enum import Enum, unique


@unique
class EnumType(Enum):
    auto = 0            # auto 就是 6 个单字符
    colon = 1           # :
    comma = 2           # ,
    braceLeft = 3       # {
    braceRight = 4      # }
    bracketLeft = 5     # [
    bracketRight = 6    # ]
    number = 7          # 169
    string = 8          # "name"


