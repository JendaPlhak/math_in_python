#!/bin/bash
for STUD in "Jendas" "Kvagrs";
do
    for TASK in `ls ../${STUD}Work/ | grep ".*task"`
    do
        echo Processing ${STUD}Work/${TASK}
        python article.py ../${STUD}Work/${TASK}/cmt
    done
done