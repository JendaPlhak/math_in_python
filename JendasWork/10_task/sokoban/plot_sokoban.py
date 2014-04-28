from AStar import AStar, AStarNode
import sys
import svgwrite

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


def plotStateText(boxes, sokoban, maze):

    for symbol, coord in maze:
        if coord in boxes:
            sys.stdout.write("$")
        elif coord == sokoban:
            sys.stdout.write("@")
        elif symbol in ['@', '$']:
            sys.stdout.write(' ')
        else:
            sys.stdout.write(symbol)
    print "\n---------------------------"


class PlotStateSvg():

    def __init__(self, path):
        self.index = 1
        self.path  = path

    def plotState(self, boxes, sokoban, maze):
        draw = svgwrite.drawing.Drawing()
        size = 30

        square = [(0, 0), (0, size), (size, size), (size, 0)]
        for symbol, coord in maze:
            x, y = coord.real * size, coord.imag * size
            if coord in boxes:
                clr = 'green' if symbol == '.' else 'brown'
                draw.add( draw.polygon([(x+a, y+b) for a, b in square], 
                                       stroke =clr, 
                                       fill   =clr))
            elif coord == sokoban:
                draw.add( draw.circle(center = [x + size/2, y + size/2], 
                                      r      = size/2, 
                                      stroke = 'red', 
                                      fill   = 'red'))
            elif symbol == ".":
                for points in [((x + size/2, y), (x + size/2, y + size)),
                               ((x, y + size/2), (x + size,   y + size/2))]:
                    draw.add( draw.line(start  = points[0], 
                                        end    = points[1],
                                        stroke = 'green', 
                                        fill   = 'green'))
            elif symbol == "#":
                draw.add( draw.polygon([(x+a, y+b) for a, b in square], 
                                       stroke ='gray', 
                                       fill   ='gray'))
        draw.saveas(self.path + \
                    "{0:010d}".format(self.index) + \
                    ".svg")
        self.index += 1


def plotPath(path, map_, sokoban, maze):

    search = AStarMap(set(map_))
    start  = path[0]
    plot   = PlotStateSvg("sokoban/sokoban")

    for state in path[1:]:
        sokoban_end = (start.boxes - state.boxes).pop() 
        start_node  = AStarMapNode(0, sokoban)
        end_node    = AStarMapNode(0, sokoban_end - state.dir)

        search.map  = set(map_) - start.boxes

        sokoban_path = [s.coord for s in search.search(start_node, end_node)]
        for coord in sokoban_path:
            plot.plotState(start.boxes, coord, maze)
        plot.plotState(state.boxes, sokoban_end, maze)

        sokoban = sokoban_end
        start   = state


        


