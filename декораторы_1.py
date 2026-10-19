@@ -1,4 +1,15 @@
import time
import random
from math import sqrt


def in_out(func):
    def wrapper(*args, **kwargs):
        print(f'на входе функции {func.__name__} - {args}\n {kwargs}')
        result = func(*args, **kwargs)
        print(f'На выходе функции {func.__name__} - {result}')
        return result
    return wrapper


def time_run(func):
@@ -18,6 +29,7 @@ def wrapper():
        print('AFTER')
    return wrapper


@decor
def proba():
    print('PROBA')
@@ -27,8 +39,14 @@ def etalon(n, m, z):
    print('ETALON')
    time.sleep(n + m + z)

@in_out
def summatr(n, m):
    return n + m


if __name__ == '__main__':

    # proba()
    etalon(3, 1, 1 )
    # etalon(3, 1, 1 )
    res = sqrt(summatr(random.randint(1,1000), random.randint(1,1000)) /.33)
    print(res)