#!/usr/bin/env python
from Turtle import Turtle
from cmath  import exp, pi
from math   import hypot, atan, sin, cos

from complex_frac import complexFractal

import numpy             as np
import matplotlib.pyplot as plt


def tree(draw, rec, a):

    if rec == 0:
        return

    draw.forward(a)
    root = draw.coord
    dir  = draw.dir

    draw.left(45)
    tree(draw, rec - 1, a/2)

    draw.setDir(dir)
    draw.setCoord(root.real, root.imag)

    draw.right(45)
    tree(draw, rec - 1, a/2)


def sierpinskiTriangle(draw, rec, a, first=True):

    V0 = draw.coord
    V1 = draw.coord + draw.dir * a
    V2 = draw.coord + exp(1j * pi / 3.) * draw.dir * a

    if first:
        draw.addLine(V0, V1)                        # Draw outer triangle
        draw.addLine(V0, V2)
        draw.addLine(V1, V2)

    S0 = (V0 + V1) / 2
    S1 = (V0 + V2) / 2
    S2 = (V1 + V2) / 2
    draw.addLine(S0, S1)  # Draw inner triangle
    draw.addLine(S0, S2)
    draw.addLine(S1, S2)


    if rec > 1:
        draw.coord = S0
        sierpinskiTriangle(draw, rec - 1, a/2, False)

        draw.coord = S1
        sierpinskiTriangle(draw, rec - 1, a/2, False)

        draw.coord = V0
        sierpinskiTriangle(draw, rec - 1, a/2, False)


def processGramar(rec, instructions, rules, non_terminals):

    for _ in xrange(rec):
        instructions = ''.join(rules[s] for s in instructions)

    for non_terminal in non_terminals:
        instructions = instructions.replace(non_terminal, "")

    return instructions


def drawGramar(draw, instructions, step, angle1, angle2):

    for action in instructions:
        if action == "-":
            draw.right(angle1)
        elif action == "+":
            draw.left(angle2)
        elif action == "F":
            draw.forward(step)
        elif action == "B":
            draw.backDir()
        else:
            draw.backwards(step)



def kochFlake(draw, rec, side):  # Implementation using instructions

    instructions = "F-F-F"    # Originally was invented only Koch curve, we need 3 of them to form the flake
    rules        = {'F':'F+F-F+F', '+':'+', '-':'-',} # every straight line replace with 2-sides of triangle ___ > _/\_
    instructions = processGramar(rec, instructions, rules, [])

    drawGramar(draw, instructions, side / 3 ** (rec - 1), 120, 60)



def hilbertCurve(draw, rec, side):

    instructions = "A"   # Representation as Lindenmayer system. See http://en.wikipedia.org/wiki/Hilbert_curve#Representation_as_Lindenmayer_system
    rules        = {'A':'-BF+AFA+FB-','B':'+AF-BFB-FA+', '+':'+', '-':'-', 'F':'F'}
    instructions = processGramar(rec, instructions, rules, ('A', 'B'))

    drawGramar(draw, instructions, side / float(2**rec - 1), 90, 90)


def krishnaAnklet(draw, rec, side):

    instructions = "-A--A"
    rules        = {'A':'AFA--AFA', '-':'-', 'F':'F'}
    instructions = processGramar(rec, instructions, rules, ['A'])

    drawGramar(draw, instructions, side / float(2**rec - 1), 45, None)


def pentagonSnowflake(draw, rec, side):

    instructions = "FA+FA+FA+FA+FA"
    rules        = {'A':'-F+F+FC+F+F', 'C':'-F-F-FBDB-F-F', 'D':'FA+FA+FA+FA+FA+', 'E':'+F-F-FC-F-F', '+':'+', '-':'-', 'F':'F', 'B':'B'}
    instructions = processGramar(rec, instructions, rules, ['A', 'C', 'D', 'E'])

    drawGramar(draw, instructions, side, 72, 72)


def pentagonSnowflakeMirror(draw, rec, side): # Draw the pentagon snowflake using reflections

    inner    = True
    edges    = []
    vertices = []
    # Initialize pentagon
    draw.penUp()
    for _ in xrange(5):
        start = draw.coord
        draw.forward(side)
        draw.right(72)
        edges.append((start, draw.coord))
        vertices.append(start)

    for r in xrange(rec):
        edges_tmp = []
        vertices_tmp = []
        for i in xrange(5):
            edge_tmp, new_vortex = addSymetry(edges, vertices, i)
            edges_tmp.extend(edge_tmp)
            vertices_tmp.append(new_vortex)
        vertices = vertices_tmp

        if inner:
            edges.extend(edges_tmp)
        else:
            edges = edges_tmp

    for edge in edges:
        draw.addLine(edge[0], edge[1])


def addSymetry(edges, vertices, i):

    vortex = vertices[(i + 3)% 5]
    edge   = (vertices[i], vertices[(i+1) % 5])

    dir_vector = edge[1] - edge[0]
    norm       = dir_vector.imag - 1j * dir_vector.real   # Calculate shift vector to shift our linear space to origin
    norm      /= hypot(norm.real, norm.imag)
    norm      *= -norm.real * edge[0].real -norm.imag * edge[0].imag


    if dir_vector.real == 0:
        angle = pi/2
    else:
        angle = atan(dir_vector.imag / dir_vector.real)

    sin_ = sin(2*angle)
    cos_ = cos(2*angle)

    new_edges = []
    for e in edges:
        e_tmp = []
        for V in e:
            V_tmp = V
            V = V + norm     # Linear transformation - shift, rotation, back-shift
            V = (cos_*V.real + sin_*V.imag) + \
                1j*(sin_*V.real - cos_*V.imag)
            V = V - norm

            if V_tmp == vortex:
                vortex_new = V
            e_tmp.append(V)

        new_edges.append(e_tmp)
    return new_edges, vortex_new





if __name__ == "__main__":


    draw = Turtle("Tree", [5, 80])
    tree(draw, 10, 100.)
    draw.dumpImage()

    draw = Turtle("Koch_Flake", [15, 80])
    kochFlake(draw, 5, 100)
    draw.dumpImage()

    draw = Turtle("Sierpinski_Triangle")
    sierpinskiTriangle(draw, 7, 500)
    draw.dumpImage()

    draw = Turtle("Hilbert_Curve",[5, 5])
    hilbertCurve(draw, 7, 300)
    draw.dumpImage()

    draw = Turtle("Krishna_Anklet", [150, 5])
    krishnaAnklet(draw, 5, 200)
    draw.dumpImage()

    draw = Turtle("Pentagon_snow_flake", [260, 250])
    pentagonSnowflakeMirror(draw, 4 , 7)
    draw.dumpImage()


    # complexFractal(julia_=True,  path="img/Julia_Set.png")
    # complexFractal(julia_=False, path="img/Mandelbrot_set.png")


    