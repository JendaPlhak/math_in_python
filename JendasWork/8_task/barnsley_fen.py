#!/usr/bin/env python
import scipy.stats as stats
from PIL import Image, ImageDraw
from affine_transformation import *


def barnsley_fen(n_i=200000):

    a = 5
    points = [ PointGroup(square(a)) ]

    trans  = [  array([[ 0    , 0     , 0 ],
                       [ 0    , 0.16  , 0 ],
                       [ 0    , 0     , 1 ],
                      ]),

                array([[ 0.85 , 0.04  , 0  ],
                       [-0.04 , 0.85  , 1.6],
                       [ 0    , 0     , 1  ],
                      ]),

                array([[ 0.2 ,-0.26 , 0  ],
                       [ 0.23, 0.22 , 1.6],
                       [ 0   , 0    , 1 ],
                      ]),
                
                array([[-0.15, 0.28, 0   ],
                       [ 0.26, 0.24, 0.44],
                       [ 0    , 0  , 1   ],
                      ])
            ]

    randint = stats.rv_discrete( values=(range(4), (0.01, 0.85, 0.07, 0.07)) )
    point   = array([0, 0, 1])

    size = (512,1024)
    im   = Image.new('RGB', size)
    draw = ImageDraw.Draw(im)

    for i in randint.rvs(size=n_i):
        point = dot(trans[i], point)
        draw.point( (size[0]/2.1  + point[0]*size[0]/5.0, point[1]*size[1]/11.0),
                     fill='#0f0') 

    im.save("img/Barsley_fen.png", "PNG")


if __name__ == '__main__':

    barnsley_fen()