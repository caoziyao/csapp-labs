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


class Graphics(object):

    def __init__(self, cpu=None):
        self.width = 256
        self.height = 240

        self.cpu = cpu

        scale = 1
        self.size = (self.width * scale, self.height * scale)
        self.screen = pygame.display.set_mode(self.size, 0, 32)

        self.black = (0, 0, 0)

    def exit(self):
        sys.exit()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()

    def draw(self):
        self.update()

        self.screen.fill(self.black)

        for h in range(self.height):
            for w in range(int(self.width / 2)):
                self.screen.set_at((h, w), (255, 0, 0))

        pygame.display.flip()
