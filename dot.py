import pygame
import math

from brain import Brain
from colors import *
from helpers import add, dist, limit


class Dot:

    RADIUS = 5
    _MAX_VEL = 2


    def __init__(self, goal, start=None):
        width, height = pygame.display.get_surface().get_size()
        self._pos = start if start is not None else (width / 2, height - 50)
        self._vel = (0, 0)
        self._acc = (0, 0)

        self._start = start
        self._goal  = goal
        self.brain  = Brain(1500)

        self.isdead = False
        self.atgoal = False
        self.champion = False


    def _move(self):
        self._acc = add(self._acc, self.brain.dirs[self.brain.step])
        self.brain.step += 1
        self._vel = add(self._vel, self._acc)
        self._vel = limit(self._vel, Dot._MAX_VEL)
        self._pos = add(self._pos, self._vel)


    def _ingoal(self):
        return dist(self._pos, self._goal.pos) < 10


    def _insurf(self):
        width, height = pygame.display.get_surface().get_size()
        return Dot.RADIUS < self._pos[0] < width  - self.RADIUS \
           and Dot.RADIUS < self._pos[1] < height - self.RADIUS


    def _inobstacle(self, obstacles=None):
        if obstacles is None:
            return False
        return any([obstacle.collide(self._pos) for obstacle in obstacles])


    def update(self, obstacles=None):
        if not self.isdead and not self.atgoal:
            if self.brain.step < len(self.brain.dirs):
                self._move()
            else:
                self.isdead = True

            if not self._insurf() or self._inobstacle(obstacles):
                self.isdead = True
            if self._ingoal():
                self.atgoal = True


    def draw(self):
        surface = pygame.display.get_surface()
        color = GREEN if self.champion else BLACK
        pygame.draw.circle(surface, color, self._pos, Dot.RADIUS)


    def fitness(self):
        if self.atgoal:
            return 2 + 1 / (self.brain.step ** 2)
        else:
            return 1 / (dist(self._pos, self._goal.pos) ** 2)


    def clone(self):
        dot = Dot(self._goal, self._start)
        dot.brain = self.brain.clone()
        return dot


    def mutate(self, minimum=0):
        dot = Dot(self._goal, self._start)
        dot.brain = self.brain.mutate(minimum)
        return dot
