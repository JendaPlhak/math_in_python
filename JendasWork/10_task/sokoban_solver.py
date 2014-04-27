#!/usr/bin/env python
from AStar import AStar, AStarNode
import sys


class AStarLTNode(AStarNode): # AStart no Left Turn Node

    def __init__(self, sokoban, boxes, empty_move, map_):

        self.boxes       = boxes
        self.sokoban     = self.sokobanLeftMost(sokoban, map_)
        self.empty_move  = empty_move
        self.hash        = hash((self.sokoban, tuple(self.boxes)))
        AStarNode.__init__(self)

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def move_cost(self, target):
        return 1

    def sokobanLeftMost(self, sokoban, map_):
        """
        Apply BSD to find left-most top corner to place sokoban
        and also find all possible box shifts
        """
        unseen         = set([sokoban])
        seen           = set()
        possible_shift = set()
        LTM            = sokoban #LeftTopMost
        while unseen:
            coord = unseen.pop()
            seen.add(coord)
            for dir_ in (1, 1j, -1, -1j):
                new_coord = coord + dir_
                if new_coord in map_:
                    if new_coord in self.boxes:
                        if new_coord + dir_ in map_ and new_coord + dir_ not in self.boxes:
                            possible_shift.add((new_coord, new_coord + dir_))
                    elif new_coord.real < LTM.real or (new_coord.real == LTM.real and new_coord.imag < LTM.imag):
                        LTM = new_coord
                        if not new_coord in seen:
                            unseen.add(new_coord)
                    else:
                        if not new_coord in seen:
                            unseen.add(new_coord)

        return LTM




class AStarLT(AStar): # AStart no Left Turn class

    def __init__(self, map_, targets):
        self.map       = map_
        self.targets   = targets
        self.dirs      = (1, 1j, -1, -1j)
        self.deadLocks = set()
        print "Preprocessing..."
        self.loadDeadLocks()
        print "     Done!"


    def loadDeadLocks(self):
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


    def digTunels(self):

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


    def heuristic(self, node):
        dist = 0
        for box in node.boxes:
            dist_list = []
            for target in self.targets:
                diff = box - target
                dist_list.append(abs(diff.real) + abs(diff.imag))
            dist += min(dist_list)
        return dist


    def neighbours(self, node):

        neigh = []
        for dir_ in self.dirs:
            if dir_ == -node.empty_move:  # No point going back if we moved without box in previous step
                continue
            coord = node.sokoban + dir_
            if coord in self.map:
                if coord in node.boxes:
                    box_coord = coord + dir_
                    if box_coord not in node.boxes and box_coord in self.map and box_coord not in self.deadLocks:
                        new_boxes = set(node.boxes)
                        new_boxes.remove(coord)
                        new_boxes.add(box_coord)
                        neigh.append(AStarLTNode(coord, new_boxes, 0, self.map))
                else:
                    neigh.append(AStarLTNode(coord, node.boxes, dir_, self.map))
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

    start = AStarLTNode(sokoban, boxes,   0, map_)
    end   = AStarLTNode(sokoban, targets, 0, map_)

    search_engine = AStarLT(map_, targets)
    path = search_engine.search(start, end)

    for state in path:
        with open("sokoban.txt", 'r') as f:
            for row, line in enumerate(f):
                for col, symbol in enumerate(line):
                    if col + 1j*row in state.boxes:
                        sys.stdout.write("$")
                    # elif col + 1j*row in search_engine.deadLocks:
                    #     sys.stdout.write("X")
                    elif col + 1j*row == state.sokoban:
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