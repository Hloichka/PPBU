import time

def time_run():
    def wrapper(*args, **kwargs):
    start = time.time()
    func(*args, **kwargs)
    end = time.time()
    duration = round(end - start, 2)
    print(f'Функция {func.__name__} работае {duration} сек.')
    return wrapper()

def decor(func):
    def wrapper():
        print("BEFPRE")
        func()
        print("AFTER")
    return wrapper

@decor
def pandora():
    print("PROBA")

@time_run
def etalon(n, m, z):
    print('ETALON')
    time.sleep(n + m + z)


if __name__ == '__main__':

    etalon(3, 1, 1)