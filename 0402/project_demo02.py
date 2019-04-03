"""
判断迭代
"""
from collections.abc import Iterable, Iterator
# 创建列表
L  = [1, 2, 3, 4]
# 创建字典
D = {"a":1, "b":2}
# 创建字符串
S = "string"
# 创建整型
I = 10
# 判断是否迭代  是否为迭代器
print(isinstance(L, Iterable))
print(isinstance(L, Iterator))
print(isinstance(D, Iterable))
print(isinstance(D, Iterator))
print(isinstance(S, Iterable))
print(isinstance(S, Iterator))
print(isinstance(I, Iterable))
print(isinstance(I, Iterator))