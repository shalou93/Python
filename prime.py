#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 打印100以内的所有质数

l = []
for i in range(2,100):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        l.append(i) 
print(l)