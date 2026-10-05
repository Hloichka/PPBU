contacs = {}

def input_contact():
    name = input("введите имя: ") ###две разные переменные name с одним именем
    phone = input("введите номер сотового телефона: ")
    if len(phone) == 11 and phone.isdigit() and phone.startswith("8"):
        contacs[name] = phone
        print("контакт добавлен")
        print(contacs)
    else:
        print("неверный ввод")
def find_contact():
    name = input("введите имя: ")###две разные переменные name с одним именем
    print(contacs.get(name, "контакт не найден" )) ### .get функция сразу ищет имя и если его нет указывает, что его нет. вместе if-else
    # if name in contacs:
    #     print(name)
    # else:
    #     print("контакт не найден")

def del_contact():
    name = input("выберите контакт: ")
    try:
        del contacs[name]
        print("контакт удален")
    except KeyError:
        print("контакт не найден")


while True: ###посторяет вывод пока пользователь не выберет нужную функцию
    do = input ("выберите действие: ")
    if do == "1":
        input_contact()
    elif do == "2":
        find_contact()
    elif do == "3":
        del_contact()
    elif do == "4":
        break ### если 4 то просто вылетаем из цикла while (выходим)
    else:
        print("неверный ввод")







