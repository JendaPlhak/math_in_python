#!/usr/bin/env python
import sys
sys.path.append('../1_task')

from decimal   import *
from math      import log, factorial
#from gcd       import gcd_recursive_modulo
from itertools import product

context = Context(prec=49)

X = 2
Y = 3.11


def compare_exp(x,y, result):

    return

def logarithm(x, err=10**(-6)):

    n = 1
    x = x - 1
    term = Decimal( x ) 
    _sum = Decimal( term )

    if abs(x) < 1:
        while err < abs(term):
            n += 1
            term = Decimal( (-1)**(n + 1) * x**n / n )
            _sum += term

        return _sum

    else:
        _sum = logarithm(x - 1)
        while err < abs(term):
            n += 1
            term = Decimal( (-1)**(n) / (( x - 1)**n * n) )
            _sum += term

        return _sum

def p(x, a):
# calculates x**a

    result = 1
    for i in xrange(a):
        result *= x

    return result

def gcd_modulo(a, b):

    steps = 0
    while a % b != 0:
        tmp = a
        a   = b
        b   = tmp % b

        steps +=1

    return b


def root(S, n=2, eps=0.000001):
# calculates n-th root of S with eps precision
    
    S = Decimal(S)
    def f(z):
        return Decimal( z**n  - S)

    def derf(z):
        return Decimal(n - 1.) * Decimal( z**n )

    x_0 = Decimal( 10 )
    if derf(x_0) == 0:
        return None
    x_n = x_0 - context.divide( f(x_0), derf(x_0))

    while abs(x_n - x_0) / x_n > eps:
        #print f(x_0), Decimal( derf(x_0) )
        x_0 = x_n
        if derf(x_0) == 0:
            return None
        x_n = x_0 - context.divide(f(x_0), derf(x_0))

    return Decimal( x_n )



def taylor_series(x, y, n=10):

    logar  = log(x)
    result = 0

    for k in xrange(n):
        result += (p(logar, k) * p(y,k)) / factorial(k)

    return Decimal( result )


def fraction(y):
# rewrites y as a fraction naively
    
    int_part = int(y)
    decimal  = str( y - int_part )[2:]
    if not decimal:
        decimal = 0
        denom   = 1
    else:
        denom   = p(10, len( decimal ))
    decimal  = int( decimal )
    numer    = int_part * denom + decimal
    modul    = gcd_modulo(numer, denom)
    #print "MODUL", modul, numer, denom

    return numer / modul, denom / modul



def naive_method(x, y):

    exp, rot = fraction(y)
#    print exp, rot

    result = root(x, rot)
    if result == None:
        return None
    result = p(result, exp)

    return result


if __name__ == '__main__':

    args = [0.1, 11, 3.12, 1651]
    exps = [13.1, 2, 165, 0.123]


    for arg, exp in product(args, exps):
        print "<p>$x^y = {",arg,"}^{",exp,"}$</p>"
        print 
        print "<pre>"
        print ">>> {}".format( arg**exp)
        print ">>> {}".format( taylor_series(arg, exp))
        print ">>> {}".format( naive_method(arg, exp))
        print "</pre>"
        print 