def fun(a, b, num):
    a = a
    b = b
    yield a
    yield b
    count = 0
    while count < num:
        a, b = b, a+b
        yield b
        count += 1
        print(b)


reslut = fun(1, 2, 10)
for r in reslut:
    print(r)
