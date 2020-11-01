import math


def add(tuple1, tuple2):
    return tuple(sum(x) for x in zip(tuple1, tuple2))


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def limit(vector, magnitude):
    current = math.sqrt(sum(element ** 2 for element in vector))
    if current > magnitude:
        return tuple(map(lambda x: x / (current / magnitude), vector))
    return vector
