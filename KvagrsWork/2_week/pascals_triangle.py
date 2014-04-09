#######################################
#
# Pascals triangle, modulo
#
#######################################

#from bmplib import bmp
import svgwrite

def pascalsTriangle(n): # 2 < n = number of layers in the triangle

    layers = []
    layers.append([1])      # append the first two layer of pascals triangle
    layers.append([1,1])

    for i in range(2,n):
        tmp_list=[]
        tmp_list.append(1)
        for j in range(i-1):
            tmp_list.append( layers[i-1][j] + layers[i-1][j+1] )
        else:
            tmp_list.append(1)

        layers.append(tmp_list)

    return layers


def differentColors(mod):       

    colors = []
    for x in range(1,mod+1):
        red   = int( (100+255/(x/5.))%255 )
        green = int( (150+255/(x/5.))%255 )
        blue  = int( (70+255/(x/5.))%255 )
        colors.append( (red, green, blue) )

    return colors


def drawPascalsTriangle(n, mod=3, side=100, save=False, filename='', web=False):

    im     = svgwrite.drawing.Drawing()
    layers = pascalsTriangle(n)
    colors = differentColors(mod)

    for y in range(n):
        for x in range( len( layers[ y ] ) ):
            nx = n/2*side - y * side / 2 + x * side - side / 2  # off set
            color = colors[ layers[y][x] % mod ]
            im.add( im.rect(    insert = (nx, y*side) ,\
                                size   = (side, side),\
                                fill   = 'rgb' + str( color ),\
                                stroke = 'black'))
    if save:
        im.saveas( filename + '.png')
    
    return




if __name__ == '__main__':

    drawPascalsTriangle(50, mod=2, save=True, filename='pascals_triangle')