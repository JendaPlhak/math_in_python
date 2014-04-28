def insort(a, x, key=lambda x:x):
    """
    Insert item x in list a, and keep it reverse-sorted assuming a
    is reverse-sorted.
    If x is already in a, insert it to the right of the rightmost x.
    """
    lo = 0
    hi = len(a)

    val = key(x)
    while lo < hi:
        mid = (lo+hi)//2
        if val > key(a[mid]): hi = mid
        else: lo = mid+1
    a.insert(lo, x)


class AStar(object):

    def heuristic(self, node):
        """
        Estimated distance between node and target
        position.
        """
        raise NotImplementedError

    def neighbours(self, node):
        """
        Return iterable containing possible moves
        from given node.
        """
        raise NotImplementedError

    def endReached(self, node, end):
        """
        Test for target destination.
        """
        raise NotImplementedError

    def search(self, start, end):
        """
        Perform A* search. If path is not found,
        exception is raised, otherwise path is returned. 
        """
        self.end  = end
        start.h   = self.heuristic(start)
        start.f   = start.h
        close_set = set()
        open_set  = set([start])
        open_list = [start]

        while open_set:
            x = open_list.pop()

            if self.endReached(x, end):
                return self.reconstructPath(start, x, close_set)

            open_set.remove(x)
            close_set.add(x)

            for node in self.neighbours(x):
                if node in close_set: 
                    continue

                new_g = x.g + x.move_cost(node)
                add   = False

                if node in open_set:
                    if new_g < node.g: continue
                else:
                    add = True

                node.g      = new_g
                node.h      = self.heuristic(node)
                node.f      = node.g + node.h
                node.parent = x
                if add:
                    open_set.add(node)
                    insort(open_list, node, key=lambda x: x.f)

        raise Exception("No Path found!")
                

    def reconstructPath(self, start, end, close_set):
        """
        Perform back-tracking and reconstruct
        path.
        """
        node = end
        path = [end]

        while node != start and node != None:
            node = node.parent
            path.append(node)

        path.reverse()
        return path



class AStarNode(object):

    def __init__(self):
        self.g = 0
        self.h = 0
        self.f = 0
        self.parent = None

    def move_cost(self, target):
        raise NotImplementedError

    def __hash__(self):
        raise NotImplementedError

    def __eq__(self, other):
        raise NotImplementedError






class AStarMapNode(AStarNode):

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


class AStarMap(AStar): 

    def __init__(self, map_):
        self.map = map_

    def heuristic(self, node):
        diff = node.coord - self.end.coord
        return abs(diff.real) + abs(diff.imag)

    def endReached(self, node, end):
        return node.coord == end.coord

    def neighbours(self, node):
        neigh = []
        for dir_ in (1, -1, 1j, -1j):
            coord   = node.coord + dir_
            if coord in self.map:
                neigh.append(AStarMapNode(dir_, coord))
        return neigh













