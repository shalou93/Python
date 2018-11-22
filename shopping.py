# -*- coding:utf-8 -*-

products = [['iphone8',6888],['MacPro',14800],['小米6',2499],['Coffee',31],['Book',80],['Nike Shoes',799]]
shopping_cart = []
run_flag = True
while run_flag:
    print("------------商品列表------------")
    for index,p in enumerate(products):
        print("%s.%s %s" %(index,p[0],p[1]) )
    choice = input("请输入想购买的商品编号: ")
    if choice.isdigit():
        choice = int(choice)
        if 0 <= choice < len(products):
            shopping_cart.append(products[choice])
            print("Added product %s into shopping cart."  % (products[choice]) )
    elif choice == 'q':
        if len(shopping_cart) > 0:
            print("你购买的商品列表如下: %s" %(shopping_cart))
        run_flag = False
    else :
        print("请输入正确的商品编号.")
