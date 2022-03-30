# coding=utf-8

import re

patRecord = re.compile('.*- .*')

class parser:
    """
    文本解析
    """
    def __init__(self):
        ''' init function '''
        self.txtfile = "listing20-1.txt"
        self.textlist = []

    def findText(self):
        ''' 找出文本块 '''
        strtmp = ''
        with open(self.txtfile) as f:
            for line in f.readlines():
                # 怎么判断空行？
                if line in ['\n', '\r\n']:
                    if len(strtmp) > 0:
                        self.textlist.append(strtmp)
                        strtmp = ''
                    continue
                strtmp += line

    def findList(self):
        ''' 找到列表 '''
        for item in self.textlist:
            # print(item)
            if patRecord.match(item):
                print('line match:\n {}'.format(item))
            else:
                print('line not match:\n {}'.format(item))


class showOnline:
    """
    在浏览器中显示文本
    """
    def __init__(self):
        pass


# 添加标记
def mark(block, types):
    ''' add mark '''
    if type[0] == 1:
        block = "<h2>" + block + "</h2>" 

    if type[1] == 1:
        block = "<h1>" + block + "</h1>" 

    if type[2] == 1:
        block = "<li>" + block + "</li>" 

    return block

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


if __name__ == '__main__':
    ''' main function '''
    p = parser()
    p.findText()
    for item in p.textlist:
        type = handleRules(p.textlist, item)
        item = mark(item, type)
        print(item)
