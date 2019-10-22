#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 打印倒立三角形

num = int(input("Please input the num: "))

for i in range(-num,num+1):
    if i < 0:
        i = -i
    else:
        i = i
    print(" "*i + "*"*(num+1-i))
