#!/usr/bin/env python
import sys
import os
import re

# local directory
directory =  sys.argv[1]

# get the variable part of directory 
part_dir = re.match(".*/(.*?Work/.*?_task/)cmt", directory).group(1)

# send warning
if not os.path.isdir( directory ):
    print "Could not find dir: %s" % directory
    sys.exit()

# cycle through all the files in directory      
for _file in os.listdir( directory ):


    # only if commentar
    if _file.endswith(".cmt"):

        # open commentary
        with open( directory +'/'+ _file ,'r') as f:
            commentary = f.read()
        
        # get the name
        _file_name = _file[ : _file.index('.cmt') ]
        
        # if the task directory does not exists, make it happen!
        if not os.path.exists( '../webserver/layout2/templates/'+ part_dir ):
            os.makedirs( '../webserver/layout2/templates/'+ part_dir )

        # create new file for the article
        with open( '../webserver/layout2/templates/'+ part_dir +'article_'+ _file_name +'.html','w') as article:
            commentary = commentary.split('\n\n')
        
            # article formatting
            for par in commentary:
                
                # skip any html tagged paragraf in *.cmt
                if re.match(r'^<(\w+)>.*(<\\?\1)$'):
                    article.write( par )

                # if it does not find and img it just adds paragraf
                if '&img=' not in par:
                    article.write('<p>\n'+\
                                  par  +\
                                  '\n</p>\n\n')
                else:
                    # slicing the par for img and alt
                    img = re.findall('"([^"]*)"', par)[0]
                    alt = re.findall('"([^"]*)"', par)[1]

                    if 'width' in par:
                        width = re.findall('"([^"]*)"', par)[2]
                    else:
                        width = '500'

                    article.write('<img ')
                    if 'inline' in par:
                        article.write('class="inline_img" ')

                    article.write('src="../static/img/'+ part_dir + img + '"\
                                  alt="'+ alt +'"\
                                  width="'+ width +'"/>\n')
            # finally adding buttons for codes
            article.write('<div class="menuCode">\
                           \r   <ul>\
                           \r       <li><span id="buttonCode">Show code</span></li>\
                           \r       <li><a href="'+ _file_name+'.py">Get code</a></li>\
                           \r       <li><a href="https://github.com/JendaPlhak/math_in_python/blob/master/'+ part_dir + _file_name +'.py">Get Git</a></li>\
                           \r   </ul>\
                           \r</div>')