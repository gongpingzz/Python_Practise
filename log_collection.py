#coding:utf-8

import os
import sys
import re
import argparse


substr1 = "now state name"
substr2 = "packet num"
substr3 = "############# session"
substr4 = "#############"
substr5 = "UtsCallBackFunc"
substr6 = "recv numeric data"
substr7 = "recv field data"
substr8 = "Zealot-debug:"
substr9 = "func=Chunk"
substr10 = "filerestore"
substr11 = "func=AddDataToStreamingCache"

#f2 = open('state_log.txt', 'w')


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

