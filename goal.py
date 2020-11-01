import pygame

from colors import *


class Goal:

    _RADIUS = 7


    def __init__(self, pos=None):
        width, height = pygame.display.get_surface().get_size()
        self.pos = pos if pos is not None else (width / 2, 50)


    def draw(self):
        surface = pygame.display.get_surface()
        pygame.draw.circle(surface, RED, self.pos, Goal._RADIUS)
