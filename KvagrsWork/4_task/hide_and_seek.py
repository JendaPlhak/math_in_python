#!/usr/bin/env python

from PIL       import Image
from itertools import product

import urllib, cStringIO
import re

PATH = 'http://www.fi.muni.cz/~xpelanek/IV122/zadani/'

def download_file(path): 

    print "Attempting to download file from:"
    print "URL: {}".format( path )

    _file    = cStringIO.StringIO(urllib.urlopen( path ).read())
    if _file:
        print "... successfully read to buffer"
    else:
        print "ERROR while trying to read from:"
        print "URL: {}".format( path )

        return 

    filename  = path[::-1].split('/')[0][::-1]

    with open(filename, 'w') as f:
        f.write( _file.getvalue() )
        print "+++ {}".format( filename )

    _file.close()

    return



def seek_one():
    
    #download( PATH +'skryvacka1.png')
    _file = cStringIO.StringIO(urllib.urlopen( PATH + 'skryvacka1.png').read())
    im    = Image.open('')
    im.save('img/hide_one.png')

    pix = im.load()
    for x, y in product(xrange(im.size[0]), xrange(im.size[1])):
            pix[x,y] = (0, 0, pix[x,y][2] * 255)
            
    im.save('img/solved_one.png')
    _file.close()

    return
    

def seek_two():

    _file = cStringIO.StringIO(urllib.urlopen( PATH + 'skryvacka2.png').read())
    im    = Image.open(_file)
    im.save('img/hide_two.png')

    pix = im.load()
    for x, y in product(xrange(im.size[0] - 1), xrange(im.size[1])):
        if pix[x, y][0] - pix[x + 1, y][0] < 3:
            pix[x, y] = (255,255,255)
        else:
            pix[x, y] = (0,0,0)

    im.save('img/solved_two.png')
    _file.close()
    return


def seek_three():

    _file = cStringIO.StringIO(urllib.urlopen( PATH + 'skryvacka3.png').read())
    im    = Image.open(_file)
    im.save('img/hide_three.png')

    pix = im.load()    
    for x, y in product(xrange(0, im.size[0] - 2, 2), xrange( im.size[1] )):
            if bool(pix[x, y][0]) != bool(pix[x + 2,y][0]):
                pix[x, y] = (0,0,0)
            else:
                pix[x, y] = (255,255,255)
    for x, y in product(xrange(im.size[0]), xrange(0,im.size[1] - 2,2)):
            if bool(pix[x, y][0]) != bool(pix[x, y + 2][0]):
                pix[x, y] = (0,0,0)
            else:
                pix[x,y] = (255,255,255)
    
    im.save('img/solved_three.png')
    _file.close()
    return


if __name__ == '__main__':

    seek_one()
    seek_two()
    seek_three()