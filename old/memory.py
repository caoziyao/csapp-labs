# coding: utf-8


class Memory(object):

    def __init__(self):
        self._memory = []


    def get_memery(self, index):

        if index < len(self._memory):
            return self._memory[index]
        else:
            raise Exception('memery overflow')

    def process_program_mem(self):
        pass

    def process_control_mem(self):
        pass

    def process_code_mem(self):
        pass