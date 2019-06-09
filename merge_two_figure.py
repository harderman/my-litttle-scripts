#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'hh'

from PIL import Image

"""
拼接两张图片(上下拼接), 需指定大小
"""
img_arr = ['fig/screenshot003.png', 'fig/screenshot004.png']
to_image = Image.new('RGBA', (252, 189 * 2))
for i in range(len(img_arr)):
    from_image = Image.open(img_arr[i])
    # loc = ((i % 2) * 200, (int(i/2) * 200))
    loc = (0, (i % 2) * 189)
    print(loc)
    to_image.paste(from_image, loc)

to_image.save('fig/merged1.png')
