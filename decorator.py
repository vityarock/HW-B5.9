#!/usr/bin/env python3
def benchmark(func):
    """Функция(используется как декоратор) принимает на вход функцию, запускает её 10 раз и выводит среднее время выполнения"""
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
    """Функция выводит последовательность Фибоначчи для начальных чисел 0 и 1"""
    a = 0
    b = 1
    for __ in range(10000):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    fib()
