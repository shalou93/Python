#!/usr/bin/env python
# 依次打印一个不超过5位数的万位、千位、百位、十位、个位
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
for i in range(count,0,-1):
    c = num // 10**(i-1)
    print(c)
    num -= c*(10 ** (i-1))
