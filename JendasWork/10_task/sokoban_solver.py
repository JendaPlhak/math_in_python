#!/usr/bin/env python
from AStar import AStar, AStarNode
import sys


class AStarLTNode(AStarNode): # AStart no Left Turn Node

    def __init__(self, sokoban, boxes):

        self.boxes       = boxes
        self.sokoban     = sokoban
        self.hash        = hash((self.sokoban, tuple(self.boxes)))
        AStarNode.__init__(self)

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def move_cost(self, target):
        return 1

    def sokobanLeftMost(self, map_):
        """
        Apply BSD to find left-most top corner to place sokoban
        and also find all possible box shifts
        """
        unseen   = set([self.sokoban])
        seen     = set()
        posShift = set()
        LTM      = self.sokoban #LeftTopMost
        while unseen:
            coord = unseen.pop()
            seen.add(coord)
            for dir_ in (1, 1j, -1, -1j):
                new_coord = coord + dir_
                if new_coord in map_:

                    if new_coord in self.boxes:
                        if new_coord + dir_ in map_ and new_coord + dir_ not in self.boxes:
                            posShift.add((new_coord, new_coord + dir_))

                    elif new_coord.real < LTM.real or (new_coord.real == LTM.real and new_coord.imag < LTM.imag):
                        LTM = new_coord
                        if not new_coord in seen:
                            unseen.add(new_coord)
                    else:
                        if not new_coord in seen:
                            unseen.add(new_coord)

        self.posShift = posShift
        self.sokoban  = LTM




class AStarLT(AStar): # AStart no Left Turn class

    def __init__(self, map_, targets):
        self.map       = map_
        self.targets   = targets
        self.dirs      = (1, 1j, -1, -1j)
        self.deadLocks = set()
        print "Preprocessing..."
        self.loadDeadLocks()
        self.digTunnels()
        print "     Done!"


    def loadDeadLocks(self):
        """
        Locate all simple dead-locks. That
        means all corners and coordinates between corners
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
                        continue
                    else:
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
                    if not (coord + dir_ * 1j not in self.map or coord - dir_ * 1j not in self.map):
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


    def heuristic(self, node):
        """
        Estimated distance between current and final
        position
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
        node.sokobanLeftMost(self.map)
        for PS in node.posShift:
            if PS[1] in self.deadLocks: 
                continue
            new_boxes = set(node.boxes)
            new_boxes.remove(PS[0])
            if PS[1] in self.tunnels:
                new_boxes.add(self.tunnels[PS[1]])
            else:
                new_boxes.add(PS[1])
            neigh.append(AStarLTNode(PS[0], new_boxes))
        return neigh



if __name__ == '__main__':
    
    map_ = set()
    with open("sokoban.txt", 'r') as f:
        targets = set()
        boxes   = set()
        for row, line in enumerate(f):
            for col, symbol in enumerate(line):
                coord = col + 1j*row

                if symbol == ' ':
                    map_.add(coord)
                elif symbol == '@':
                    map_.add(coord)
                    sokoban = coord
                elif symbol == '.':
                    map_.add(coord)
                    targets.add(coord)
                elif symbol == '$':
                    map_.add(coord)
                    boxes.add(coord)
                else:
                    if symbol != '#' and symbol != '\n':
                        print "Unknown symbol '%s' will be considered a wall" % symbol

    start = AStarLTNode(sokoban, boxes)
    end   = AStarLTNode(sokoban, targets)

    search_engine = AStarLT(map_, targets)
    path = search_engine.search(start, end)

    for state in path:
        with open("sokoban.txt", 'r') as f:
            for row, line in enumerate(f):
                for col, symbol in enumerate(line):
                    coord = col + 1j*row
                    if coord in state.boxes:
                        sys.stdout.write("$")
                    # elif coord in search_engine.deadLocks:
                    #     sys.stdout.write("X")
                    # elif coord in search_engine.tunnels:
                    #     sys.stdout.write("O")
                    elif coord == state.sokoban:
                        sys.stdout.write("@")
                    elif symbol in ['@', '$']:
                        sys.stdout.write(' ')
                    else:
                        sys.stdout.write(symbol)
        print "\n---------------------------"

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