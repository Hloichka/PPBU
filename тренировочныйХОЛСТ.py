import tkinter as tk


def draw_shapes():
    canvas.create_rectangle(100, 100, 150, 150, fill="red")
    canvas.create_oval(50, 50, 100, 100, fill="orange")
    canvas.create_text(150, 25, text="Пример холста")
window = tk.Tk()
canvas = tk.Canvas(window, width=600, height=800) #### создаем холст
canvas.pack()
draw_shapes() ####Рисуем фигуры на холсте





window.mainloop()



