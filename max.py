#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 返回传入的列表中最大和第二大的元素的值

def l_max(para):
    m1 = max(para)
    para.remove(m1)
    m2 = max(para)
    return m1,m2

print(l_max([1,2,3,4,5]))
