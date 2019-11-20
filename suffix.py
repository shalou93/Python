#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 打印出文件名的后缀

def get_suffix(filename, has_dot=False):
    pos = filename.rfind('.')

    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ""

print(get_suffix('12.py'))
