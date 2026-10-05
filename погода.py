
def write(f, content):
    try:
        with open(f, 'a') as f:
            f.write(data + '\n') ###(data) как данные
            print("Данные сохранены")
    except IOError:
        print("Ошибка при записи ")


print("Создатель дневника погоды")
while True:
    date = input("Какая дата? Или хотите выйти?" + '\n') ###Дата как date
    if date == 'Выход':
        break
    t = input('Введите температуру: ')
    d = input('Есть осадки? ')
    data = f"{date}: Температура:\n {t}Осадки\n {d} "  ###почему не переносит курсор?

    write("log.txt", data)




