def f():
    yield 1
    return "hello"


print(next(f()))
f = f()
try:
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
except StopIteration as e:
    print(e)
