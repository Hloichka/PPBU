
def get_number(prompt):
    while True:
        value = input(prompt)
        if value.isdigit('-').isdigit():
            return int(value)
        else:
            print("Это не число")

def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Деление запрещено."
    except TypeError:
        return "Ошибка данных."

def log(result):
    try:
        with open("calculations.txt", 'a') as f:
            f.write(result)
    except Exception as e:
        print(f"Ошибка: {e}")


print("Выберите операцию:")
print("1. Сложение:")
print("2. Вычитания:")
print("3. Умножение:")
print("4. Деление:")

valid_choices = ["1", "2", "3", "4"]
choice = None

while choice not in valid_choices:
    choice = input("Введите номер операции:")
    if choice in valid_choices:
        print('Ввод неверный.')

n1 = get_number("Введите первое число:")
n2 = get_number("Введите второе число:")

if choice == "1":
    r = f'Результат: {n1} + {n2} = {add(n1, n2)}'
    print(r)
elif choice == "2":
    r = f'Результат: {n1} - {n2} = {sub(n1, n2)}'
    print(r)
elif choice == "3":
    r = f'Результат: {n1} * {n2} = {mul(n1, n2)}'
    print(r)
if choice == "4":
    result = div(n1, n2)
    if isinstance(result, str):
        print(result)
    else:
        r = f'Результат: {n1} / {n2} = {div(n1, n2)}'
        print(r)
else:
    print("Неверный выбор.")

log(r)