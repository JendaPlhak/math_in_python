#!/usr/bin/env python
from decimal import *
import gmpy
import time
import sys
import math
import numpy as np
getcontext().prec = 1001



def leibniz():

    # print "Calculating Pi using method of Leibniz..."
    i    = Decimal(1)
    pi   = Decimal(0)
    plus = True

    start     = time.time()

    while time.time() - start < 1.: # Can be expected, that error will be 
                                    # approximately at most equal to the 10*(n + 1 member of series)
        if plus:   
            pi  += 1/i
            plus = False
        else:
            pi  -= 1/i
            plus = True

        i  += 2

    return pi * 4


def archimedes():

    # print "Calculating Pi using method of Archimedes..."
    a = 2*Decimal(3).sqrt()
    b = Decimal(3)
    n = 0

    start = time.time()

    while time.time() - start < 1.:
        n += 1
        a = (2 * a * b) / (a + b)
        b = (a * b).sqrt()
    return a


def monte_carlo(n_per_round = 100):

    # print "Calculating Pi using Monte Carlo method..."
    out   = 0
    start = time.time()

    n = 0
    while time.time() - start < 1.:
        n += 1
        for x, y in np.random.random((n_per_round, 2)):
            if (x*x + y*y) ** 0.5 > 1:
                out += 1

    inside = n * n_per_round - out
    ratio  = Decimal(out) / Decimal(inside)
    return 4 / (ratio + 1)


def bellard_formula(): # http://en.wikipedia.org/wiki/Bellard%27s_formula

    # print "Calculating Pi using formula of Bellard..."
    sum_  = Decimal(0)
    start = time.time()
    i     = 0

    while time.time() - start < 1.:
        sum_ += (
                    (-1)**i / Decimal(1 << 10*i)  \
                )                                 \
                *                                 \
                (                                 \
                    -Decimal(1 << 5)/(4*i + 1)    \
                    -Decimal(1)/(4*i + 3)         \
                    +Decimal(1 << 8)/(10*i + 1)   \
                    -Decimal(1 << 6)/(10*i + 3)   \
                    -Decimal(1 << 2)/(10*i + 5)   \
                    -Decimal(1 << 2)/(10*i + 7)   \
                    +Decimal(1)/(10*i + 9)        \
                )
        i += 1

    return sum_ * 1/Decimal(1 << 6)


def determinePrecision(pi):

    pi     = str(pi)
    pi_ref = str(gmpy.pi(10000))  # reference pi

    min_len = min(len(pi), len(pi_ref))

    i = 0
    while i < min_len and pi[i] == pi_ref[i]:
        i += 1
    return i


if __name__ == "__main__":

    print "Precision of Monte Carlo method: %d digits" % determinePrecision(monte_carlo())
    print "Precision of Leibniz method:     %d digits" % determinePrecision(leibniz())
    print "Precision of Archimedes method:  %d digits" % determinePrecision(archimedes())
    print "Precision of Ballards formula:   %d digits" % determinePrecision(bellard_formula())
    print 