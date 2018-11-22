#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random
number = random.randint(1,101)
user_input = ""
guess = 0
while user_input != number:
    user_input = str(input("Please input a number: "))
    guess += 1
    if not user_input.isdigit():
        pass
    elif not 0 <= int(user_input) <= 100:
        pass
    else:
        if int(user_input) > number:
            print("Your number is too large.")
        elif int(user_input) < number:
            print("Your number is too small.")
        else:
            break
print("only %d ,that congratulations to you." %(guess))
