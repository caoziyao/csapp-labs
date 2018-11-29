# coding: utf-8

from src.parser.parser import parse_token
from src.tokenizer.token_parse import token_list
from src.utils.util import read_file
from src.generate_ir.ir import generate_ir
from src.codegen.machie import generate_asm

"""
    [+ 1 2]         ; 表达式的值是 3
    [* 2 3 4]       ; 表达式的值是 24
    [log "hello"]   ; 输出 hello, 表达式的值是 null(关键字 表示空)
    [+ 1 [- 2 3]]   ; 表达式的值是 0, 相当于普通语法的 1 + (2 - 3)
    [if [> 2 1] 3 4]; 表达式的值是 3
    [if yes
        [log "成功"]
        [log "没成功"]
    ]
"""

def main():
    path = 'main.lang'
    code = read_file(path)
    ts = token_list(code)
    ast = parse_token(ts)

    ir = generate_ir(ast)
    asm = generate_asm(ir)

    print('ir', asm)


if __name__ == '__main__':
    main()