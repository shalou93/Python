#!/usr/bin/env python
# 求n阶乘之和

n = int(input("Please input the num: "))
sum = 0
num = 1
for i in range(1,n+1):
    num *= i
    sum += num
print(sum)
