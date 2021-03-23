#coding:utf-8
"""
本文件用于从海量日志中提取关键日志 eg: 从dest.log 文件中提取 error warning 相关的日志
python log_collection.py -f dest.log -l "error&warning"
"""

import os
import sys
import re
import argparse


def argvparse():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='从日志文件获取目标日志')
    parser.add_argument('-f', '--filename', dest='filename', help='dest log file')
    parser.add_argument('-l', '--log', dest='log', help='想得到的日志，要是有多个关键字，请用&分割')
    args = parser.parse_args()
    return args


def state_goto():
    """collect the goto state from zealotPcap run log"""
    flag = 0
    args = argvparse()

    filename = args.filename.split("//")[-1]
    texts = args.log.split('&')
    print(filename)
    print(texts)

    with open(filename) as f:
        for line in f.readlines():
            for text in texts:
                if(re.search(text, line) != None):
                    print line
                    break

if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print "Error parameter number, use --help for detail"
        exit()
    state_goto()

