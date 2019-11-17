#!/usr/bin/env python
# 求10000以内的完美数
#完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身，例如 28 = 1 + 2 + 4 + 7 + 14
from math import sqrt,pow

for i in range(1,10000):
    result = 0
    for j in range(1,int(sqrt(i))+1):
        if i % j == 0:
            result += j
            if j>1 and i != pow(j,2):
                result += i // j
    if result  == i:
       print(i)
