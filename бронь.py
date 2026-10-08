####проект по бронированию
####список мест в виде списка кортежей
####[["Б1", "свободно"], ["Б2", "свободно"]]
####метод bint привязка к кнопки или мышки - типо ввести и энтер->запускается процесс
from tkinter import *
from tkinter import messagebox as mb


def book_seat(event=None):
    s = seat_entry.get()
    try:
        if seat[s] == "Свободно ":
            seat[s] = 'Забронированно'
            update_canvas()
            mb.showinfo('Выполнено', f'Место {s} успешно забронировано.')
        else:
            mb.showinfo('Ошибка', f'Место {s} недоступно.')
    except KeyError:
        mb.showinfo('Ошибка', f'Место {s} не существует.')


def update_canvas():
    canvas.delete('all')
    for i, (seats, status) in enumerate(seat.items()):
        x = i * 40 + 5
        y = 20
        color_seat = "green" if status == "Свободно " else "red"
        canvas.create_rectangle(x, y, x+30, y+30, fill=color_seat)
        canvas.create_text(x+20, y+20, text=seats)


def cancel_booking(event=None):
    s = cancel_seat_entry.get()
    try:
        if seat[s] == "Забронированно":
            seat[s] = 'Свободно '
            update_canvas()
            mb.showinfo('Выполнено', f'Бронь {s} отменена.')
        else:
            mb.showinfo('Ошибка', f'Место {s} недоступно.')
    except KeyError:
        mb.showinfo('Ошибка', f'Место {s} не существует.')


window = Tk()
window.title('')
window.geometry('400x300')


canvas = Canvas(window, width=400, height=60, background='light gray')
canvas.pack(pady=10)

seat = {f'Б{x}':"Свободно " for x in range(1, 11)} ###отображать в столб свободные места
update_canvas() ###обновляет холст


seat_entry = Entry()
seat_entry.pack(pady=10)
seat_entry.focus()
seat_entry.bind('<Return>', book_seat)
Button(text='Забронировать место', command=book_seat).pack(pady=10)


cancel_seat_entry = Entry()
cancel_seat_entry.pack(pady=10)
cancel_seat_entry.focus()
cancel_seat_entry.bind('<Return>', cancel_booking)
Button(text='Отменить бронь', command=cancel_booking).pack(pady=10)



window.mainloop()
