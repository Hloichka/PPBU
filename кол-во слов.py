def count(file_name):
    try:
        with open(file_name, encoding='UTF-8') as f:
            content = f.read()
            words = content.split() #делим на отдельные слова
            return len(words)
    except FileNotFoundError:
        print('Файл не найден')
    except Exception as e:
        print(f'Произошла ошибка: {e}')
words1 = count('БасняДураков.txt') ###другая переменная
print(f'кол-во слов в файде: {words1}')
