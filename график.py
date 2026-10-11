from tkinter import *
from  PIL import Image, ImageTk, ImageGrab
from tkinter import messagebox as mb
from tkinter import filedialog as fd


pen_color = "black"
pen_width = 3

def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x, y, x + pen_width, y + pen_width, fill=pen_color, outline=pen_color)


def set_width():
    global pen_width
    try:
        pen_width = int(width_entry.get())
    except ValueError:
        mb.showerror("Ошибка", f"Введите целое число.")


image_tk = None

def load_image():
    global image_tk
    try:
        file_path = fd.askopenfilename(filetypes=[('image files', '*.png;*.jpg;*.jpeg;*.bmp;*.gif')])
        if file_path:
            img = Image.open(file_path)
            image = img.resize((800, 400))
            image_tk = ImageTk.PhotoImage(image)
            canvas.create_image(0, 0, image=image_tk, anchor="nw")
            canvas.image = image_tk
    except Exception as e:
        mb.showerror("Ошибка", f"Ошибка: {e}")


def save_image():
    try:
        file_path = fd.asksaveasfilename(defaultextension='.png', filetypes=[('PNG files', '*.png')])
        if file_path:
            x = window.winfo_rootx()
            y = window.winfo_rooty()
            x1 = x + 800
            y1 = y + 400
            ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)
            mb.showinfo("Сохранено", "Изображение сохранено.")
    except Exception as e:
        mb.showerror("Ошибка", f"Не сохранено: {e}")


window = Tk()
window.title('Графический редактор')

canvas = Canvas(width=800, height=400)
canvas.pack()
canvas.bind("<B1-Motion>", draw)


colors = ["red", "green", "blue", "yellow", "cyan", "magenta", "purple", "orange", "white", "pink"]
for color in colors:
    lbl = Label(bg=color, width=8, height=2)
    lbl.pack(side=LEFT)
    lbl.bind("<B1-Motion>", lambda e, c=color: globals().update(pen_color=c))


def quit1():
    window.destroy()


# Button(text="Загрузить", command=load_image).pack()
# Button(text="Сахранить", command=save_image).pack()
Button(text="Установить толщину", command=set_width).pack(side=RIGHT)
width_entry = Entry(width=10, font=("Arial", 13))
width_entry.pack(side=RIGHT)
Label(text="Толщина линии: ").pack(side=LEFT)


menu_bar = Menu(window)
window.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить", command=load_image)
file_menu.add_command(label="Сохранить", command=save_image)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=quit1)





window.mainloop()
