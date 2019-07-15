#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'hh'

import cv2

"""
图片裁剪，宽度不变，高度裁剪为原图的1/4
你也可以自行调整大小
"""


def img_cut(img):
    raw_shape = img.shape
    new_shape = [*raw_shape]
    new_shape[0] = int(new_shape[0] / 4)
    new_img = img[0:new_shape[0], 0:new_shape[1]]
    return new_img


if __name__ == '__main__':
    path = "./fig/too_large_image.png"
    img = cv2.imread(path)
    new_img = img_cut(img)
    cv2.imwrite('./fig/cut_img.png', new_img)
