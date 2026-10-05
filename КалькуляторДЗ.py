import os

File = "calculations.txt"


def get_number(prompt): ###для того чтобы в переменной было только цисла
    while True: ###для бесконечного цикла (крутиться бесконечно, пока не введется число и с числом запуститься операция ниже)
        value = input(prompt) ###это английское слово «значение». В Python это не команда и не ключевое слово, а просто
        ### имя переменной, которое часто используют программисты.
        ### это английское слово «подсказка», «приглашение». В Python это не команда и не ключевое слово, а просто имя
        ### переменной или параметр, который часто используют.
        ###От английского "prompt" — «подсказка», «приглашение к вводу».
        if value.lstrip("-").isdigit():###это метод строки, который проверяет, состоит ли строка только из цифр
            ###lstrip() дает нам удалить пробелы перед строкой, однако если мы напишем ("-") то удаляется тот знак что в ковычках.
            return int(value)###возвращает значение из функции и немедленно завершает её выполнение.
        else:
            print("Это не число!")


def save_result(ex, rt):###сохраняем результат в файл
    with (open(File, "a", encoding='utf-8') as fi): ###Режим append — дозапись в конец сокращенно "а"
        ####указывает кодировку файла (как превращать текст в байты)/ Без encoding Python использует системную кодировку
        ####файл, записанный на Windows в cp1251, не откроется на Linux (там utf-8) — будут кракозябры
        fi.write(f"Результат: {ex} = {rt}\n")


def show_history():
    print("История вычислений: ")
    if not os.path.exists(File): ###проверяем существует ли файл (не понимаю зачем)
####От английского "path exists" — «путь существует».
        print("История пуста. ")
        return

    with open(File, "rt", encoding="utf-8") as fi: ###utf-8 что это? почему оно помогает читать файл?
        c = fi.read()
    if c:
        print(c, end="") ###зачем тут пробел end=""?
    else:
        print("История пуста. ")


add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: "Число на ноль не делится." if y == 0 else x / y


###def add(x, y):
###   return x + y
###def sub(x, y):
###    return x - y
###def mul(x, y):
###    return x * y
###def div(x, y):
###    if y == 0:
###        return "Ошибка. Деление на 0"
###    else:
###        return x / y
###меню управления
while True:
    print("Выберите операцию: ")
    print("1. Сложение ")
    print("2. Вычитание ")
    print("3. Умножение ")
    print("4. Деление ")
    print("5. Просмотр истории вычислений ")
    print("0. Выход ")


    valid_choices = ["1", "2", "3", "4", "5", "0"]
    choice = None ###none это ничего(пусто)


    while choice not in valid_choices:
        choice = input ("Введите номер операции: ")
        if choice not in valid_choices:
            print("Вы ввели не верный математический способ. ")

    if choice == "0":
        print("Выход")
        break

    elif choice == "5":
        show_history()
    else:
        n1 = get_number("Введите первое число: ")
        n2 = get_number("Введите второе число: ")
        if choice == "1": ###что дает чойс???-что за переменная?
            rt = add(n1, n2)
            ex = f"{n1} + {n2}"
            print(f"Результат {ex} = {rt}")
            save_result(ex, rt)
        elif choice == "2":
            rt = sub(n1, n2)
            ex = f"{n1} - {n2}"
            print(f"Результат {ex} = {rt}")
            save_result(ex, rt)
        elif choice == "3":
            rt = mul(n1, n2)
            ex = f"{n1} * {n2}"
            print(f"Результат {ex} = {rt}")
            save_result(ex, rt)
        elif choice == "4":
            rt = div(n1, n2)
            if isinstance(rt, str): ###команда возвращает истина или ложь, это в случае деления на 0
                print(rt)
            else:
                ex = f"{n1} / {n2}"
                print(f"Результат: {ex} = {rt:.1f}") ###чтобы сократить знаки после запятой(:.1f)
                save_result(ex, f"{rt:.1f}")
        else:
            print("Неверный выбор операции: ")
