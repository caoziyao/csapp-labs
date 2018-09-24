global _GetRDTSC

section .text

_GetRDTSC:


mov     rax, 0x2000004 ; write
mov     rdi, 1 ; stdout
mov     rsi, msg
mov     rdx, msg.len
syscall

cpuid
rdtsc
shl   rdx, 32
or    rax, rdx

ret


section .data

msg:    db      "Hello, world!", 10
.len:   equ     $ - msg
