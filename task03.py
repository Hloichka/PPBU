

name = input().strip()

if name == "":
    print("Ошибка: пустое имя.")
elif len(name) >= 12:
    print("Ошибка: слошком длинное имя.")
elif any(names.isdigit() for names in name):
    print("Ошибка: в имени цифры.")
else:
    print(f"Имя принято: {name}")

