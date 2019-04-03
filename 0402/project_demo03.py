"""
添加权限管理
"""


def checkout(f):
    def check():
        if input("请输入您的姓名") == "sjy":
            f()
        else:
            print("没有权限")
    return check


@checkout
def H():
    print("通过权限管理的显示界面")

H()



