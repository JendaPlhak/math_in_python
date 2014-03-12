#!/bin/sh

STUD="Jendas"
IMG_PATH=/home/jendas/skola/math_in_python/webserver/layout2/static/img/${STUD}Work


cd /home/jendas/skola/math_in_python/${STUD}Work

for dir in */
do
    dir=${dir%*/}
    cd ${dir}

    if [ ! -d "img" ]; then
        mkdir img
    fi

    for file in $(find . -maxdepth 1 -perm -111 -type f)
    do
        echo ${file}
        "${file}"
    done

    if [ ! -d "${IMG_PATH}/${dir}/" ]; then
        mkdir -p ${IMG_PATH}/${dir}/
    fi

    cp img/* ${IMG_PATH}/${dir}/

    echo ${dir##*/}
    cd ..
done