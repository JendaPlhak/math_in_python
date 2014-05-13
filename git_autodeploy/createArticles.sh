#!/bin/bash
DIR=$1
for STUD in "Jendas" "Kvagrs";
do
    for TASK in `ls ${DIR}/../${STUD}Work/ | grep ".*task"`
    do
        python article.py ${DIR}/../${STUD}Work/${TASK}/cmt
    done
done