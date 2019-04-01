"""
类属性 实例属性
类方法 静态方法 实例方法
"""


# 首先定义一个类
class Person:
    """这是一个用来创建人对象的类"""
    head = 1

    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age

    def exaple(self):
        print(self.name, "这是实例方法")

    @classmethod
    def exaple2(cls):
        print("这是类的方法")

    @staticmethod
    def exaple3():
        print("这是静态方法")


# head 为类属性 name 和age 为实例属性
if __name__ == "__main__":
    xiao_ming = Person("xioa_ming", 10)
    print(xiao_ming.name, xiao_ming.age, Person.head)
    xiao_ming.exaple()
    xiao_ming.exaple2()
    xiao_ming.exaple3()
    Person.exaple2()
    Person.exaple3()
