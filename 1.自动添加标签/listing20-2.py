# -*- encoding=utf-8 -*-
import re


def findBlock(file):
    ''' 找出文本块 ''' 
    texts = []
    strtmp = ''
    with open(file) as f:
        for line in f.readlines():
            # 怎么判断空行？
            if line in ['\n', '\r\n']:
                if len(strtmp) > 0:
                    texts.append(strtmp)
                    strtmp = ''
                continue
            strtmp += line
    return texts

def handleRules(texts, block):
    ''' 对应的规则 '''
    # check 标题
    # 标题： 只包含一行的文本块，长度最多为70，并且不以冒号结尾
    # 题目： 文档中的第一个文本块，前提条件是它属于标题
    # 列表项是以 - 打头的文本块
    # 
    # 怎么判断只有一行？
    
    patRecord = re.compile('.*- .*')
    title_type = 0
    subject_type = 0
    list_type = 0
    types = [title_type, subject_type, list_type]

    if len(block) < 70 and block[-1] != ':' :
        types[0] = 1

    if texts[0] == block and title_type == 1 :
        types[1] = 2

    if patRecord.match(block):
        types[2] = 3

    return types
