#!/anaconda3/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'hh'

import os

"""
合并txt

使用说明：
1. 在此程序所在目录新建一文件夹"old_txt"
2. 把所有需要转换的图片放入"old_txt"中
3. 运行此程序，你将获得一文件"new_txt.txt"，合并成功
"""


def merge_txt():
    dirs = os.listdir('./old_txt')
    for old in dirs:
        old_path = os.path.join('./old_txt', old)
        with open('new_txt.txt', 'a+') as new_txt:
            with open(old_path) as f:
                while True:
                    line = f.readline()
                    new_txt.write(line)
                    if not line:
                        break

            # new_txt.write('\n')


if __name__ == '__main__':
    merge_txt()
