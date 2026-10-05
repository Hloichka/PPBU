from tkinter import *

window = Tk()  ####создаем окно
lb = Listbox(width=15, height=7) ####размеры окна в строках
lb.pack()   ####чтобы был размещен - куда? что это?
days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
for day in days:
    lb.insert(END, day) ###проще чем ниже вариант


# lb.insert(0, 'Понедельник') ### insert-это вставка
# lb.insert(1, 'Вторник')
# lb.insert(2, 'Среда')
# lb.insert(3, 'Четверг')
# lb.insert(4, 'Пятница')
# lb.insert(5, 'Суббота')
# lb.insert(6, 'Воскресенье')








window.mainloop() ###чтобы окно вышло



