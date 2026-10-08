from tkinter import *
# import random
import time
from tkinter import messagebox as mb


def load_phrase():
    try:
        with open("phrase.txt", "r") as f:
            return f.read().strip()   ####strip удаляет пробелы или лишние знаки в использующем файле
    except FileNotFoundError:
        mb.showerror("Ошибка!", "Файл не найден")
        return "quickbrownfxetypasdghjlzvm"


def start():
    global i, t
    i = 0
    t = time.time()
    label.config(text=phrase[i])
    window.bind("<Key>", check) ###функция check помогает отобразить какую клавишу мы нажали


def check(event):
    global i
    if event.char == phrase[i]:
        i += 1
        if i == len(phrase):
            finish()
        else:
            label.config(text=phrase[i])
    else:
        label.config(text=f"Ошибка! Ожидалась буква {phrase[i]}, \n Нажми любую клавишу для продолжения")
        window.bind("<Key>", cont)


def finish():
    elapsed = time.time() - t
    time_allowed = len(phrase)
    if elapsed <= time_allowed:
        res = f"Поздравляем! Ваше время {elapsed:.1f} сек. \n Нужно не больше {time_allowed} сек."
        window.unbind("<Key>")
    else:
        res = f"Вы потратили {elapsed:.1f} сек., \n Нужно не больше {time_allowed} сек."
        window.unbind("<Key>")
    mb.showinfo("Результат", res)
    if mb.askyesno("Повторить?", "Хотите повторить еще раз?"):
       start()
    else:
        window.destroy()


def cont(event):
    global i
    label.config(text=phrase[i])
    window.bind("<Key>", check)
    return

"""Создание окна"""
i = 0
t = 0
phrase = load_phrase()

window = Tk()
window.title("Тренажер")
window.geometry("800x100")

"""создание метки"""
label = Label(font=('Helvetica', 24))
label.pack()

"""Вызов окна"""
start()
window.mainloop()
