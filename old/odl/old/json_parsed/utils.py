# coding: utf-8


def log(*args, **kwargs):
    print(*args, **kwargs)

def read_file(path):

    with open(path, 'r') as f:
        return f.read()