#!/usr/bin/env python
from AStar        import AStar, AStarNode
from plot_sokoban import plotPath


class AStarSokNode(AStarNode): # AStart Sokoban node

    def __init__(self, sokoban, boxes, dir_, new_box):

        self.dir      = dir_ 
        self.new_box  = new_box
        self.boxes    = boxes
        self.sokoban  = sokoban
        self.orig_sok = sokoban
        self.hash     = hash((self.sokoban, tuple(self.boxes)))
        AStarNode.__init__(self)

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def move_cost(self, target):
        score = 1
        if self.new_box != target.orig_sok:
            score += 0.2
        if self.dir != target.dir:
            score += 0.1
        return score

    def sokobanLeftMost(self, map_):
        """
        Apply BSD to find left-most top corner to place sokoban
        and also find all possible box shifts
        """
        unseen   = set([self.sokoban])
        seen     = set()
        posShift = set()
        LTM      = self.sokoban # LeftTopMost
        dirs     = (1, 1j, -1, -1j)

        while unseen:
            coord = unseen.pop()
            seen.add(coord)
            for dir_ in dirs:
                new_coord = coord + dir_
                if new_coord in map_:

                    if new_coord in self.boxes:
                        if new_coord + dir_ in map_ and new_coord + dir_ not in self.boxes:
                            posShift.add((new_coord, new_coord + dir_))

                    elif self.isMoreLeft(new_coord, LTM):
                        LTM = new_coord
                        if not new_coord in seen:
                            unseen.add(new_coord)
                    elif new_coord not in seen:
                        unseen.add(new_coord)

        self.sokoban  = LTM
        return posShift


    def isMoreLeft(self, coord, LTM):

        if coord.real < LTM.real:
            return True
        elif coord.real == LTM.real and\
             coord.imag < LTM.imag:
             return True

        return False



class AStarSok(AStar): 

    def __init__(self, map_, targets, sokoban):

        self.map       = map_
        self.targets   = targets
        self.dirs      = (1, 1j, -1, -1j)
        self.deadLocks = set()
        print "Preprocessing..."
        self.removeUnreachable(sokoban)
        self.loadDeadLocks()
        self.digTunnels()
        print "     Done!"

    def removeUnreachable(self, sokoban):
        """
        Remove all unreachable coordinates.
        """
        unseen = set([sokoban])
        seen   = set()

        while unseen:
            coord = unseen.pop()
            seen.add(coord)
            for dir_ in self.dirs:
                new_coord = coord + dir_
                if new_coord in self.map and\
                   new_coord not in seen:
                    unseen.add(new_coord)
        self.map = seen


    def loadDeadLocks(self):
        """
        Locate all simple dead-locks. That
        means all corners and fields between corners
        """
        # First, locate all corners
        for coord in self.map:
            if coord in self.targets:
                continue
            wall = False
            for dir_ in list(self.dirs) + [1]:
                if coord + dir_ not in self.map:
                    if wall:
                        self.deadLocks.add(coord)
                        break
                    wall = True
                else:
                    wall = False

        # Than eliminate all by-wall-paths between two corners
        corners = set(self.deadLocks)
        for corner in corners:
            for dir_ in self.dirs:
                path  = []
                coord = corner + dir_

                while coord in self.map:
                    if coord in corners:
                        for x in path: self.deadLocks.add(x)
                        break
                    if coord in targets:
                        break
                    if coord + 1j*dir_ in self.map and coord - 1j*dir_ in self.map:
                        break
                    path.append(coord)
                    coord += dir_


    def digTunnels(self):
        """
        Create teleports from entrance of tunnel
        to its end.
        """
        self.between_wals = []
        for coord in (self.map - self.deadLocks) - self.targets:
            for a, b in [(coord + 1,coord - 1), (coord + 1j, coord - 1j)]:
                if (a not in self.map or a in self.deadLocks) and \
                   (b not in self.map or b in self.deadLocks):
                   self.between_wals.append(coord)
                   break

        self.tunnels = {}
        for coord in self.between_wals:
            for dir_ in (1, 1j):
                start = coord
                end   = coord
                path  = set([start])
                while start - dir_ in self.between_wals:
                    start -= dir_
                    path.add(start)
                while end + dir_ in self.between_wals:
                    end += dir_
                    path.add(end)
                if start != end and not path & self.targets:
                    self.tunnels[start] = end 
                    self.tunnels[end]   = start
                    break


    def endReached(self, node, end):
        """
        Test for target destination.
        """
        for box in end.boxes:
            if box not in node.boxes:
                return False
        return True


    def heuristic(self, node):
        """
        Estimated distance between node and target
        position.
        """
        dist = 0
        for box in node.boxes:
            dist_list = []
            for target in self.targets:
                diff = box - target
                dist_list.append(abs(diff.real) + abs(diff.imag))
            dist += min(dist_list)
        return dist


    def neighbours(self, node):
        """
        Find all possible moves for given node
        """
        neigh = []
        posShift = node.sokobanLeftMost(self.map)
        for PS in posShift:       # PS[0] = from, PS[1] = to
            if PS[1] in self.deadLocks: 
                continue
            new_boxes = set(node.boxes)
            new_boxes.remove(PS[0])
            if PS[1] in self.tunnels:
                new_box = self.tunnels[PS[1]]
                sokoban = new_box - (PS[1] - PS[0])
            else:
                new_box = PS[1]
                sokoban = PS[0]
            new_boxes.add(new_box)
            neigh.append(AStarSokNode(sokoban, new_boxes, PS[1] - PS[0], new_box))
        return neigh


def mazeFileIterator(f):

    for row, line in enumerate(f):
        for col, symbol in enumerate(line):
            if symbol != '\n':
                yield symbol, col + 1j*row


if __name__ == '__main__':
    
    map_    = set()
    targets = set()
    boxes   = set()
    maze    = []

    with open("../mazes/sokoban.txt", 'r') as f:
        for symbol, coord in mazeFileIterator(f):
            maze.append((symbol, coord))
            if symbol in [' ', '@', '.', '$']:
                map_.add(coord)
                if symbol == '@':
                    sokoban = coord
                elif symbol == '.':
                    targets.add(coord)
                elif symbol == '$':
                    boxes.add(coord)
            else:
                if symbol != '#':
                    print "Unknown symbol '%s' will be considered a wall" % symbol

    start = AStarSokNode(sokoban, boxes,   0, -1)
    end   = AStarSokNode(sokoban, targets, 0, -1)

    search_engine = AStarSok(set(map_), targets, sokoban)
    path = search_engine.search(start, end)

    plotPath(path, map_, sokoban, maze)


###########
#         #
#    $$   #
#  .      #
#         #
#@     .  #
###########
    #####
    #   #
    #$  #
  ###  $##
  #  $ $ #
### # ## #   ######
#   # ## #####  ..#
# $  $          ..#
##### ### #@##  ..#
    #     #########
    ####### 