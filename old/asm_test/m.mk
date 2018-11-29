nasm -f macho 1.asm -g
ld -macosx_version_min 10.7.0 -o 1 1.o
