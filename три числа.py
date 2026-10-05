import os
import tkinter as tk
import math
from tkinter import *


windcan = tk.Tk()
windcan.title("Калькулятор")
windcan.geometry("400x350")

Label(windcan, text="Введите три числа и нажмите на нужную вам функцию").pack(pady=5)


def add_num():
    try:
        x = int(number1.get())
        y = int(number2.get())
        z = int(number3.get())
        result = x + y + z
        result_num.config(text=f'Результат: {x} + {y} + {z} = {result}')

    except ValueError:
        result_num.config(text=f'Ошибка: введите число')
    except Exception as err:
        pass


def mul_num():
    try:
        x = int(number1.get())
        y = int(number2.get())
        z = int(number3.get())
        result = x * y * z
        result_num.config(text=f'Результат: {x} * {y} * {z} = {result}')

    except ValueError:
        result_num.config(text=f'Ошибка: введите число')
    except Exception as err:
        pass


add = lambda x, y, z: x + y + z
mul = lambda x, y, z: x * y * z


number1 = Entry(windcan, width=20)
number1.config(font=("Calibri", 12), justify="center")
number1.pack(pady=5) ###менеждер разметки (сетка)

number2 = Entry(windcan, width=20)
number2.config(font=("Calibri", 12), justify="center")
number2.pack(pady=5) ###менеждер разметки (сетка)

number3 = Entry(windcan, width=20)
number3.config(font=("Calibri", 12), justify="center")
number3.pack(pady=5) ###менеждер разметки (сетка)

result_num = Label(windcan, width=20, bg='light grey')
result_num.config(font=("Calibri", 12), justify="center")
result_num.pack(pady=5) ###менеждер разметки (сетка)
# result_num.config(text=f"{result}")

add_button = Button(text="Сложить три числа", command=add_num)
add_button.pack(pady=5)

mul_button = Button(text="Умножить три числа", command=mul_num)
mul_button.pack(pady=5)



windcan.mainloop()