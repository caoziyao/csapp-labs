# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/29 
@desc:
"""

from enum import Enum, unique, auto


@unique
class InstrY(Enum):
    halt = auto()       # 1	 Halts the system
    nop = auto()        # 1			No operation
    rrmovq = auto()     # 2	 ra rb  : rb -> ra
    irmovq = auto()     # 10 ra v   : v -> ra
    rmmovq = auto()     # 10 ra [a] : Moves the value of address a -> ra
    mrmovq = auto()     # 10 [a] ra : ra -> move value of address a
    OPq = auto()        # 2	rA, rB	See table 2
    jXX = auto()        # 9	Dest	See table 3
    call = auto()       # 9	Dest	Pushes the return address onto the stack and jumps to Dest
    ret = auto()        # 1		Returns from call
    pushq = auto()      # 2	rA	Same as x86-64
    popq = auto()       # 2	rA	Same as x86-64
    iOPq = auto()       # 10	V, rB	See table 2
    brk = auto()        # 1 Temporarily halts the system until the user manually starts it

    addq = auto()       # Adds rA to rB and stores it in rB
    subq = auto()       # Subtracts rA from rB and stores it in rB
    andq = auto()       # Ands rA and rB and stores it in rB
    xorq = auto()       # XORs rA and rB and stores it in rB
    iaddq = auto()      # Adds V to rB and stores it in rB
    isubq = auto()      # Subtracts V from rB and stores it in rB
    iandq = auto()      # Ands V and rB and stores it in rB
    ixorq = auto()      # XORs V and rB and stores it in rB

    jmp = auto()        # Jumps to Dest unconditionaly
    jle = auto()        # Jumps to Dest if (SF^OF)|ZF
    jl = auto()         # Jumps to Dest if SF^OF
    je = auto()         # Jumps to Dest if ZF
    jne = auto()        # Jumps to Dest if ~ZF
    jge = auto()        # Jumps to Dest if ~(SF^OF)
    jg = auto()         # Jumps to Dest if ~(SF^OF)&~ZF
