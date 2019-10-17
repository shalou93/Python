#!/usr/bin/env python
# 依次打印一个不超过5位数的个位，十位，百位，千位，万位
num = int(input("Please input the num: "))

if num >= 100:
    if num >= 10000:
        print("5位数")
        count = 5
    elif num >= 1000:
        print("4位数")
        count = 4
    else:
        print("3位数")
        count = 3
else:
    if num >= 10:
        print("2位数")
        count = 2
    else:
        print("1位数")
        count = 1
for i in range(1,count+1):
    c = num // 10
    print(num - 10*c )
    num = c
