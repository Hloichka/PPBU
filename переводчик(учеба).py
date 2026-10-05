from idlelib.editor import keynames


def translate(file):
    dictonary = {}
    try:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                key, value = line.split()
                dictonary[key] = value
            print(dictonary)
    except FileNotFoundError:
        print('Файл не найден')
    except ValueError:
        print('Ошибка значения')
    return dictonary

dict = translate("wordline.txt")
while True:
    word = input(f'Введите слово:{""}')
    if word in dict:
        print(f"Перевод {word}: {dict[word]}")
    else:
        print('Слово не найдено')
    exit = input("Хотите выйти?")
        if word.lower() == "да":
            break
