# coding: utf-8

from enum import Enum, unique

@unique
class EnumVerbosity(Enum):
    # 在unittest.main()中加 verbosity 参数
    # 默认是 1，如果设为 0，则不输出每一用例的执行结果，即没有上面的结果中的第1行；如果设为 2，则输出详细的执行结果，如下：
    none = 0
    default = 1
    detail = 2
