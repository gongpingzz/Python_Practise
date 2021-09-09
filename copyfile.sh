#!/bin/bash

# 遍历文件中的文件，查找文件位置，复制到另一个目录下

file="1.txt"

while IFS= read -r line
do
        # display $line or do somthing with $line
        echo ${line}
        filepath=$(find -name ${line})
        echo ${filepath}
        cp ${filepath} ./dstdir/
done <"$file"
