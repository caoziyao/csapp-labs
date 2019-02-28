# coding: utf-8


class Quads(object):
    index = 0
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Quads, cls).__new__(cls, *args, **kw)
        return cls._instance

    def tmp_var(self):
        t = '#{}'.format(self.index)
        self.index += 1
        return t
