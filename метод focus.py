####позволяет устанавливать фокус ввода на определенный виджет
####и пользоваться им без мыши
from tkinter import *

def next_widget(event):
    event.widget.tk_focusNext().focus()
    return

window = Tk()

entry1 = Entry()
entry1.pack()

entry2 = Entry()
entry2.pack()


entry1.bind('<Tab>', next_widget)
entry2.bind('<Tab>', next_widget)



window.mainloop()


