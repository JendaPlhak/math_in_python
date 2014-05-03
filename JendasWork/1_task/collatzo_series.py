#!/usr/bin/env python
import pygal
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def calculate_collatzo_convergence(n):

    steps = 0
    max_n = 0

    while n != 1:
        steps += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        max_n = max(max_n, n)

    return steps, max_n


class BitmapPlot():

    def __init__(self, path, title):
        self.im       = pygal.XY(stroke=False, x_label_rotation=30)
        self.path     = path
        self.im.title = title
        self.points   = []

    def new_point(self, coord):
        self.points.append(coord)

    def flush(self):
        self.im.add('Num. iterations', self.points)

    def save(self):
        self.flush()
        open(self.path, 'w').write(self.im.render())


def plotForPath(path, data):

    fig = plt.figure(figsize=(23.5, 23.5))
    plt.plot(data[0], data[1],  'ko')
    fig.savefig(path, dpi=80, bbox_inches='tight')

if __name__ == "__main__":
    

    collatzo_normal = []
    collatzo_max    = []
    for i in xrange(8000):
        pair = calculate_collatzo_convergence(i + 1)
        collatzo_normal.append([i, pair[0]])
        collatzo_max.append([i, pair[1]])

    plotForPath("img/Collatzo_serie_8000.jpg", zip(*collatzo_normal))
    plotForPath("img/Collatzo_serie_25.jpg",   zip(*collatzo_normal[:25]))
    plotForPath("img/Collatzo_serie_max.jpg",  zip(*collatzo_max[:3000]))
