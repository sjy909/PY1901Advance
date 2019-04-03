"""
生成器
"""
# 生成一个列表
L = [x for x in range(10)]
# 打印一下列表的内容和数据
print(L, type(L))
# 生成生成器
G = (x for x in range(10))
# 打印生成器内容
print(G, type(G))
# 需要用next方法获取
print(G.__next__())
print(next(G))
# for 循环获取
for x in G:
    print(x)


# 使用yield得到函数生成器，内部储存斐波拉契数列
def red(num):
    a = 0
    b = 1
    # 计数参数默认值为0
    index = 0
    yield a
    yield b
    while index < num:
        a, b = b, a+b
        # 返回b
        yield b
        # 计数加一
        index +=1


for x in red(10):
    print(x)


# 有return  yield的函数如何返回值为return中的内容
def test():
    yield 1
    return "hello"


result = test()
print(next(result))
print(next(result))

