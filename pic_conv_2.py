#!/anaconda3/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'hh'

import cv2

old_img_path = "./fig/IMG_2952.JPG"

img = cv2.imread(old_img_path)

new_img_path = "./fig/gray.jpg"

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite(new_img_path, gray_image)
