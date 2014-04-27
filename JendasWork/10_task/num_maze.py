#!/usr/bin/env python
import re


def loadMazeList(f_name):

    maze_list = []
    with open(f_name, "r") as f:
        separator = ":-]"
        while separator:
            maze = NumMaze(int(f.readline()))
            for row in xrange(maze.size):
                for column, value in enumerate(re.findall("\d+", f.readline())):
                    maze.grid[(row, column)] = [int(value), -1]
            maze_list.append(maze)
            separator = f.readline()
    return maze_list


class NumMaze():

    def __init__(self, size):

        self.size = size
        self.grid = {}
        self.directions = ((0, 1), (0, -1), (1, 0), (-1, 0))


    def findPath(self):

        active_vert = [(0, 0)]
        visited     = []
        paths       = {key:[[]] for key in self.grid}

        self.grid[(0, 0)][1] = 0

        next_fun = lambda jump, vert, dir_: tuple(map(lambda x, y: x + y*jump, vert, dir_))

        while active_vert:
            vert = active_vert.pop(0)
            jump = self.grid[vert][0]

            if not jump: continue

            for dir_ in self.directions:
                next_ = next_fun(jump, vert, dir_)
                add   = self.addNext (jump, vert, next_)
                if add:
                    self.grid[next_][1] = self.grid[vert][1] + jump
                    if add != "Equal":
                        active_vert.append(next_)
                        paths[next_] = [path + [vert] for path in paths[vert]]
                    else:
                        paths[next_].extend([path + [vert] for path in paths[vert]])


        last_coord = (self.size - 1, self.size - 1)
        print "Lowest possible sum: %d" % self.grid[last_coord][1]

        print "Possible paths: "
        for path in set([tuple(path) for path in paths[last_coord]]):
            print "     ", list(path) + [last_coord]
        print


    def addNext(self, jump, vert, next_):

        if next_ in self.grid:
            if self.grid[next_][1] == -1:
                return True
            if self.grid[vert][1] + jump < self.grid[next_][1]:
                return True
            if self.grid[vert][1] + jump == self.grid[next_][1]:
                return "Equal"
        return False


if __name__ == '__main__':
    
    maze_list = loadMazeList("ciselne-bludiste.txt")
    for maze in maze_list:
        maze.findPath()
