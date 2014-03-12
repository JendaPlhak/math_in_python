#!/usr/bin/env python
import pygal

def calculate_collatzo_convergence(n):

    steps = 0
    max_n = 0
    while n != 1:

        steps += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1

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


if __name__ == "__main__":

    Collatzo_plot           = BitmapPlot("img/Collatzo_serie.svg", "Collatzo_serie")
    Collatzo_serie_max_plot = BitmapPlot("img/Collatzo_serie_max.svg", "Collatzo_serie_max")

    for i in xrange(3000):
        pair = calculate_collatzo_convergence(i + 1)
        Collatzo_plot.new_point([i, pair[0]])
        Collatzo_serie_max_plot.new_point([i, pair[1]])

    Collatzo_plot.save()
    Collatzo_serie_max_plot.save()
