#！/usr/bin/env python
# 将整数反转输出

num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)


print(str(num)[::-1])
