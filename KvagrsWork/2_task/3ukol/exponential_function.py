#! usr/bin/python

def extend_integer(x):

    n = 0
    while (10 * x) % 10 != 0:
        x *= 10
        print x
        n += 1
    return x, n


def exponent_iteration(x, y):
    # calculate x**y for x, y real using iteration
    pass


X = 3.451264
Y = 1.1586455

if __name__ == '__main__':

    print extend_integer(15.16316)