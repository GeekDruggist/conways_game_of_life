import random
from screen import Screen as sc


class Populate:
    def gen(num):
        return set([((random.randrange(0, sc.GRID_HEIGHT)), random.randrange(0, sc.GRID_WIDTH)) for _ in range(num)])
