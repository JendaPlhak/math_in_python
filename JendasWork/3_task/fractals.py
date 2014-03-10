from turtle import Turtle
from cmath  import exp, pi


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



def hilberCurve(draw, rec, side):

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




draw = Turtle()
draw.setCoord(150, 150)
draw.penDown()

# tree(draw, 10, 100.)

# draw.setCoord(400, 50)
# kochFlake(draw, 5, 100)
# draw.resetDir()

# draw.setCoord(750, 350)
# sierpinskiTriangle(draw, 7, 500)


# draw.setCoord(500, 50)
# hilberCurve(draw, 7, 300)

# draw.setCoord(500, 50)
# krishnaAnklet(draw, 6, 300)

pentagonSnowflake(draw, 6, 25)

draw.dumpImage()