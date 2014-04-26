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

        while open_set:

            x = min(open_set, key=lambda x: x.f)
            if x.coord == end.coord:
                return self.reconstructPath(start, x, close_set)

            open_set.remove(x)
            close_set.add(x)

            for node in self.neighbours(x):
                if node in close_set: 
                    continue

                new_g = x.g + x.move_cost(node)

                if node not in open_set:
                    open_set.add(node)
                elif not new_g < node.g:
                    continue

                node.g      = new_g
                node.h      = self.heuristic(node)
                node.f      = node.g + node.h
                node.parent = x

        return None
                

    def reconstructPath(self, start, end, close_set):

        node = end
        path = [end.coord]

        while node != start and node != None:
            node = node.parent
            path.append(node.coord)

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














