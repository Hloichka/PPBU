import random

def li(file_name):
    try:
        with open(file_name, encoding='utf-8') as f:
            con = f.readlines()

        if not con:
            print('Файл пустой ')
        else:
            print(random.choice(con)) #что за choice?
    except FileNotFoundError:
        print('Файл не найден')
    except Exception as e:
        print(f'Произошла ошибка: {e}')

li('подсказка.txt')
