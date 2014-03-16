#!/usr/bin/env python
import svgwrite
import numpy as np
from cmath import exp, pi


def roundComplex(z):
    return z.real + 1j*z.imag


class Turtle():

    def __init__(self, title, start_coord=[100,100]):

        self.draw    = svgwrite.drawing.Drawing()
        self.coord   = start_coord[0] + 1j*start_coord[1]
        self.dir     = 1
        self.pendown = True
        self.title   = title


    def left(self, angle, rad=False): # angle in degrees
        if not rad:
            self.dir = self.dir * exp(-1j * ((angle / 360.) * 2*pi))
        else:
            self.dir = self.dir * exp(-1j * angle)


    def right(self, angle, rad=False): # angle in degrees
        if not rad:
            self.dir = self.dir * exp(1j * ((angle / 360.) * 2*pi))
        else:
            self.dir = self.dir * exp(1j * angle)


    def resetDir(self):
        self.dir = 1

    def penUp(self):
        self.pendown = False

    def penDown(self):
        self.pendown = True

    def forward(self, step, colour='black'):
        new_coord = self.coord + self.dir * step
        if self.pendown:
            self.draw.add( self.draw.line(start  = (self.coord.real, self.coord.imag),\
                                          end    = (new_coord.real, new_coord.imag),  \
                                          stroke = colour ))
        self.coord = new_coord        


    def backwards(self, step, colour='black'):
        new_coord = self.coord - self.dir * step
        if self.pendown:
            self.draw.add( self.draw.line(start  = (self.coord.real, self.coord.imag),\
                                          end    = (new_coord.real, new_coord.imag),   \
                                          stroke = colour ))
        self.coord = new_coord


    def addLine(self, from_, to, colour='black'):
        self.draw.add( self.draw.line(start  = (from_.real, from_.imag),\
                                      end    = (to.real, to.imag),      \
                                      stroke = colour ))

    def addLineNumpy(self, from_, to, colour='black'):
        self.draw.add( self.draw.line(start  = (from_[0], from_[1]),\
                                      end    = (to[0], to[1]),      \
                                      stroke = colour ))

    def addPoint(self, center):
        self.draw.add( self.draw.circle(center=center, r=5, stroke = 'red', fill='red'))

    def text(self, text, fill='black'):
        self.draw.add(self.draw.text(text, (10,300), fill=fill, font_size=20))

    def setCoord(self, x, y):
        self.coord = x + 1j*y

    def setDir(self, dir):
        self.dir = dir

    def backDir(self):
        self.right(180)

    def dumpImage(self):
        self.draw.saveas("img/" + self.title + ".svg")

    def show(self):
        self.draw.show()
