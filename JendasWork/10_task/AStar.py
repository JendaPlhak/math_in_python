

def insort(a, x, lo=0, hi=None, key=lambda x:x):
    """Insert item x in list a, and keep it reverse-sorted assuming a
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
        raise NotImplementedError

    def neighbours(self, node):
        raise NotImplementedError

    def search(self, start, end):

        start.h   = self.heuristic(start)
        start.f   = start.h
        close_set = set()
        open_set  = set([start])
        open_list = [start]

        while open_set:
            x = open_list.pop()

            final = True
            for box in end.boxes:
                if box not in x.boxes:
                    final = False
                    break
            if final:
                return self.reconstructPath(start, x, close_set)

            open_set.remove(x)
            close_set.add(x)

            for node in self.neighbours(x):
                if node in close_set: 
                    continue

                new_g = x.g + x.move_cost(node)

                add = False
                if node not in open_set:
                    add = True
                elif not new_g < node.g:
                    continue

                node.g      = new_g
                node.h      = self.heuristic(node)
                node.f      = node.g + node.h
                node.parent = x
                if add:
                    open_set.add(node)
                    insort(open_list, node, key=lambda x: x.f)

        raise Exception("No Path found!")
                

    def reconstructPath(self, start, end, close_set):

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














