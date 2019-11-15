# -*- coding:utf-8 -*-
# 求水仙花数
# 说明：水仙花数也被称为超完全数字不变数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$

for i in range(100,1000):
    s_1 = i % 10
    s_2 = i // 10 % 10
    s_3 = i //  100


    if i == s_1 ** 3 + s_2 ** 3 + s_3 ** 3:
        print(i)
