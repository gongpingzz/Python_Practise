#!/bin/bash

file="1.txt"

while IFS= read -r line
do
        # display $line or do somthing with $line
        echo ${line}
        filepath=$(find -name ${line})
        echo ${filepath}
        mv ${filepath} ./dstdir/
done <"$file"
