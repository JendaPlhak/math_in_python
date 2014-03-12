#!/usr/bin/env python
from decimal import *
import gmpy
import math
import numpy as np
getcontext().prec = 30


def leibniz(max_error = 10**(-2)):

    print "Calculating Pi using method of Leibniz..."

    i    = Decimal(1)
    pi   = Decimal(0)
    plus = True
    cur_error = Decimal(max_error) + Decimal(1)

    while max_error < cur_error: # Can be expected, that error will be 
                                 # approximately at most equal to the 10*(n + 1 member of series)
        if plus:   
            pi  += 1/i
            plus = False
        else:
            pi  -= 1/i
            plus = True

        i  += 2
        if i % 10000 == 1:
            cur_error = 10/i

    return pi * 4


def archimedes(max_rounds=10**3):

    print "Calculating Pi using method of Archimedes..."

    a = 2*Decimal(3).sqrt()
    b = Decimal(3)
    n = 0

    while n < max_rounds:
        n += 1
        a = (2 * a * b) / (a + b)
        b = (a * b).sqrt()
    return a


def monte_carlo(max_rounds=1000, n_per_round = 100):

    print "Calculating Pi using Monte Carlo method..."
    n   = 0
    out = 0
    while n < max_rounds:
        for x, y in np.random.random((n_per_round, 2)):
            if (x*x + y*y) ** 0.5 > 1:
                out += 1
        n += 1

    inside = max_rounds * n_per_round - out
    ratio  = Decimal(out) / Decimal(inside)
    return 4 / (ratio + 1)


def bellard_formula(n_steps = 1000): # http://en.wikipedia.org/wiki/Bellard%27s_formula

    print "Calculating Pi using formula of Bellard..."

    sum_ = Decimal(0)

    for i in xrange(n_steps):
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
    return sum_ * 1/Decimal(1 << 6)


if __name__ == "__main__":

    print leibniz()
    print archimedes()
    print monte_carlo()
    print bellard_formula()
    print gmpy.pi(125)
    print 