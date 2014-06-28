# -*- coding: utf-8 -*-

import svgfig as svg
from math import sin, cos, pi
import copy


class Turtle(object):

    def __init__(self, center=(0, 0)):
        self.x, self.y = center
        self.angle = 0.
        self.pen = True
        self.lines = []
        self.queue = []

    def forward(self, step):
        new_x = self.x + cos(self.angle) * step
        new_y = self.y + sin(self.angle) * step
        self._draw_line(self.x, self.y, new_x, new_y)

        self.x = new_x
        self.y = new_y

        return self

    def back(self, step):
        return self.forward(-step)

    def right(self, step):
        self.angle += float(step)
        return self

    def left(self, step):
        self.angle -= float(step)
        return self

    def penup(self):
        self.pen = False
        return self

    def pendown(self):
        self.pen = True
        return self

    def rotate(self, angle):
        """ Rotace kolem pocatku po smeru hodinovych rucicek. Bez vykresleni. """
        self.x, self.y = self.x*cos(angle)+self.y*sin(angle),\
                         -self.x*sin(angle)+self.y*cos(angle)
        self.angle += angle
        return self

    def push(self):
        """ Uloz si pozici zelvy na zasobnik. """
        self.queue.append({'x': self.x,
                           'y': self.y,
                           'angle': self.angle,
                           'pen': self.pen})
        return self

    def pop(self):
        d = self.queue.pop()
        self.x, self.y = d['x'], d['y']
        self.angle = d['angle']
        self.pen = d['pen']
        return self

    def copy(self):
        """ Zkopiruje zelvu, pole s objekty necha jako ukazatel na puvodni. """
        return copy.copy(self)

    def circle(self, r):
        """ Nakresli kruznici kolem zlevy s polomerem r."""
        self.lines.append(svg.Ellipse(
            self.x, self.y, r, 0, r, stroke_width=0.2))
        return self

    def _draw_line(self, x, y, new_x, new_y):
        if self.pen:
            self.lines.append(svg.Line(x, y, new_x, new_y, stroke_width=0.2))

    def show(self, **kwargs):
        """ kwargs:
            width=400, height=400, viewBox="0 0 2000 2000"
        """
        s = svg.Fig(*self.lines).SVG()

        c = svg.canvas(s, **kwargs)
        c.inkview()
        return self

    def xml(self):
        s = svg.Fig(*self.lines).SVG()
        return s.xml()

    def save(self, name, **kwargs):
        s = svg.Fig(*self.lines).SVG()
        c = svg.canvas(s, **kwargs)
        c.save(name)
        return self

    def add(self, obj):
        """ Prida libovolny objekt do svg. """
        self.lines.append(obj)

    def star(self, n, r):
        """ Z aktualni pozice vykresli n-cipou hvezdu. Nefunguje pro sude n.
        uhel pi/n
        """
        assert n % 2 == 1, 'Nefunguje pro sude.'

        for i in range(n):
            self.forward(r)
            self.right(pi - pi/float(n))
        return self

    def polygon(self, n, r):
        """ uhel pi - 2pi/n"""
        for i in range(n):
            self.forward(r)
            self.right(2*pi/n)
        return self




if __name__ == '__main__':
    turtle = Turtle(center=(50,50))

    #turtle.star(9, 40).show()
    #turtle.polygon(11, 10).show()

    turtle.push().forward(10).pop().right(pi/2).forward(10).show()




