#!/usr/bin/env python

import svgwrite
import colorsys

def pascals_triangle(n):
# 2 < n = number of layers in the triangle
    
    # append the first two layer of pascals triangle
    layers = [[1], [1, 1]]

    # adding further layers
    for i in range(2,n):
        tmp_list=[]
        tmp_list.append(1)
        for j in range(i-1):
            tmp_list.append( layers[i-1][j] + layers[i-1][j+1] )
        else:
            tmp_list.append(1)

        layers.append(tmp_list)

    return layers


def different_colors(N):       
# see http://stackoverflow.com/questions/876853/generating-color-ranges-in-python

    HSV_tuples = [(x * 1.0 /  N, 1, 0.85) for x in range(N) ]
    RGB_tuples = map(lambda x: colorsys.hsv_to_rgb( *x ), HSV_tuples)
    RGB_tuples = map(lambda x: tuple(map(lambda y: int(y * 255),x)),RGB_tuples)

    return RGB_tuples


def draw_pascals_triangle(n, mod=3, side=100, filename='', web=False):

    # initialize drawing canvas, create layers and colors
    im     = svgwrite.drawing.Drawing()
    layers = pascals_triangle( n )
    colors = different_colors(mod)

    for y in range(n):
        for x in range( len( layers[ y ] ) ):
            # off set
            nx = n/2*side - y * side / 2 + x * side - side / 2
            color = colors[ (layers[y][x] + 2) % mod ]
            im.add( im.rect(insert = (nx, y * side) ,\
                            size   = (side, side),\
                            fill   = 'rgb' + str(color),\
                            stroke = 'black'))
    if filename:
        im.saveas( filename + '.png')
    
    return


if __name__ == '__main__':

    draw_pascals_triangle(50, mod=20, filename='pascals_triangle')