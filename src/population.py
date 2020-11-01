import pygame
import random


from dot import Dot


class Population:

    def __init__(self, goal, size, start=None):
        self._dots = [Dot(goal, start) for _ in range(size)]
        self.gen = 0


    def update(self, obstacles=None):
        for dot in self._dots:
            dot.update(obstacles)


    def draw(self):
        for dot in self._dots:
            dot.draw()


    def isdead(self):
        return all(dot.isdead or dot.atgoal for dot in self._dots)


    def _champion(self):
        fitness = [dot.fitness() for dot in self._dots]
        return self._dots[fitness.index(max(fitness))]


    def _parent(self):
        fitness = [dot.fitness() for dot in self._dots]

        interval = random.uniform(0, sum(fitness))
        current = index = 0
        while current < interval:
            current += fitness[index]
            index += 1

        return self._dots[index - 1]


    def evolve(self):
        print(sum(1 for dot in self._dots if dot.atgoal), '\t', end='')
        print(self._dots[0].brain.step)

        self.gen += 1
        minimum = max(0, self._dots[0].brain.step - 100)

        self._dots[0] = self._champion().clone()
        self._dots[0].champion = True

        for i in range(1, len(self._dots) // 2):
            self._dots[i] = self._dots[0].mutate(minimum)

        for i in range(len(self._dots) // 2, len(self._dots)):
            self._dots[i] = self._parent().mutate(minimum)
