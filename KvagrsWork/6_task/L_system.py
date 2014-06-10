#!/usr/bin/python

import sys
sys.path.append('../3_task')

import re
import turtle_lib

def generate_Lsystem(axiom, rule, n):
    # symbols {F, -, +}
    # axiom    F--F--F
    # rule     F -> F+F--F+F
    # n        number of ap

    for i in xrange(n):
        axiom = "".join([rule[x] if x in rule else x for x in axiom])

    return axiom


def interpret_Lsytem(path, instr):

    turtle = Turtle()

    for step in path:
        turtle.instr[step][0](instr[step][1])

    turtle.draw_object('koch_L_system')
    return


if __name__ == '__main__':

    path         = generate_Lsystem('F--F--F', {'F':'F+F--F+F'}, 4)
    instr = { 'F' : [forward, 10],
                     '-' : [left, 60],
                     '+' : [right, 60]}
    interpret_Lsytem(path, instr)