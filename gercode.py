#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 生成指定位数的随机验证码


import string
import random

all_par = (string.ascii_letters+string.digits)

def ger_code(len=4):
    code = "".join(random.sample(all_par,len))
    return code

print(ger_code(4))
