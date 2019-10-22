#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 打印闪电

num = int(input("Please input the num: "))

for i in range(-num,num+1):
    s = ""
    if i < 0:
        i = -i
        #print(' '*i + '*'*((num+1-i) if i != 0 else 2*num+1))  # 三目运算符
        print(' '*i + '*'*((num+1-i))) 
    elif i ==0:
        print('*'*(2*num+1))
    else:
        i = i
        print(' '*num + '*'*(num+1-i))
