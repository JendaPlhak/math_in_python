#!/usr/bin/env python
import sys
sys.path.append("../3_task")
from Turtle    import Turtle
from itertools import product as prod
from random    import shuffle


hex_grid = {}
for i in xrange(10):
    for j in xrange(10):
        if (i + j) % 2 == 0:
            hex_grid[i+1j*j] = True
            sys.stdout.write("#")
        else:
            sys.stdout.write(" ")
    sys.stdout.write("\n")

direct = (2+0j, -2+0j, 1+1j, 1-1j, -1-1j, -1+1j)

for x in hex_grid:
    sys.stdout.write(str(x) + ": ")
    for dir_ in direct:
        if x + dir_ in hex_grid:
            sys.stdout.write(str(x + dir_) + ", ")
    print



class MazeGenerator(object):

    def __init__(self, n, k=4):

        self.grid  = {}
        self.walls = {}
        self.dirs  = [2+0j, -2+0j, 1+1j, 1-1j, -1-1j, -1+1j]

        for i in xrange(n):
            for j in xrange(n):
                if (i + j) % 2 == 0:
                    self.grid[i+1j*j] = True

        for field in self.grid:
            for dir_ in self.dirs:
                if field + dir_ in self.grid:
                    self.walls[(field, field + dir_)] = True

        self.visited = set()
        
        self.demolishWalls(0)

    def copyGrid(self):
        return {x:dict(self.grid[x]) for x in self.grid}

    def demolishWalls(self, node):
        
        self.visited.add(node)
        shuffle(self.dirs)
        for dir_ in self.dirs:
            if node + dir_ in self.grid and node + dir_ not in self.visited:
                if self.grid[node][dir_]:
                    cp = self.copyGrid()
                    cp[node][dir_]         = 0
                    cp[node + dir_][-dir_] = 0
                    if not self.cycle(cp):
                        self.grid = cp
                        self.demolishWalls(node + dir_)

    def cycle(self, grid):
        
        visited  = set()
        to_visit = set([(0, 1)])
        dirs     = set([1, 1j, -1, -1j])

        while to_visit:
            node = to_visit.pop()
            if node[0] in visited:
                return True
            else:
                for dir_ in dirs - set([-node[1]]):
                    if grid[node[0]][dir_] == 0:
                        to_visit.add((node[0] + dir_, dir_))
        return False


def plotMaze(grid, d=20):

    dirs = ((1, 1+1j), (1j, 1+1j), (0, 1j), (0, 1))
    draw = Turtle("SquareMaze", background=True)
    for square in grid:
        walls = grid[square]
        for i, dir_ in enumerate(dirs):
            if walls[1j**i]:
                draw.addLine((square + dir_[0])*d, (square + dir_[1])*d)

    draw.dumpImage()


if __name__ == '__main__':
    plotMaze(MazeGenerator(8).grid)