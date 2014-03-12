#!/usr/bin/env python
import math
from decimal import Decimal



def exp_taylor(x, y, max_error=10**(-10)):    # Calculates x^y using Taylors series, see
                                             # http://www.wolframalpha.com/input/?i=taylor+series+a%5Ex
    ln_x        = math.log(x)
    y_pow       = 1
    n_fac       = 1
    ln_x_pow    = 1
    n           = 0

    n_th_term   = y_pow * ln_x_pow / n_fac
    sum_prod    = n_th_term

    while max_error < n_th_term:
        n        += 1
        n_fac    *= n
        ln_x_pow *= ln_x
        y_pow    *= y

        n_th_term = y_pow * ln_x_pow / n_fac
        sum_prod += n_th_term

    return sum_prod


def newton_sq_root(x, max_error=10**(-10)): #calculates x^(1/2)

    y    = x
    diff = (x/(2*y) - 0.5*y)
    while abs(diff) > max_error:
        y += diff
        diff = (x/(2*y) - 0.5*y)

    return y
    

def exp_bisection(x, exp, max_error=10**(-10)):
  if(exp >= 1):
    tmp = exp_bisection(x, exp / 2.)
    return tmp * tmp
  else:
    a = 0.;
    b = 1.0;

    sqr = newton_sq_root(x)
    acc = sqr  
    mid = b / 2.

    while(abs(mid - exp) > max_error):  # This method approximates the exponent by powers of 0.5
        sqr = newton_sq_root(sqr)  

        if mid <= exp:
          a    = mid
          acc *= sqr
        else:
          b    = mid
          acc *= (1./sqr)

        mid = (a + b) / 2.

    return acc;

if __name__ == "__main__":
    
    x = 35.50545456454646
    y = 1.574858754854588784545

    print "To Calculate: {0}^{1}".format(x, y)
    print "     Taylor:    %f" % exp_taylor(x, y)
    print "     Bisection: %f" % exp_bisection(x, y)
    print "     Python:    %f" % x ** y