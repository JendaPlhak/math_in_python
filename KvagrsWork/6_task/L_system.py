#!/usr/bin/python

import sys
sys.path.append('../3_task')

from lib_turtle import *


def generate_Lsystem(axiom, rule, n):
# generates a string from the axiom
# by given rules and iteration

    for i in xrange(n):
        axiom = "".join([rule[x] if x in rule else x for x in axiom])

    return axiom


def interpret_Lsytem(path, forward=7, angle=60, filename=''):
# goes through the path and draws 

    turtle = Turtle()
    turtle.left(90)
    states = []
    instr  = { 'A' : ['forward', forward],
               'F' : ['forward', forward],
               'B' : ['forward', forward],
               'x' : ['forward', 0],
               'y' : ['forward', 0],
               '-' : ['left', angle],
               '+' : ['right', angle]}

    for step in path:
        if step == '[':
            states.append([turtle.x, turtle.y, turtle.phi])
        elif step == ']':
            state = states.pop()
            turtle.set_pos( state[:2] )
            turtle.set_dir( state[2] )
        else:
            getattr(turtle, instr[step][0])( instr[step][1])

    if filename:
        turtle.draw_object( 'L_system_'+ filename )

    return


if __name__ == '__main__':

    
    path  = generate_Lsystem('F--F--F', {'F':'F+F--F+F'}, 4)
    interpret_Lsytem(path, forward=3, angle=60, filename='koch_original')

    path  = generate_Lsystem('F--F--F', {'F':'F+F--F+F'}, 4)
    interpret_Lsytem(path, forward=3, angle=61, filename='koch_change')

    path  = generate_Lsystem('A', {'A':'B-A-B', 'B':'A+B+A'}, 8)
    interpret_Lsytem(path, forward=1, angle=60, filename='sierpinski_original')

    path  = generate_Lsystem('A', {'A':'B-A-B', 'B':'A+B+A'}, 8)
    interpret_Lsytem(path, forward=1, angle=59, filename='sierpinski_change')

    path = generate_Lsystem('x', {'x':'-yF+xFx+Fy-',
                                  'y':'+xF-yFy-Fx+'}, 5)
    interpret_Lsytem(path, angle=90, filename='hilbert_original')

    path = generate_Lsystem('x', {'x':'-yF+xFx+Fy-',
                                  'y':'+xF-yFy-Fx+'}, 5)
    interpret_Lsytem(path, angle=91, filename='hilbert_change')

    path = generate_Lsystem( 'A', {'A': 'F[+A]-A',
                                   'F': 'FF'}, 7)
    interpret_Lsytem( path, forward=2, angle=45, filename='basic_tree_original')

    path = generate_Lsystem( 'A', {'A': 'F[+A]-A',
                                   'F': 'FF'}, 7)
    interpret_Lsytem( path, forward=2, angle=47, filename='basic_tree_change')

    path = generate_Lsystem('A', {'A':'F-[[A]+A]+F[+FA]-A',
                                  'F':'FF'}, 5)
    interpret_Lsytem( path, angle=26, filename='tree_original')

    path = generate_Lsystem('A', {'A':'F-[[A]+A]+F[+FA]-A',
                                  'F':'FF'}, 5)
    interpret_Lsytem( path, angle=28, filename='tree_change')

    
    path = generate_Lsystem('A', {'A':'-A++B',
                                  'B':'A--B+'}, 10)
    interpret_Lsytem( path, angle=45, filename='dragon_original')
    
    path = generate_Lsystem('A', {'A':'-A++B',
                                  'B':'A--B+'}, 10)
    interpret_Lsytem( path, angle=43, filename='dragon_change')

    path = generate_Lsystem('F', {'F':'F[+F]F[-F]F'}, 4)
    interpret_Lsytem(path, angle=25.7, filename='weed_original')

    path = generate_Lsystem('F',{'F':'FF+[+F-F-F]-[-F+F+F]'},4)
    interpret_Lsytem(path, angle=25, filename='simple_bush_original')

    path = generate_Lsystem('F', {'F':'F[+F]F[-F]F'}, 4)
    interpret_Lsytem(path, angle=26.7, filename='weed_change')

    path = generate_Lsystem('F',{'F':'FF+[+F-F-F]-[-F+F+F]'},4)
    interpret_Lsytem(path, angle=26, filename='simple_bush_change')