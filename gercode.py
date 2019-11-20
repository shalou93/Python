#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 生成指定位数的随机验证码

import string
import random

all_chr = (string.ascii_letters+string.digits)

def ger_code(code_len=4):
    """
    生成指定长度的验证码
    :param code_len: 验证码的长度(默认4个字符)
    :return: 由大小写英文字母和数字构成的随机验证码
    """
    code = "".join(random.sample(all_chr,code_len))
    return code

print(ger_code(4))

