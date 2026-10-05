from tkinter import *
import tkinter.messagebox as mb   ####высплывающие окна
import time
import pygame as pg  ###для того чтоб читало mp3

pg.mixer.init()
pg.mixer.music.load('Sound_01036.mp3')




def tick():
    global time_alarm
    current_time = time.strftime('%H:%M')
    if (time_alarm == current_time or  ####сравнивает с устанавливаемым временем будильника(чтобы сработал звонок)
            time_alarm == time.strftime('%H:%M') or
            time_alarm == time.strftime('%H')):
        time_alarm = '' ###это для того чтоб звук постоянно играл до нашего выкл, чтобы будильник не запускался каждую секунду.
        pg.mixer.music.play()

    skreen_time.after(1000, tick)
    skreen_time.config(text=current_time)


def on_click():
    global time_alarm
    time_alarm = entry_time.get().strip()

    mb.showinfo('Включение',
                f'Будильник установлен на {time_alarm}')


def off_click():
    global time_alarm
    time_alarm = ''
    entry_time.delete(0, END)
    pg.mixer.music.stop()
    mb.showwarning('Выключение', f'Будильник выключен')



'''''делим сверху функции а снизу лицевая часть'''
time_alarm = ''  ###это для того чтоб звук постоянно играл до нашего выкл, чтобы будильник не запускался каждую секунду.
root = Tk() #объект окошко вызвать в которую ввод данных идет
root.title('Будильник')
root.config(background = 'black')
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
##print(WIDTH, HEIGHT)
x = 300 ##размер окна выподающего
y = 200
root.geometry(f'{x}x{y}+{WIDTH // 2 - x // 2}'
              f'+{HEIGHT // 2 - y // 2 - 25}')

skreen_time = Label(root, text='00:00', font='Arial 50')
skreen_time.config(bg = 'black', fg = 'limegreen')
skreen_time.pack()


entry_time = Entry(root, width=10, font='Arial 20', justify='center')
entry_time.config(bg = 'darkred', fg = 'limegreen')
entry_time.pack(pady=5)

on = Button(root, text='Вкл', font=('Arial 10'), width=10, justify='center', command=on_click)
on.config(bg = 'black', fg = 'limegreen')
on.pack(pady=5)


off = Button(root, text='Выкл', font=('Arial 10'), width=10, justify='center', command=off_click)
off.config(bg = 'black', fg = 'limegreen')
off.config(bg = 'darkred', fg = 'yellow')
off.pack(pady=5)


tick() ####что за функция

root.mainloop()