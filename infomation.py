# -*- coding:utf-8 -*-
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

def print_info():
    with open('E:\Desktop\Py\info.txt','r+') as f:
        data = f.read().split()
        p_data = data[i].split(',')
        while True:
            for x,p in enumerate(p_data):
                print("%s %s" %(x,p))
            user_action = input("请输入您要修改的字段值:")



def change_info():
    pass

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
    show_info()
    user_choice = int(input("请选择您的操作:"))
    if user_choice == 1:
        change_info()
    elif user_choice == 2:
        print_info()
    elif user_choice == 3:
        change_password()
    else:
        print("请输入正确的操作:")
    break
