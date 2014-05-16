#!/usr/bin/env python
from affine_transformation import *


def realtives(transforms, rec=8, a=400, title=""):

    points = [ PointGroup(square(a)) ]

    points = iterReductionCopy( points,
                                scaling(0.5, 0.5),
                                transforms,
                                rec)

    drawPoints(points, "Sierpinski_relative_" + title)



if __name__ == '__main__':

    a = 400

    realtives(  [identity(), 
                 translation(a/2, 0),
                 translation(a/4, a/2)],
                 a=a,
                 title="triangle",
            )

    realtives(  [identity(), 
                 translation(a/2, 0),
                 translation(a/2, a/2)],
                 a=a,
                 title="right",
            )

    realtives(  [identity(), 
                 combine([ translation(a/2, 0),   rotate( 90, x=3*a/4, y=a/4)   ]),
                 combine([ translation(a/2, a/2), rotate(-90, x=3*a/4, y=3*a/4) ])],
                 a=a,
                 title="rotate"
            )
    
    realtives(  [combine([rotate(-90, x=a/4, y=a/4)   ]),
                 translation(a/2, 0), 
                 combine([ translation(a/2, a/2), rotate(90, x=3*a/4, y=3*a/4) ])],
                 a=a,
                 title="pen"
            )

    realtives(  [combine([rotate(180, x=a/4, y=a/4)   ]),
                 translation(a/2, 0), 
                 combine([ translation(a/2, a/2), rotate(180, x=3*a/4, y=3*a/4) ])],
                 a=a,
                 title="A"
            )