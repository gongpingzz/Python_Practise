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



if __name__ == '__main__':
    ''' main function '''
    p = parser()
    p.findText()
    # for item in p.textlist:
    #     print(item)
    p.findList()