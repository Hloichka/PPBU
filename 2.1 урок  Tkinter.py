from tkinter import *
##модуль для ?

from index import text

def answer(event=None):
    answ = num.get().strip()
    result.configure(text=answ)

root = Tk() #объект окошко вызвать в которую ввод данных идет
root.title('start')
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
##print(WIDTH, HEIGHT)
x = 300 ##размер окна выподающего
y = 150
root.geometry(f'{x}x{y}+{WIDTH // 2 - x // 2}'
              f'+{HEIGHT // 2 - y // 2 - 25}')
##все что после + это мы играли с размером выпадающего окна
# по отношению к основному экрану пк.

# root.geometry('300x100+400+200')

##если хочу чтоб по середине экрана выходило окно-> определить параметры монитора пк (строка 12,13,14 str)

prompt = Label(text='введите значение', font='Arial 12')
prompt.pack(side=TOP)
# prompt.pack(side=BOTTOM) ## значение с какой стороны? (слева, справа, снизу, всерху)
# prompt.pack(side=LEFT)
# prompt.pack(side=RIGHT)
num = Entry(width=5, font='Arial 12', justify='center') ##(видджит)дает нам поле,
# куда пользователь может вводить текст (одну строку).
num.pack()

result = Label(width=5, text=' ', font='Arial 12', bg='lightgray') ##(видджит)дает нам текстовую метку — просто текст,
# который нельзя редактировать.
result.pack(pady=10)

btn = Button(text="Выполнить", command=answer)
btn.pack()

num.bind('<Return>', answer) ##повторяет введеные данные в нижнее окно

root.mainloop() ##обязательно прописывать, графический редактор

