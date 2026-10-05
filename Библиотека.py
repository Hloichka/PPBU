from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
from PIL import Image, ImageTk


# ######from PIL import Image хз зачем?
# ####(пример)
# ###Загрузка изображения
# image = image.open("example.jpg")
# ###Задаем максимальный размер
# max_size = (100, 100)
# ###Изменение размера изображения
# image.thumbnail(max_size)


def quit():
    window.destroy()


def open():
    try:
        file = fd.askopenfilename()
        if file: ###если файл был выбран и он не пуст-то мы обработаем данные
            img = Image.open(file)
            imgconv = img
            width = int(ws.get()) ####гет берет значение из переменной которую указываешь перед точкой
            height = int(hs.get())
            img.thumbnail((width, height))
            imgtk = ImageTk.PhotoImage(img)
            img_window = Toplevel(window) ####Toplevel - верхний уровень
            img_window.title("Просмотр изображения") ###Изменили заголовок
            l = Label(img_window, image=imgtk)### создали метку и в нее разместили изображение
            l.pack() ###разместили метку
            l.image = imgtk
    except FileNotFoundError:
        mb.showerror("Ошибка", "Файл не найден")
    except OSError:
        mb.showerror("Ошибка", "Не удалось Открыть, возможно это не изображение")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка: {e}")


window = Tk()
window.title("Photo")
window.geometry("500x500")


l1 = Label(text="Ширина окна")
l1.pack() ###выводит значение выше, или окно. (можно делать в одну строчну но она станет не изменна)
ws = Spinbox(window, from_=100, to=1400, increment=100) ####дополнительное окно отображающее размер окна(сверху)
ws.pack()


h1 = Label(text="Высота окна")
h1.pack() ###выводит значение выше, или окно. (можно делать в одну строчну но она станет не изменна)
hs = Spinbox(window, from_=100, to=1200, increment=100) ####дополнительное окно отображающее размер окна(сверху)
hs.pack()


l = Label()
l.pack()


mainmenu = Menu(window)
window.config(menu=mainmenu)


filemenu = Menu(mainmenu, tearoff=0) ####чтоб меню держалось и не отклеивалось (лол а такое бывает?)
filemenu.add_command(label="Открыть...", command=open)
filemenu.add_separator()
filemenu.add_command(label="Выход", command=quit)
mainmenu.add_cascade(label="Файл", menu=filemenu)




window.mainloop()




