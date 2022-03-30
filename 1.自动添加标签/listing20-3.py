# -*- encoding=utf-8 -*-
import re

# 添加标记
def mark(block, types):
    ''' add mark '''
    if type[0] == 1:
        block = "<h2>" + block + "</h2>" 

    if type[1] == 1:
        block = "<h1>" + block + "</h1>" 

    if type[2] == 1:
        block = "<li>" + block + "</li>" 

