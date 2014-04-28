#!/bin/sh

for img in sokoban/*.svg; do
    filename=${img%.*}
    convert ${filename}.svg -background white -flatten ${filename}.jpg
    rm ${filename}.svg
done


convert sokoban/* sokoban.gif

convert sokoban.gif sokoban/sokoban%05d.png  
avconv -i sokoban/sokoban%05d.png -filter:v "setpts=2.1*PTS" sokoban.avi  
