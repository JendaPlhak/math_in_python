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

            if re.match(r'^\s*html', commentary):
                article.write( commentary[ commentary.index('html') + 4 :] )
                sys.exit()

            commentary = commentary.split('\n\n')
            """
            # create cuts by html tags
            cuts = [m.span() for m in re.finditer(r'(<(\w+).*?>.*?</\2>)', commentary)]
            cuts = [x for y in cuts for x in y]

            # add beginning and ending cuts if needed
            if 0 not in cuts:
                cuts.insert(0, 0)
            if len(commentary) not in cuts:
                cuts.append( len(commentary) )

            # cut the commentary into pars and html elements    
            pars = []
            for i in range( len(cuts) - 1):
                pars.append( commentary[ cuts[i] : cuts[i + 1]] )
            
            # go through pars and do another slicing
            commentary = []
            for par in pars:
                if re.match(r'<(\w+).*?>.*?(</\1>)', par):
                    print "halooo"
                    print par
                    print "niciiic"
                    commentary.append( par )
                else:
                    print
                    print
                    print "splitted par", par.split('\n\n')
                    commentary.extend( par.split('\n\n'))
            
            print 
            print "cuts", cuts
            print
            print "pars:\n", pars
            
            for com in commentary:
                print
                print "com", com
            """

            # article formatting
            for par in commentary:
                
                """
                # skip any html tagged paragraf in *.cmt
                if re.match(r'^<(\w+).*?>.*?(</?\1>)$', par):
                    print "Writing par", par[:80]
                    article.write( par )
                """
                # if it does not find and img it just adds paragraf
                if '&img=' not in par:
                    #print "blba", par[:80]
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
                           \r</div>\
                           \r   <div class="code">\
                           \r   <pre>\
                           \r       <code class="python">\
                           \r{\% include '+ part_dir + _file_name +'.py \%}\
                           \r       </code>\
                           \r   </pre>\
                           \r</div>')