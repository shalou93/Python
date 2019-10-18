#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 打印斐波那契数列

num = int(input("Please input the num: "))
a,b = (1,1)
for i in range(num):
   print(a,end=" ")
   a,b = b,a+b
