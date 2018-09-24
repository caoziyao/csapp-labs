global start
        section .text

        start:
           

            mov     rax, 0x2000001 ; exit
            mov     rdi, 0
            syscall
        section .data