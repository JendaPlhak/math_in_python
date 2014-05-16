#!/usr/bin/env python
import sys
sys.path.append("../3_task")

from numpy import array, dot
from math  import sin, cos, pi
from test_pictures import regularPolygon
from Turtle   import Turtle

def identity():
    return array([[ 1 , 0 , 0 ],
                  [ 0 , 1 , 0 ],
                  [ 0 , 0 , 1 ],
                 ])


def rotate(angle, x=300, y=300):

    angle = angle/180. * pi

    t = translation(x, y)
    t = dot(t,array([[ cos(angle),-sin(angle) , 0 ],
                     [ sin(angle), cos(angle) , 0 ],
                     [ 0         , 0          , 1 ],
                    ]))
    t = dot(t,translation(-x, -y))
    return t


def scaling(s_x, s_y):
    return array([[ s_x , 0   , 0 ],
                  [ 0   , s_y , 0 ],
                  [ 0   , 0   , 1 ],
                 ])


def translation(t_x, t_y):
    return array([[ 1 , 0 , t_x ],
                  [ 0 , 1 , t_y ],
                  [ 0 , 0 , 1   ],
                 ])


def combine(t_list):   # Take list of transformations and multiply them

    result = t_list.pop()
    while t_list:
        result = dot(result, t_list.pop())
    return result



def applyTransformDraw(points, transform, rec):

    draw = Turtle("Square", start_coord=[100,100])
    l    = len(points)
    draw.connectPoints(points)

    for _ in xrange(rec):
        for i in xrange(l):
            points[i] = dot(transform, points[i])
        draw.connectPoints(points)
    draw.dumpImage()


def applyTransform(points, transform, rec=1):

    for _ in xrange(rec):
        for point in points:
            point.applyTrans(transform)
    return points


def drawPoints(points, title, clr='green'):

    draw = Turtle(title, background=True)
    if isinstance(points[0], PointGroup):
        for pointGroup in points:
            draw.connectPoints(pointGroup.points)
    else:
        for point in points:
            draw.addPoint((500*point[0] + 200, 500*point[1] + 200), clr)
    draw.dumpImage()

def copyPoints(points):

    copy_points = []
    for pointGroup in points:
        copy_points.append(pointGroup.copy())
    return copy_points


def iterReductionCopy(points, reduction, transforms, rec):
    
    for _ in xrange(rec):
        print "Iteration NO. %d" % (_ + 1)
        points     = applyTransform(points, reduction)
        new_points = []

        for trans in transforms:
            transformed = applyTransform(copyPoints(points), trans)
            new_points.extend(transformed)
        points = new_points
    print "Calculation finished!"
    return points



def square(a=100):
    return [array([0, 0, 1]),
            array([0, a, 1]),
            array([a, a, 1]),
            array([a, 0, 1])]



class PointGroup():

    def __init__(self, points):
        self.points = points

    def applyTrans(self, transform):

        for i in xrange(len(self.points)):
            self.points[i] = dot(transform, self.points[i])
        return self

    def copy(self):
        cp = []
        for point in self.points:
            cp.append(list(point))
        return PointGroup(cp)




if __name__ == '__main__':

    print applyTransform(square(), 
                         combine([ rotate(10, 150, 150), scaling(1.1, 0.8)]), 
                         100)

