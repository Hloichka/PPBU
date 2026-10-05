####проект по бронированию
####список мест в виде списка кортежей
####[["Б1", "свободно"], ["Б2", "свободно"]]
from tkinter import *
from tkinter import messagebox as mb


def book_seat(seat):
    s = seat_entry.get
    try:
        if seat[s] == "Свободно ":
            seat[s] = 'Забронированно'
            mb.showinfo('Выполнено', f'Место {s} успешно забронировано.')
        else:
            mb.showinfo('Ошибка' f'Место {s} недоступно.')
    except KeyError:
        mb.showinfo('Ошибка' f'Место {s} не существует.')


def update_canvas():
    canvas.delete('all')
    for i, (seats, status) in enumerate(seat.items()):
        x = i * 40 + 20
        y = 20
        color_seat = "green" if status == "Свободно" else "red"
        canvas.create_rectangle(x, y, x+30, y+30, fill=color_seat)
        canvas.create_text(x+20, y+20, text=seats)



window = Tk()
window.title('')
window.geometry('400x200')


canvas = Canvas(window, width=400, height=200, background='black')
canvas.pack(pady=10)

seat = {f'Б{x}':"Свободно " for x in range(1, 11)} ###отображать в столб свободные места
update_canvas() ###обновляет холст


seat_entry = Entry()
seat_entry.pack(pady=10)

Button(text='Забронировать место', command=book_seat).pack(pady=10)




window.mainloop()
