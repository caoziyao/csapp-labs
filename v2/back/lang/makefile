
all:
	nasm -f macho64 bin/main.s
	ld -macosx_version_min 10.7.0 -o bin/main bin/main.o

run:
	./bin/main
