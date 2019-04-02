"""
装饰器
"""


# 定义一个装饰器
def check_user(fun):
    def check():
        name = input("请输入您的账户名称")
        if name == 'sjy':
            fun()
        else:
            print("输入账户没有权限")

    return check


@check_user
def show_list():
    for i in range(10):
        print(i)


show_list()
