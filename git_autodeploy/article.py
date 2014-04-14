#!/usr/bin/env python
import sys
import os
import re

# local directory
directory =  sys.argv[1]
# get the variable part of directory 
part_dir = directory[ directory.index('templates/') + len('templates/'): ]

# cycle through all the files in directory
for _file in os.listdir( directory ):

    # only if commentar
    if _file.endswith(".cmt"):

        # open commentary
        with open( directory + _file ,'r') as f:
            commentary = f.read()
        
        # get the name
        _file_name = _file[ _file.index('_') + 1:]
    
        # create new file for the article
        with open( directory +'article_'+ _file_name +'.html','w') as article:
            commentary = commentary.split('\n\n')
        
            # article formatting
            for par in commentary:
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