import pygame
from pygame.locals import *
import time

from population import Population
from dot import Dot
from goal import Goal
from obstacle import Obstacle
from levels import *
from colors import *


def _draw(obstacles, goal, population):
    pygame.display.get_surface().fill(WHITE)

    for obstacle in obstacles:
        obstacle.draw()
    goal.draw()
    population.draw()

    pygame.display.update()


def main():
    pygame.init()
    pygame.display.set_caption('Evolution!')

    pygame.display.set_mode((500, 700))

    obstacles = LEVEL2
    goal = Goal()
    population = Population(goal, 200)

    finished = False
    while not finished:
        if population.isdead():
            population.evolve()

        population.update(obstacles)
        _draw(obstacles, goal, population)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                finished = True


if __name__ == '__main__':
    main()
