#!/usr/bin/env python3
def benchmark(func):
    import time  
    def wrapper():
        avg_time = 0
        for i in range(10):
            start = time.time()
            func()
            end = time.time()
            avg_time += end - start
        print('[*] Среднее время выполнения: {:.4f} секунд.'.format(avg_time/10))
    return wrapper


@benchmark
def fib():
    a = 0
    b = 1
    for __ in range(10000):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    fib()
