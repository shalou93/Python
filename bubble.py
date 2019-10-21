#!/usr/bin/env python

l = [1,9,8,5,6,7,4,3,2]

length = len(l)
count = 0

for i in range(length):
	flag = True
	for j in range(length-i-1):
		count += 1
		if l[j] > l[j+1]:
			tmp = l[j+1]
			l[j+1] = l[j]
			l[j] = tmp
			flag = False		
	if flag:
		break

print(l)
print(count)
