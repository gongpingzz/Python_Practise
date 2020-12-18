# coding = UTF-8
# image2base64.py

"""
this will  convert image file to Base64 string
"""

import os
import base64
import argparse

#def get_filename(absolute_path):


def write_to_txt(string,filename): #(base64字符串，绝对路径文件名)
    (dir_name,base_filename) = os.path.split(filename)
    base_filename = os.path.splitext(base_filename)[0]
    suffix = '_base64.txt'
    txt_name = os.path.join(dir_name,base_filename + suffix ) #拼接包含路径的 txt 文件名
    #print(txt_name)
    #print(dir_name)
    f = open(txt_name,'w')
    f.write(string)
    f.close


def convert(filename):
    f=open(filename,'rb') #二进制方式打开图文件
    ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
    write_to_txt(ls_f,filename)
    f.close()


def get_parser():
    parser = argparse.ArgumentParser(description='change extension of files in a working directory')
    parser.add_argument('filename', metavar='FILENAME', type=str, nargs=1, help='photo`s filename')
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    filename = args['filename'][0]
    convert(filename)


if __name__ == '__main__':
    main()
