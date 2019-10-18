#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 打印斐波那契数列第n项

num = int(input("Please input the num: "))
a,b = (0,1)
for i in range(num):
   a,b = b,a+b
print(a)
