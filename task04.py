t = input()

if len(t) != 5 or t[2] != ":":
    print("Формат неверный")
else:
    for i in [0, 1, 3, 4]:
        if not t[i].isdigit():
            print("Формат неверный")
            break
    else:
        print("Формат верный")
