from tkinter import *
from tkinter import messagebox as mb


def add_item():  ###функция для кнобки ввода
    if s.get() == '0':
        l1.insert(END, e.get())  ### действие ее при вводе (в конец insert) (END-считаем в конец -> e.get из этой переменной
        e.delete(0, END)   ### считали и сразу очистили с 0 до конца end
    else:
        if validate_phone():
            l2.insert(END, e.get())
            e.delete(0, END)
            # mb.showinfo("Добавление номера", "Номер добавлен",)

def del_item():  ###функция для кнобки удаления
    if l1.curselection():
        l1.delete(ANCHOR)  ### действие для кнопки "удаленя" удаления ввода
    elif l2.curselection():
        l2.delete(ANCHOR)
    else:
        print("Ничего не выбрано")


def save():  ###сохраняем в файл
    try:
        with open('phones.txt', 'w') as f:
            for i in range (l1.size()):
                f.write(f'{l1.get(i)} : {l2.get(i)}\n')
        mb.showinfo("Сохранено", "Контакт добавлен.")
    except Exception as e:
        mb.showerror("Ошибка: {e}")



def load():
    try:
        with open('phones.txt', 'r') as f:
            l1.delete(0, END)
            l2.delete(0, END)
            for line in f:
                name, _, phone = line.partition(" : ") ###как разделить - партишен
                l1.insert(END, name)  ###insert записывать
                l2.insert(END, phone)
        mb.showinfo("Загрузка", "Контакт загружен")
    except Exception as e:
        mb.showerror("Ошибка: {e}")
    except FileNotFoundError:
        mb.showerror("Файл не найден")


def validate_phone():
    number = e.get()
    if len(number) == 11 and number.isdigit() and number.startswith('8'):
        # mb.showinfo("Проверка", "Номер проверен")
        return True
    else:
        mb.showerror("Ошибка", "Неверный ввод номера")
        return False


window = Tk()
s = StringVar() ### переменная будет возращать строчку
f1 = Frame()
f1.pack(side=LEFT)
m1 = Label(f1, text="Имя")
m1.pack()
l1 = Listbox(f1)
l1.pack()


f2 = Frame()
f2.pack(side=LEFT)
m2 = Label(f2, text="Номер")
m2.pack() ###под меткой будет список
l2 = Listbox(f2)
l2.pack() ###список


# l = Listbox()
# l.pack(side=LEFT) ###разместить - пак-сайдлефт с лево
f3 = Frame() ###поле где ввод отображается
f3.pack(side=LEFT)
r1 = Radiobutton(f3, text="Имя", value=0, variable=s)
r1.pack()
r2 = Radiobutton(f3, text="Номер", value=1, variable=s)
r2.pack()


e= Entry(f3) ###что поле ввода
e.pack()
b1 = Button(f3, text="Добавить", command=add_item) ###кнобка добавить
b1.pack()
b2 = Button(f3, text="Удалить", command=del_item) ###кнобка удалить
b2.pack()
b3 = Button(f3, text="Сохранить", command=save) ###кнобка сохранения
b3.pack()
b4 = Button(f3, text="Загрузить", command=load) ###кнобка загрузить
b4.pack()



window.mainloop()
s = StringVar(value=0)