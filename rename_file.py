#!/anaconda3/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'hh'

import os

path = './new_flv_file'


def rename_file():
    dirs = os.listdir(path)
    if '.DS_Store' in dirs:
        dirs.remove('.DS_Store')

    for filename in dirs:
        old_path = os.path.join(path, filename)

        _1 = filename.find('_')
        # _2 = filename.rfind('_')

        new_file_name = filename[_1+1:]
        new_path = os.path.join(path, new_file_name)

        os.rename(old_path, new_path)


if __name__ == '__main__':
    rename_file()
