#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time

def main():
    content = '湖北武汉欢迎您......'
    while True:
        # 清理屏幕上的输出
        os.system('clear')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(1)
        content = content[1:] + content[0]

if __name__ == '__main__':
    main()
