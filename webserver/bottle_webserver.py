#!/usr/bin/env python

import sys
sys.path.append("2_cviceni/")

from urlparse         import parse_qs
from bottle           import route, run, template, static_file
from pascals_triangle import plot_pascals_triangle


@route('/')
def index():
    return '<b>Something is coming...</b>'


@route('/pascal/<qstring>')
def index(qstring):
    print "Attempting to print pascals triangle"
    print "     Parameters: %s\n" % qstring

    params = parse_qs(qstring)
    print params
    return plot_pascals_triangle( int(params["n_layers"][0]),
                                  int(params["d"][0])
                                )


@route('/ahoj/<name>')
def index(name):
    return '<b>ahoj {0}</b>\n<img src="http://25.media.tumblr.com/93a200d60363ff4e6b928d1ad1174c22/tumblr_n126y7hHEQ1tt6sj1o1_400.gif" alt="wiiiii">'.format(name)
run(host='localhost', port=8080)
