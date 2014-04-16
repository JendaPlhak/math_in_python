#!/usr/bin/env python
import scipy.stats as stats
from affine_transformation import *


def barnsley_fen(n_i=5000):

    a = 500
    points = [ PointGroup(square(500)) ]

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
    points  = [array([0, 0, 1])]
    for i in randint.rvs(size=n_i):
        points.append(dot(trans[i], points[-1]))

    drawPoints(points, "Pelanek_star_random")


if __name__ == '__main__':

    barnsley_fen()