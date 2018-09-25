
global start
section .text

start:
   
        mov     rax, 0x2000004 ; write
        mov     rdi, 1 ; stdout
        mov     rsi, msg
exit:
    mov     rax, 0x2000001 ; exit
    mov     rdi, 0
    syscall
section .data
    msg:    db      "hello js", 10
    .len:   equ     $ - msg

        mov     rdx, msg.len
        syscall
    
