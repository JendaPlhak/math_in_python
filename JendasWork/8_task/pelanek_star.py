#!/usr/bin/env python
import scipy.stats as stats
from affine_transformation import *


def pelanek_star(rec=5):

    a = 500
    points = [ PointGroup(square(500)) ]

    trans  = [  array([[ 0.255, 0     , 0.3726 * a],
                       [ 0    , 0.255 , 0.6714 * a],
                       [ 0    , 0     , 1      ],
                      ]),

                array([[ 0.255, 0     , 0.1146 * a],
                       [ 0    , 0.255 , 0.2232 * a],
                       [ 0    , 0     , 1      ],
                      ]),

                array([[ 0.255, 0     , 0.6306 * a],
                       [ 0    , 0.255 , 0.2232 * a],
                       [ 0    , 0     , 1      ],
                      ]),

                combine([translation(-a/2, -a/2),
                        array([[ 0.370,-0.642 , 0.6356],
                               [ 0.642, 0.370 ,-0.0061],
                               [ 0    , 0     , 1      ],
                              ]),
                        translation(a/2, a/2)])
                ]

    points = iterReductionCopy( points,
                                identity(),
                                trans,
                                rec)

    points = applyTransform(points, translation(200, 200))

    drawPoints(points, "Pelanek_star")


def pelanek_star_iterative(n_i=5000):

    a = 1

    trans  = [  array([[ 0.255, 0     , 0.3726 * a],
                       [ 0    , 0.255 , 0.6714 * a],
                       [ 0    , 0     , 1      ],
                      ]),

                array([[ 0.255, 0     , 0.1146 * a],
                       [ 0    , 0.255 , 0.2232 * a],
                       [ 0    , 0     , 1      ],
                      ]),

                array([[ 0.255, 0     , 0.6306 * a],
                       [ 0    , 0.255 , 0.2232 * a],
                       [ 0    , 0     , 1      ],
                      ]),

                array([[ 0.370,-0.642 , 0.6356],
                       [ 0.642, 0.370 ,-0.0061],
                       [ 0    , 0     , 1      ],
                      ])
                ]

    randint = stats.rv_discrete( values=(range(4), (0.25, 0.25, 0.25, 0.25)) )
    points  = [array([0, 0, 1])]
    for i in randint.rvs(size=n_i):
        points.append(dot(trans[i], points[-1]))

    drawPoints(points, "Pelanek_star_random")



if __name__ == '__main__':

    # pelanek_star()
    pelanek_star_iterative()