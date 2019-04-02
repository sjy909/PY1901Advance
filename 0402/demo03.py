"""
迭代器
"""
from collections.abc import Iterable, Iterator
one = [1, 2, 3]
two = dict()
print(isinstance(one, Iterable))
print(isinstance(two, Iterable))
print(isinstance(one, Iterator))
print(isinstance(two, Iterator))

list()

# iter()函数
one = iter(one)
print(next(one))
