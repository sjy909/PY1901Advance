"""
实例方法：需要第一个参数为self
类方法：需要第一个参数为cls，并且需要使用@classmethod声明
静态方法：需要使用@staticmethod声明
"""
class Good():
    """
    这是一个类
    """
    def __init__(self, name):
        self.name = name

    def qqq(self):
        print(self.name)
        print("实例方法")

    @classmethod
    def ppp(cls):
        print(cls.__dir__)
        print("类方法")

    @staticmethod
    def fff():
        print("静态方法")

if __name__== "__main__":
    ds = Good(name="qw")

    ds.fff()
    ds.ppp()
    ds.qqq()

    Good.fff()
    Good.ppp()

    
