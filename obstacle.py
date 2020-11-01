import pygame

from colors import *
from dot import Dot


class Obstacle:

    def __init__(self, pos, size):
        self._pos  = pos
        self._size = size


    def collide(self, pos):
        return self._pos[0] - Dot.RADIUS < pos[0] < self._pos[0] + self._size[0] + Dot.RADIUS \
           and self._pos[1] - Dot.RADIUS < pos[1] < self._pos[1] + self._size[1] + Dot.RADIUS


    def draw(self):
        surface = pygame.display.get_surface()
        rect = pygame.Rect(self._pos, self._size)
        pygame.draw.rect(surface, BLACK, rect)
