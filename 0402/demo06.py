"""
时间统计
"""
import time


def count_time(f):
    def ct():
        start = time.time()
        f()
        end = time.time()
        print(end-start)

    return ct


@count_time
def countlist():
    li = [x for x in range(100000)]
    index = 0
    while True:
        for x in li:
            # print(index)
            index += 1
            if x == 100000:
                print(index)
                print(11111111111111111111111111111111111111111)
                break


countlist()
