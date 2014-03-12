#!/usr/bin/env python

import sys
sys.path.append("../../JendasWork/2_task/")
sys.path.append("/home/ubuntu/math_in_python/JendasWork/2_task/")

from flask import Flask, render_template
app = Flask(__name__)

from urlparse         import parse_qs
from bottle           import route, run, template, static_file
from pascals_triangle import plot_pascals_triangle


@app.route('/')
@app.route('/<name>')
def home(name=''):
    return render_template('home.html', name=name)


@app.route('/plhak/')
@app.route('/plhak/<task>')
def plhak(task=''):
    return render_template('plhak.html', task=task)


@app.route('/plhak/pascal/<qstring>')
def index(qstring):
    print "Attempting to print pascals triangle"
    print "     Parameters: %s\n" % qstring

    params = parse_qs(qstring)
    print params
    if not (int(params["n_layers"][0]) > 0 and int(params["n_layers"][0]) < 150):
        params["n_layers"][0] = 50
        
    return plot_pascals_triangle( int(params["n_layers"][0]),
                                  int(params["d"][0])
                                )


#def kvapil():
#    return render_template('kvapil.html')
#
@app.route('/kvapil/') 
@app.route('/kvapil/<task>')
def kvapil(task=''):
    return render_template('kvapil.html', task=task)




if __name__ == '__main__':
    app.run(port=8080)