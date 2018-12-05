# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/12/4 
@desc:
"""
import sys
import pygame
from graphics.ascii import ascii_map


class Graphics(object):

    def __init__(self, cpu=None):
        self.width = 256
        self.height = 240
        self.cpu = cpu

        scale = 1
        self.size = (self.width * scale, self.height * scale)
        self.screen = pygame.display.set_mode(self.size, 0, 32)

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)

        self.font_size = 5  # 1 2*2  3*3

    def exit(self):
        """

        :return:
        """
        sys.exit()

    def update(self):
        """

        :return:
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()

    def draw(self):
        """

        :return:
        """
        self.update()
        self.screen.fill(self.white)

        for h in range(self.height):
            for w in range(int(self.width / 2)):
                self.screen.set_at((h, w), self.black)

        pygame.display.flip()

    def _draw_block(self, start):
        """
        画区块
        :param start:
        :return:
        """
        scale = self.font_size

        for w in range(scale):
            for h in range(scale):
                x = start[0] + w
                y = start[1] + h
                self.screen.set_at((x, y), self.black)

    def draw_char(self, char, start=(0, 0)):
        """
        画字符
        :param char:
        :return:
        """
        codes = ascii_map.get(char, None)
        if codes is None:
            raise Exception('un support char {}'.format(char))

        self.update()
        self.screen.fill(self.white)
        scale = self.font_size

        for index, row in enumerate(codes):
            for i in range(8):
                col = (row >> (7 - i)) & 0x1
                if col == 1:
                    sw = start[0] + index * scale
                    sh = start[1] + i * scale
                    self._draw_block((sw, sh))

        pygame.display.flip()
