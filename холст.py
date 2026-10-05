from tkinter import *


def draw_circle():
    color = color_var.get()
    canvas.create_oval(50, 50, 150, 150, outline=color, fill=color) ###кардинаты и размер фигуры


def draw_triangle():
    color = color_var.get()
    canvas.create_polygon(50, 150, 100, 50, 150, 100, outline=color, fill=color) ###кардинаты и размер фигуры


def draw_square():
    color = color_var.get()
    canvas.create_rectangle(50, 50, 150, 150, outline=color, fill=color) ###кардинаты и размер фигуры

def clear_canvas():
    canvas.delete("all")


window = Tk()
window.title("Рисуем фигуру")
window.geometry("400x550")

color_var = StringVar(value="yellow")

canvas = Canvas(window, width=350, height=200, )###вывод кнопки-ее размер
canvas.pack()
circle_button = Button(text="Окружность", command=draw_circle)###текст на кнопки и вывод ее(draw-рисовать)
circle_button.pack(pady=10)

triangle_button = Button(text="Треугольник", command=draw_triangle)###текст на кнопки и вывод ее(draw-рисовать)
triangle_button.pack(pady=10)

square_button = Button(text="Квадрат", command=draw_square)###текст на кнопки и вывод ее(draw-рисовать)
square_button.pack(pady=10)

cler_button = Button(text="Очистить", command=clear_canvas, padx=40)
cler_button.pack(pady=10)

blue_radio = Radiobutton(text="Голубой", variable=color_var, value="blue",)
blue_radio.pack(pady=10)

red_radio = Radiobutton(text="Красный", variable=color_var, value="red",)
red_radio.pack(pady=10)

green_radio = Radiobutton(text="Зеленый", variable=color_var, value="green",)
green_radio.pack(pady=10)



window.mainloop()

