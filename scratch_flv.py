#!/anaconda3/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'hh'

import os
import shutil

"""
提取多个文件夹中的flv格式视频

使用说明：
1. 在此程序所在目录新建两个文件夹"old_flv_file"，"new_flv_file"
2. 把所有需要提取的flv视频放入"old_flv_file"中
3. 运行此程序，将old_flv_file中所有的文件夹里的flv视频提取到new_flv_file文件夹中
"""


def scratch_flv():
    dirs = os.listdir('./old_flv_file')
    if '.DS_Store' in dirs:
        dirs.remove('.DS_Store')
    for old in dirs:
        old_path = os.path.join('./old_flv_file', old)
        old_path_path = os.listdir(old_path)
        for o_pp in old_path_path:
            if 'flv' in o_pp:
                shutil.move(os.path.join(old_path, o_pp), './new_flv_file')


if __name__ == '__main__':
    scratch_flv()
//
