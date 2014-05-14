#!/usr/bin/env python
from Turtle import Turtle
from math import sin, pi


def regularPolygon(draw, a=50, n=5): # a = side in pixels, n = number of angles  

    vertices = [draw.coord]
    draw.penDown()

    for i in xrange(n):
        draw.forward(a)
        draw.right(360./n)
        vertices.append(draw.coord)

    draw.right(360./n)
    draw.penUp()
    return tuple(vertices)


def star(draw, a=50, n=5): # a = side in pixels, n = number of angles  

    draw.penDown()
    angle = 180 - 360./(2 * n)

    for i in xrange(n):
        draw.forward(a)
        draw.right(angle)
    draw.penUp()


if __name__ == "__main__":

    draw = Turtle("test_pictures")

    draw.penUp()
    draw.setCoord(-50, -50)
    draw.forward(100)
    draw.right(90)
    draw.forward(50)
    draw.left(90)

    regularPolygon(draw, 100, 5)
    draw.resetDir()
    draw.right(36)
    star(draw, 100 * (sin(108/360. * 2*pi)/sin(36/360. * 2*pi)), 5)

    draw.resetDir()
    draw.forward(300)
    verticies = regularPolygon(draw, 100, 5)

    for i, vortex in enumerate(verticies[:3]):
        draw.addLine(vortex, verticies[(i + 2) % len(verticies)])
        draw.addLine(vortex, verticies[(i + 3) % len(verticies)])

    draw.setCoord(235, 50)
    star(draw, 150, 13)
    draw.dumpImage()