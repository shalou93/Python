#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 打印乘法口诀表

for i in range(1,10):
    for j in range(1,i+1):
        print("{0}x{1}={2}".format(j,i,j*i),end=" ")
    print("\n")
