"""
添加类属性 实例属性
添加类方法 实例方法 静态方法
"""
import types

class Person:
    """这是一个用来创建人对象的类"""
    def __init__(self):
        pass


# 添加类属性name
Person.name = "person"
ming = Person()
print(ming.name)
# 添加实例属性
ming.age = 20
print(ming.age)


# 添加类方法
@classmethod
def class_method(cls):
    print("这是类方法啊")


# 定义静态方法
@staticmethod
def static_method():
    print("这是静态方法")


Person.clsmethod = class_method
Person.stamethod = static_method
Person.clsmethod()
Person.stamethod()


# 实例方法需要引入types模块
def shili(self):
    print("实例方法")

ming = Person()
ming.shili = types.MethodType(shili, ming)
ming.shili()
