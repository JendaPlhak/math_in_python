#!/usr/bin/env python
from affine_transformation import *


def pelanek_star(rec=8):

    a = 200
    points = [ PointGroup(square(200)) ]

    b = a
    trans  = [  array([[ 0.255, 0     , 0.3726 * b],
                       [ 0    , 0.255 , 0.6714 * b],
                       [ 0    , 0     , 1      ],
                      ]),

                array([[ 0.255, 0     , 0.1146 * b ],
                       [ 0    , 0.255 , 0.2232 * b],
                       [ 0    , 0     , 1      ],
                      ]),

                array([[ 0.255, 0     , 0.6306 * b],
                       [ 0    , 0.255 , 0.2232 * b],
                       [ 0    , 0     , 1      ],
                      ]),

                combine([translation(-100, -100),
                        array([[ 0.370,-0.642 , 0.6356],
                               [ 0.642, 0.370 ,-0.0061],
                               [ 0    , 0     , 1      ],
                              ]),
                        translation(100, 100)])
                ]
    points = iterReductionCopy( points,
                                identity(),
                                trans,
                                rec)

    points = applyTransform(points, translation(300, 300))

    drawPoints(points, "Pelanek_star")


if __name__ == '__main__':

    pelanek_star()