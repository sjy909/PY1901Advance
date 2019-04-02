from collections.abc import Iterator, Iterable


class ITER:
    def __init__(self, li):
        self.li = li

    def __iter__(self):
        pass

    def __next__(self):
        pass


i = ITER([1, 2, 3])
print(isinstance(i, Iterable))
print(isinstance(i, Iterator))
print(isinstance(ITER, Iterable))
