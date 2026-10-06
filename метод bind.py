from tkinter import Tk


def key_press(event):
    print(f'Вы нажали клавишу: {event.char}')

def mouse_click(event):
    print(f'Клик мыши на: {event.x}, {event.y}')

def mouse_move(event):
    print(f'Курсор на позиции: {event.x}, {event.y}')

    

window = Tk()
window.bind("<Key>", key_press)
window.bind("<Button-1>", mouse_click)
window.bind("<Motion>", mouse_move)
window.mainloop()