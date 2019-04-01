"""
类属性方法
类属性方法 属于类 只占一分内存
实例方法：实例属性属于实例 没使用一个实例就生成一个内存
声明实例属性，实例方法，浪费内存，适当的选择声明类型属性和类方法节省内存
"""
"""
增加类的方法 属性
实例的方法 属性
"""


class LOVE:
    def __init__(self, _hp):
        self.hp = _hp


# 实例方法
def p(self):
    print(self.hp)


LOVE.show_hp = p

p(LOVE(1))


class S:
    def __init__(self):
        pass


S.name = "w"
q = S()
print(q.name)
