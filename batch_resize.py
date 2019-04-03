#!/anaconda3/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'hh'

import os

import cv2

"""
将图片批量转化成 200*200 大小
你也可以自行调整大小

使用说明：
1. 在此程序所在目录新建一文件夹"old_size"
2. 把所有需要转换的图片放入"old_size"中
3. 运行此程序，你将获取一文件夹"new_size"，转换成功
"""


def batch_resize():
    dirs = os.listdir('./old_size')
    try:
        os.mkdir('./new_size')
        for old in dirs:
            old_path = os.path.join('./old_size', old)
            new_path = os.path.join('./new_size', old)
            old_image = cv2.imread(old_path)
            new_image = cv2.resize(old_image, (200, 200))

            cv2.imwrite(new_path, new_image)
    except FileExistsError:
        for old in dirs:
            old_path = os.path.join('./old_size', old)
            new_path = os.path.join('./new_size', old)
            old_image = cv2.imread(old_path)
            new_image = cv2.resize(old_image, (200, 200))

            cv2.imwrite(new_path, new_image)


if __name__ == '__main__':
    batch_resize()
