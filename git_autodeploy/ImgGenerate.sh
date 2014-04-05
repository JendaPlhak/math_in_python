#!/bin/sh

for STUD in "Jendas" "Kvagrs";
do
    IMG_PATH=/home/ubuntu/math_in_python/webserver/layout2/static/img/${STUD}Work
    cd /home/ubuntu/math_in_python/${STUD}Work

    for dir in */
    do
        dir=${dir%*/}
        cd ${dir}
        echo ${dir##*/}

        if [ ! -d "img" ]; then
            mkdir img
        fi

        for file in $(find . -maxdepth 1 -perm -111 -type f -name "*.py")
        do
            echo ${file}
            "${file}"
        done

        if [ ! -d "${IMG_PATH}/${dir}/" ]; then
            mkdir -p ${IMG_PATH}/${dir}/
        fi
        
        cp img/* ${IMG_PATH}/${dir}/
        cd ..
    done
done
