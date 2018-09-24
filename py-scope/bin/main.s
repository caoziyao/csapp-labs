global start
    section .text

    start:
        mov rbx 2
        mov [a] rbx

        mov     rax, 0x2000001 ; exit
        mov     rdi, 0
        syscall
section .data
    vara  db ?