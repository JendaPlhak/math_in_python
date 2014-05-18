#!/usr/bin/env python
import logging
import sys
sys.path.append("../../JendasWork/2_task/")
sys.path.append("/home/ubuntu/math_in_python/JendasWork/2_task/")

import re

for i in xrange(6):
    sys.path.append("../../KvagrsWork/" + str(i + 1) +"_task/")
    sys.path.append("/home/ubuntu/math_in_python/KvagrsWork/" + str(i + 1) + "_task/")

from logging.handlers import RotatingFileHandler
from flask            import Flask, request, render_template
from StringIO         import StringIO

app = Flask(__name__)

from urlparse         import parse_qs
from pascals_triangle import plot_pascals_triangle

#Kvapil
from triangulation            import draw_triangulation
from segment_intersection     import draw_segment_intersection
#from chaos_game               import draw_chaos_game

from abstract_calling import evaluateFunction

tasksKvapil = {
       "collatzo"           : '1',
       "ulam_spiral"        : '1',
       "basic_graphics"     : '1',
       "gcd"                : '1',
       "pascals_triangle"   : '2',
       "turtle"             : '3',
       "polygon"            : '4',
       "effects"            : '4',
       "hide_and_seek"      : '4',
       "intersection"       : '5',
       "triangulation"      : '5',
       "gift_wrapping"      : '5',
       "chaos_game"         : '6'
    }

@app.route('/')
@app.route('/<name>')
def home(name=''):
    return render_template('home.html', name=name)

@app.route('/plhak/')
@app.route('/plhak/<task>')
def plhak(task=''):

    if task == 'pascals_triangle':

        n_layers = int(request.args.get('n_layers',0))
        d        = int(request.args.get('d',0))
    
        if n_layers < 0 or n_layers > 50 or d > 50:
            n_layers = 50
            d        = 2
#        if request.args:
#
#            arguments = dict(request.args)
#            funName   = arguments["funName"]
#            del arguments["funName"]
#            img = evaluateFunction("Jendas", funName, dict(request.args))
#            
#        else:

        # udelej file-like objekt (ma metody read, write, atd.) v pameti 
        output = StringIO()
        output.write( plot_pascals_triangle(n_layers, d, web=True) )
        output.seek(0)

        #base64_data = open( output, "rb").read().encode("base64").replace("\n", "")
        base64_data = output.read().encode("base64").replace("\n", "")
        output.close()

        #img = plot_pascals_triangle(n_layers, d)
        #base64_data = open( img, "rb").read().encode("base64").replace("\n", "")

        return render_template('plhak.html', task=task, img_data=base64_data)

    elif task.startswith('download&'):

        task = re.sub(r'download&', '', task)
        print "Proccesing download: ", task
        return render_template( 'JendasWork/1_task/collatzo.py' )

    else:    
        
        return render_template('plhak.html', task=task)


@app.route('/kvapil/') 
@app.route('/kvapil/<task>')
def kvapil(task=''):

    if task == 'triangulation':
        n     = int(request.args.get('num',0))
        check = request.args.get('checkbox',0)

        if n not in range(2,50):
            n = 3
        print check

        # udelej file-like objekt (ma metody read, write, atd.) v pameti 
        output = StringIO()
        output.write( draw_triangulation(n, min_side=check, web=True) )
        output.seek(0)

        #base64_data = open( output, "rb").read().encode("base64").replace("\n", "")
        base64_data = output.read().encode("base64").replace("\n", "")
        output.close()
    
        return render_template('kvapil.html', task=task, numTask=tasksKvapil[task], img_data=base64_data)

    elif task == 'intersection':
        n      = int(request.args.get('num',0))
        length = int(request.args.get('len',0))
        print request.args.get('nazevFunkce',)

        if n not in range(2,50) or length not in range(20,150):
            n      = 15
            length = 100

        img         = draw_segment_intersection(n, length)
        base64_data = open( img, "rb").read().encode("base64").replace("\n", "")
    
        return render_template('kvapil.html', task=task, numTask=tasksKvapil[task], img_data=base64_data)

    elif task.startswith('download&'):

        task = re.sub(r'download&', '', task)
        print "Proccesing download: ", task
        
        return render_template( 'JendasWork/1_task/collatzo.py' )

    #elif task == 'chaos_game':
    #    n     = int(request.args.get('num', 0))
    #    ratio = int(request.args.get('ratio', 0))
#
#    #    if n not in range(3,20) or ratio < 0 or ratio > 1:
#    #        n     = 3
#    #        ratio = 0.5
#
#    #    img         = draw_chaos_game(n, ratio)
#    #    base64_data = open( img, "rb").read().encode("base64").replace("\n", "")
#
    else:
        return render_template('kvapil.html', task=task, numTask=tasksKvapil[task])


if __name__ == '__main__':
    handler = RotatingFileHandler('/var/log/flask/flaskWebserver.log', maxBytes=100000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(port=8080, debug=True)