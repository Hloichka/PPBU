n = input('Введите число: ')
check = n.isdigit()
n = int(n)
if check:
    if n > 0:
    print('Число положительное')
    elif n < 0:
    print('Число отрицательное')
    else:
    print('Число ноль')
else:
    print('Вы ввели не число')
