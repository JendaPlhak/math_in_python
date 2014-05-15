#!/usr/bin/env python
import sys
sys.path.append("../3_task")
from Turtle    import Turtle
from itertools import product as prod
from random    import shuffle, randint, choice

def copyGrid(grid):
    return {x:dict(grid[x]) for x in grid}

class PerfectMazeGenerator(object):

    def __init__(self, n):

        roots = {1j**k:1 for k in xrange(4)}
        self.grid    = { i+1j*j:dict(roots) for i in xrange(n) for j in xrange(n) }
        self.visited = set()
        self.dirs    = [1, 1j, -1, -1j]
        self.demolishWalls(0)


    def demolishWalls(self, node):
        
        self.visited.add(node)
        shuffle(self.dirs)
        for dir_ in self.dirs:
            if node + dir_ in self.grid and node + dir_ not in self.visited:
                if self.grid[node][dir_]:
                    cp = copyGrid(self.grid)
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


class braidMazeGenerator(object):

    def __init__(self, n):

        self.n = n
        roots        = {1j**k:False for k in xrange(4)}
        self.grid    = { i+1j*j:dict(roots) for i in xrange(n) for j in xrange(n) }
        self.visited = set()
        self.dirs    = [1, 1j, -1, -1j]

        self.createOuterWall()
        self.randomWallToEveryVertex()
        self.randomAdding()


    def createOuterWall(self):

        n = self.n
        for i, y in enumerate([0, n-1]):
            dir_ = 1j * (-1)**(i+1)
            for x in xrange(n):
                self.grid[x + y*1j][dir_] = True

        for i, x in enumerate([0, n-1]):
            dir_ = (-1)**(i+1)
            for y in xrange(n):
                self.grid[x + y*1j][dir_] = True


    def randomWallToEveryVertex(self):

        for x in xrange(1, self.n, 2):
            for y in xrange(1, self.n, 2):
                shift = choice([0, -1-1j])
                node  = x + y*1j + shift
                if shift:
                    randir = choice([1j, 1])
                else:
                    randir = choice([-1j, -1])
                if not node in self.grid or node + randir not in self.grid:
                    continue
                self.grid[node][randir] = True    
                self.grid[node + randir][-randir] = True

    def randomAdding(self):

        for node, dir_ in self.randomNodes():

            if self.grid[node][dir_]:
                continue
            if node + dir_ not in self.grid: continue

            cp = copyGrid(self.grid)
            cp[node][dir_]         = True
            cp[node + dir_][-dir_] = True

            if not self.deadEnd(node, cp)      and \
               not self.deadEnd(node+dir_, cp) and \
               self.path(node, node+dir_, cp):
                self.grid = cp

    def deadEnd(self, node, grid):

        w = 0
        for dir_ in self.dirs:
            if grid[node][dir_]:
                w += 1
        if w < 3:
            return False
        else:
            return True


    def path(self, start, target, grid):
        
        to_visit = [start]
        visited  = set()

        while to_visit:
            node = to_visit.pop(0)
            visited.add(node)

            for dir_ in self.dirs:
                if not grid[node][dir_]:
                    next_node = node + dir_
                    if next_node == target:
                        return True
                    if next_node not in visited:
                        to_visit.append(next_node)

        return False

    def randomNodes(self):

        sample = []
        for x in xrange(self.n):
            for y in xrange(self.n):
                for dir_ in self.dirs:
                    sample.append((x+1j*y, dir_))
        shuffle(sample)
        return sample


def plotMaze(grid, d=20, name="SquareMaze"):

    dirs = ((1, 1+1j), (1j, 1+1j), (0, 1j), (0, 1))
    draw = Turtle(name, background=True)
    for square in grid:
        walls = grid[square]
        for i, dir_ in enumerate(dirs):
            if walls[1j**i]:
                draw.addLine((square + dir_[0])*d, (square + dir_[1])*d)

    draw.dumpImage()


if __name__ == '__main__':
    plotMaze(braidMazeGenerator(33).grid,   20, "BraidMaze")
    plotMaze(PerfectMazeGenerator(35).grid, 20, "PerfectMaze")