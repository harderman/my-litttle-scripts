#!/anaconda3/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'hh'

import cv2

old_img_path = "./fig/IMG_2952.JPG"

img = cv2.imread(old_img_path, 0)

new_img_path = "./fig/gray.jpg"

ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

cv2.imwrite(new_img_path, thresh2)
