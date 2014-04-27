from AStar import AStar, AStarNode
import sys


class AStarLTNode(AStarNode): # AStart no Left Turn Node

    def __init__(self, dir_, coord):
        self.dir   = dir_
        self.coord = coord
        AStarNode.__init__(self)

    def __hash__(self):
        return hash((self.coord, self.dir))

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def move_cost(self, target):

        if self.coord + self.dir == target.coord:
            return 1
        else:
            return 2


class AStarLT(AStar): # AStart no Left Turn class

    def __init__(self, map_):
        self.map = map_

    def endReached(self, node, end):
        """
        Test for target destination.
        """
        return node.coord == end.coord

    def heuristic(self, node):
        diff = node.coord - end.coord
        return abs(diff.real) + abs(diff.imag)

    def neighbours(self, node):

        neigh = []
        for rotate in (1, 1j):
            new_dir = node.dir * rotate
            coord   = node.coord + new_dir
            if coord in self.map:
                neigh.append(AStarLTNode(new_dir, coord))
        return neigh



if __name__ == '__main__':
    
    map_ = set()
    with open("mazes/left_maze.txt", 'r') as f:
        for row, line in enumerate(f):
            for col, symbol in enumerate(line):
                coord = col + 1j*row

                if symbol == ' ':
                    map_.add(coord)
                elif symbol == '+':
                    map_.add(coord)
                    end = AStarLTNode(0, coord)
                elif symbol in ['<', '>', '^', 'v']:
                    map_.add(coord)
                    dir_  = {'>':1, 'v':1j, '<':-1, '^':-1j}[symbol]
                    start = AStarLTNode(dir_, coord)
                else:
                    if symbol != '#' and symbol != '\n':
                        print "Unknown symbol '%s' will be considered a wall" % symbol

    path = AStarLT(map_).search(start, end)
    path = [x.coord for x in path]

    with open("mazes/left_maze.txt", 'r') as f:
        for row, line in enumerate(f):
            for col, symbol in enumerate(line):
                if col + 1j*row in path and symbol not in ['+', '<', '>', '^', 'v']:
                    sys.stdout.write(".")
                else:
                    sys.stdout.write(symbol)