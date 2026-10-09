from tkinter import *

pen_color = "black"


def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x, y, x + 5, y + 5, fill=pen_color, outline=pen_color)


def change_color(event):
    global pen_color
    pen_color = "red"

window = Tk()
window.title('графический редактор')

canvas = Canvas(width=600, height=400, bg=pen_color)
canvas.pack()
canvas.bind("<B1-Motion>", draw)


colors = ["red", "green", "blue", "yellow", "cyan", "magenta"]
for color in colors:
    lbl = Label(bg=color, width=8, height=2)
    lbl.pack(side=LEFT)
    lbl.bind("<B1-Motion>", lambda e, c=color: globals().update(pen_color=c))




window.mainloop()
