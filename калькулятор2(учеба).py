# import os
#
# File = "calculations.txt"
#
from msilib.schema import File


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


# def save_result(ex, rt):###сохраняем результат в файл
#     with (open(File, "a", encoding='utf-8') as fi): ###Режим append — дозапись в конец сокращенно "а"
#         ####указывает кодировку файла (как превращать текст в байты)/ Без encoding Python использует системную кодировку
#         ####файл, записанный на Windows в cp1251, не откроется на Linux (там utf-8) — будут кракозябры
#         fi.write(f"Результат: {ex} = {rt}\n")


# def show_history():
#     print("История вычислений: ")
#     if not os.path.exists(File): ###проверяем существует ли файл (не понимаю зачем)
# ####От английского "path exists" — «путь существует».
#         print("История пуста. ")
#         return

    with open(File, "rt", encoding="utf-8") as fi: ###utf-8 что это? почему оно помогает читать файл?
        c = fi.read()
    if c:
        print(c, end="") ###зачем тут пробел end=""?
    else:
        print("История пуста. ")

#
# add = lambda x, y: x + y
# sub = lambda x, y: x - y
# mul = lambda x, y: x * y
# div = lambda x, y: "Число на ноль не делится." if y == 0 else x / y


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
       return "Деление запрещенно"
   except TypeError:
       return "Ошибка данных"

def log(result):
    try:
        with open("calculations.txt", "rt", encoding="utf-8") as fi:
            File.write(result)
    except Exception as e:
        print(f'Произошла ошибка: {e}')


with open(File, "rt", encoding="utf-8") as fi:
####меню управления
while True:
    print("Выберите операцию: ")
    print("1. Сложение ")
    print("2. Вычитание ")
    print("3. Умножение ")
    print("4. Деление ")
    # print("5. Просмотр истории вычислений ")
    # print("0. Выход ")