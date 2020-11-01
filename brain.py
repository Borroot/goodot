import random
import math


class Brain:

    def __init__(self, size, dirs=None):
        self.step = 0
        self.dirs = dirs if dirs is not None else \
                [self._random() for _ in range(size)]


    def _random(self):
        radians = random.uniform(0, 2 * math.pi)
        return (math.cos(radians), math.sin(radians))


    def clone(self):
        return Brain(len(self.dirs), self.dirs.copy())


    def mutate(self, minimum):
        brain = self.clone()
        rate = 0.10

        for i in range(minimum, len(self.dirs)):
            if random.random() < rate:
                brain.dirs[i] = self._random()
        return brain
