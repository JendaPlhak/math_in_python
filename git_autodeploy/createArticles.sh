#!/bin/bash

for STUD in "Jendas" "Kvagrs";
do
    for TASK in `ls ${1}/../${STUD}Work/ | grep ".*task"`
    do
        python article.py ../${STUD}Work/${TASK}/cmt
    done
done