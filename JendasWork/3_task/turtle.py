#!/usr/bin/env python

import svgwrite
import numpy as np
from cmath import exp, pi

def roundComplex(z):
    return z.real + 1j*z.imag

class Turtle():

    def __init__(self, start_coord=[0,0]):

        self.draw    = svgwrite.drawing.Drawing()
        self.coord   = start_coord[0] + 1j*start_coord[1]
        self.dir     = 1
        self.pendown = False


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
        dir = self.dir
        self.left(145)
        new_coord = self.coord + self.dir * 5
        self.draw.add( self.draw.line(start  = (self.coord.real, self.coord.imag),\
                                      end    = (new_coord.real, new_coord.imag),  \
                                      stroke = colour ))
        self.dir = dir
        self.right(145)
        new_coord = self.coord + self.dir * 5
        self.draw.add( self.draw.line(start  = (self.coord.real, self.coord.imag),\
                                      end    = (new_coord.real, new_coord.imag),  \
                                      stroke = colour ))
        self.dir = dir
        


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


    def setCoord(self, x, y):
        self.coord = x + 1j*y

    def setDir(self, dir):
        self.dir = dir

    def backDir(self):
        self.right(180)


    def dumpImage(self, path="trol.svg"):
        self.draw.saveas(path)
