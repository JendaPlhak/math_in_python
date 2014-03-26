#!/usr/bin/env python
import logging
import sys
sys.path.append("../../JendasWork/2_task/")
sys.path.append("/home/ubuntu/math_in_python/JendasWork/2_task/")
sys.path.append("../../KvagrsWork/5_week/")
sys.path.append("/home/ubuntu/math_in_python/KvagrsWork/5_week/")

from logging.handlers import RotatingFileHandler
from flask            import Flask, request, render_template

app = Flask(__name__)

from urlparse         import parse_qs
from bottle           import route, run, template, static_file
from pascals_triangle import plot_pascals_triangle
from PIL              import Image

#Kvapil
from triangulation            import draw_triangulation
from segment_intersection     import draw_segment_intersection


@app.route('/')
@app.route('/<name>')
def home(name=''):
    return render_template('home.html', name=name)

@app.route('/plhak/')
@app.route('/plhak/<task>')
def plhak(task=''):

    if task == 'pascal':

        n_layers = int(request.args.get('n_layers',0))
        d        = int(request.args.get('d',0))
    
        if n_layers < 0 or n_layers > 50 or d > 50:
            n_layers = 50
            d        = 2
    
        img = plot_pascals_triangle(n_layers, d)
        base64_data = open( img, "rb").read().encode("base64").replace("\n", "")

        return render_template('plhak.html', task=task, img_data=base64_data)
    else:    

        return render_template('plhak.html', task=task)

#@app.route('/plhak/<qstring>')
#def index(qstring):
#    print "Attempting to print pascals triangle"
#    print "     Parameters: %s\n" % qstring
#
#    params = parse_qs(qstring)
#    print params
#    if not (int(params["n_layers"][0]) > 0 and int(params["n_layers"][0]) < 150):
#        params["n_layers"][0] = 50
#        
#    return plot_pascals_triangle( int(params["n_layers"][0]),
#                                  int(params["d"][0]),
#                                  save=False
#                                )


@app.route('/kvapil/') 
@app.route('/kvapil/<task>')
def kvapil(task=''):

    if task == 'triangulation':
        n = int(request.args.get('num',0))

        if n not in range(2,50):
            n = 3
        
        img         = draw_triangulation(n)
        base64_data = open( img, "rb").read().encode("base64").replace("\n", "")
    
        return render_template('kvapil.html', task=task, img_data=base64_data)

    elif task == 'intersection':
        n      = int(request.args.get('num',0))
        length = int(request.args.get('len',0))

        if n not in range(2,50) or length not in range(20,150):
            n      = 15
            length = 100

        img         = draw_segment_intersection(n, length)
        base64_data = open( img, "rb").read().encode("base64").replace("\n", "")
    
        return render_template('kvapil.html', task=task, img_data=base64_data)

    else:
        return render_template('kvapil.html', task=task)

if __name__ == '__main__':
    handler = RotatingFileHandler('/var/log/flaskWebserver.log', maxBytes=100000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(port=8080, debug=True)