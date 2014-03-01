#!/usr/bin/env python

import sys
sys.path.append("2_cviceni/")

from bottle import route, run, template, static_file
from pascals_triangle import plot_pascals_triangle


@route('/')
def index():
    return '<b>Something is coming...</b>'

@route('/pascal/<param_string>')
def index(param_string):
    params = param_string.split("&")
    return plot_pascals_triangle(int(params[0]),int(params[1]))

@route('/ahoj/<name>')
def index(name):
    return '<b>ahoj {0}</b>\n<img src="http://25.media.tumblr.com/93a200d60363ff4e6b928d1ad1174c22/tumblr_n126y7hHEQ1tt6sj1o1_400.gif" alt="wiiiii">'.format(name)
run(host='localhost', port=8080)

