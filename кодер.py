
import json

with open('dict.json', 'r', encoding='utf-8') as file:
    d = json.load(file)
while True:
    word = input('Введите слово для перевода: ')
    if word in d:
        print(f' {word} - {d[word]}')
    elif word == 'exit':
        break
    else:
        translate = input(f'Введите перевод слова "{word}": ')
        d[word] = translate

        with open('dict.json', 'w', encoding='utf-8') as file:
            json.dump(d, file, indent=4)

########
with open('text.txt', 'r', encoding='utf-8') as f:
    s = f.read()
    key = input('Введите ключ шифрования: ')
    secret = ''
    for c in s:
        code = ord(c) + int(key)
        symbol = chr(code)
        secret += symbol
print('Текст зашифрован!')

with open('code.txt', 'w', encoding='utf-8') as f:
    f.write(secret)
print('Файл "code.txt" для отправки сформирован.')
########


with open('code.txt', 'r', encoding='utf-8') as f:
    s = f.read()
    key = input('Введите ключ шифрования: ')
    unsecret = ''
    for c in s:
        code = ord(c) - int(key)
        symbol = chr(code)
        unsecret += symbol
print('Текст расшифрован!')

with open('decode.txt', 'w', encoding='utf-8') as f:
    f.write(unsecret)
print('Файл "decode.txt" для чтения сформирован.')
########


# file = open('text.txt', 'r', encoding='utf-8')
# # s = file.read()
# # s = file.readline()
# # print(s)
# sl = file.readlines()
# print(sl)
# file.close()

# for i in open('text.txt', 'r', encoding='utf-8'):
#     print(i.rstrip())

with open('text.txt', 'r', encoding='utf-8') as file:
    ls = file.read().title().split()

ls.sort()
print(ls)

with open('text1.txt', 'w', encoding='utf-8') as file:
    for n, f in enumerate(ls, 1):
        file.write(f'{n}. {f}\n')
########


