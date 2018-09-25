global _GetRDTSC

section .text

_GetRDTSC:

jmp L1
    ; user_ssize_t write(int fd, user_addr_t cbuf, user_size_t nbyte);
    ; %rax 作为函数返回值使用。
    ; %rsp 栈指针寄存器，指向栈顶
    ; %rdi，%rsi，%rdx，%rcx，%r8，%r9 用作函数参数，依次对应第1参数，第2参数。。。
    ; %rbx，%rbp，%r12，%r13，%14，%15 用作数据存储，遵循被调用者使用规则，简单说就是随便用，调用子函数之前要备份它，以防他被修改
    ; %r10，%r11 用作数据存储，遵循调用者使用规则，简单说就是使用之前要先保存原值
L1:
    mov     rax, 0x2000004 ; write
    mov     rdi, 1 ; stdout
    mov     rsi, msg
    mov     rdx, msg.len
    syscall

; L2:
;     mov     rax, 0x2000004 ; write
;     mov     rdi, 1 ; stdout
;     mov     rsi, mk
;     mov     rdx, 3
;     syscall

exit:
    mov     rax, 0x2000001 ; exit
    mov     rdi, 0
    syscall


section .data
msg:    db      "hello jjs"
.len:   equ     $ - msg
; mk:    db      "abc"


; mov     rax, 0x2000004 ; write
; mov     rdi, 1 ; stdout
; mov     rsi, msg
; mov     rdx, msg.len
; syscall
;
; ret
;
;
; section .data
;
; msg:    db      "Hello, world!", 10
; .len:   equ     $ - msg
