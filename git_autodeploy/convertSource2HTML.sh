#!/bin/bash

for STUD in "Jendas" "Kvagrs";
do
    CUR_PATH=/home/ubuntu/math_in_python/webserver/layout2/templates/${STUD}Work
    cd /home/ubuntu/math_in_python/${STUD}Work

    for dir in */
    do
        dir=${dir%*/}
        cd ${dir}
        echo ${dir##*/}


        if [ ! -d "${CUR_PATH}/${dir}/" ]; then
            mkdir -p ${CUR_PATH}/${dir}/
        fi

        for file in $(find . -maxdepth 1 -perm -111 -type f -name "*.py")
        do
            file_name=$(echo $file | grep -E '\w+\.py' -o)
            new_file=${CUR_PATH}/${dir}/${file_name}
            echo "  "Converting $file_name

            cp -f $file_name $new_file
        done
        cd ..
    done
done

TARGET=/home/ubuntu/math_in_python/webserver/layout2/templates/JendasWork
# some exceptional files
cp -f /home/ubuntu/math_in_python/JendasWork/7_task/complex_fractals.pyx $TARGET/7_task/complex_fractals.py