#!/usr/bin/env python
# 打印N个数的平均数

count = 0
sum = 0
while True:
	num = input("Please input the num: ")
	if num == 'quit':
		break
	count += 1
	sum += int(num)
	avg = sum / count 
	print(avg)
