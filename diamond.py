#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 打印n阶菱形

num = int(input("Please input the num: "))

for i in range(-num,num+1):
    if i < 0:
        i = -i
    else:
        i = i
    print(" "*(i) + "*"*(2*(num+1-i)-1) )       # 只需要关注前面空格数和*号个数，找规律
