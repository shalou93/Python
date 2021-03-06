#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 个人信息查询、修改

import os

login_count = 0
run_flag = True
# _username = 'zhangsan'
# _password = 'pass1'

def show_info():
    info = """
1.修改个人信息
2.打印个人信息
3.修改密码
    """
    print(info)

def open_file():
    with open('E:\Desktop\Py\info.txt','r+') as f:
        data = f.read().split()
        global p_data
        p_data = data[i].split(',')

def print_info():
        open_file()
        print(p_data)


def print_column():
        global user_column
        user_column = str(input('请输入修改后的值:'))


def change_info():
    open_file()
    for x, p in enumerate(p_data):
        print("%s %s" % (x, p))
    while True:
        user_action = int(input("请输入您要修改的字段值:"))
        if user_action == 'q':
            print('已退出登录!')
        else:
            print_column()
            p_data[user_action] = user_column

            write_info()
        break

def write_info():
    if i == 0:
        data[i] = ','.join(p_data) + '\n'
    else:
        data[i] = '\n' + ','.join(p_data)
    with open('E:\Desktop\Py\info.txt', 'w+') as f:
        f.writelines(data)



def change_passwd():
    open_file()
    print_column()
    p_data[1] = user_column
    write_info()


while login_count < 3 and run_flag == True:
    user_username = str(input("Username:"))
    user_password = str(input("Password:"))

    login_count += 1

    with open('E:\Desktop\Py\info.txt', 'r+') as f:
        data = f.read().split()
        for i in range(len(data)):
            if user_username == data[i].split(',')[0] and user_password == data[i].split(',')[1]:
                print("You are login.")
                run_flag = False
                break

while run_flag == False:
    try:
        show_info()
        user_choice = input("请选择您的操作:")
        if user_choice == '1':
            change_info()
        elif user_choice == '2':
            print_info()
        elif user_choice == '3':
            change_passwd()
        elif user_choice == 'q':
            break
    except ValueError:
        print("请输入正确的操作:")
