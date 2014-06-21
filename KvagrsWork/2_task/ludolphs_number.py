#!/usr/bin/env python

import time
import numpy as np

from math    import pi, floor, copysign, factorial
from decimal import *


sign = lambda x: copysign(1, x)
# set decimal precision
#getcontext().prec = 49
context = Context(prec=49)

def compare_pie(_pi):

    python_pi = str( Decimal(pi) )
    _pi       = str( _pi )
    dec_num   = len( python_pi )
    _pi       = _pi[:dec_num]

    for i in xrange( len(python_pi) ):
        if python_pi[i] != _pi[i]:
            _pi = _pi[:i] +'<span style="color:red">'+ _pi[i:] +'</span>'
            break

    print ">>> Differs at {} position.".format(i-1)
    return _pi


def gregory_leibnitz(_time=False, n=1000):

    _pi        = 0.
    k          = 0
    start_time = time.time()

    while time.time() - start_time < _time or k < n:
        _pi += (-1)**k * 1. / (2 * k + 1)
        k   += 1

    return Decimal(4 * _pi)


def archimedes(_time=1, rep=5):

    n    = Decimal(3)
    side = Decimal(1)
    k    = 0
    start_time = time.time()
    while time.time() - start_time < _time or k < rep:
        n    *= 2
        half  = Decimal(side / Decimal(2))
        a     = Decimal(1 - half**2).sqrt()
        b     = 1 - a
        side  = Decimal(b**2 + half**2).sqrt()
        k    += 1

    _pi   = Decimal(n * side)

    return _pi


def monte_carlo(_time=False, n=1000):

    start_time = time.time()
    k          = 0
    in_quarter = 0 

    while time.time() - start_time < _time or k < n:
        x, y = np.random.random(2)
        if x**2 + y**2 < 1:
            in_quarter += 1
        k += 1
    _pi = 4. * in_quarter / k
    
    return Decimal(_pi)


def chudnovsky(_time=1):

    S = Decimal(0)
    n = 0
    start_time = time.time()
    while time.time() - start_time < _time:

        tmp  = Decimal(-1)**n * Decimal(factorial(6 * n)) / (factorial(n)**3 * factorial(3 * n))
        tmp *= Decimal((545140134* n + 13591409) / (640320**(3 * n)))

        S += tmp
        n += 1

    _pi = Decimal(426880 * 10005**0.5) / S

    return Decimal(_pi)


if __name__ == '__main__':

    
    _pi = Decimal(pi)
    print "Python math module:"
    print ">>> {}".format(_pi)

    print "Monte carlo, time: 1 sec:"
    monte_carlo = monte_carlo(_time=1)
    print ">>>    {}".format( monte_carlo )
    print ">>> D: {}".format( abs(_pi - monte_carlo) )
    print ">>>    " + compare_pie( monte_carlo )

    print "Gregory-Leibnitz, time: 1 sec:"
    gregory_leibnitz = gregory_leibnitz(_time=1)
    print ">>>     {}".format( gregory_leibnitz )
    print ">>> D:  {}".format( abs(_pi - gregory_leibnitz) )
    print ">>>    " + compare_pie( gregory_leibnitz )

    print "Archimedes, time: 1 sec:"
    archimedes = archimedes(_time=1)
    print ">>>    {}".format( archimedes )
    print ">>> D: {}".format( abs(_pi - archimedes) )
    print ">>>    " + compare_pie( archimedes )
    
    print "Chudnovsky, time: 1 sec:"
    chudnovsky = chudnovsky()
    print ">>>    {}".format( chudnovsky )
    print ">>> D: {}".format( abs(_pi - chudnovsky) )
    print ">>>    " + compare_pie( chudnovsky )