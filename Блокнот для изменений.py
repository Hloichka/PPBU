from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from transliterate import translit, get_available_language_codes
from deep_translator import GoogleTranslator


def delete():
    text.delete('1.0', END)
    update_status()


def transliter():
    try:
        source_text = text.get("1.0", END)
        t_text = translit(source_text, 'ru', reversed=True)
        text.delete('1.0', END)
        text.insert('1.0', t_text)
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка: {e}")
    update_status()


def translate():
    try:
        source_text = text.get("1.0", END)
        translator = Translator()
        t_text = translator.translate(source_text, src='ru', dest='en').text
        text.delete('1.0', END)
        text.insert('1.0', t_text)
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка: {e}")
    update_status()


def insert():
    try:
        file = fd.askopenfilename(
            filetypes=(("TXT files", "*.txt"),
                ("HTML files", "*.html;*.htm"),
                ("All files", "*.*")))
        if file: ###проверяем выбран ли файл
            with open(file, 'r', encoding='utf-8') as f:
                s = f.read()
            text.insert(1.0, s)
    except FileNotFoundError:
        mb.showerror("Ошибка!", "Файл не найден")
    except Exception as e:
        mb.showerror("Ошибка!", f"Произошла ошибка: {e}")
    update_status()


def save():
    try:
        file = fd.asksaveasfilename(
            filetypes=(("TXT files", "*.txt"),
                ("HTML files", "*.html;*.htm"),
                ("All files", "*.*")))
        if file:  ###проверяем выбран ли файл
            with open(file, 'w', encoding='utf-8') as f:
                s = text.get("1.0", END)
                f.write(s)
    except FileNotFoundError:
        mb.showerror("Ошибка!", "Файл не найден")
    except Exception as e:
        mb.showerror("Ошибка!", f"Произошла ошибка: {e}")


def quit():
    window.destroy()


def update_status():
    content = text.get(1.0, END)
    char_count = len(content)
    word_count = len(content.split())
    status_label.config(text=f'Символов: {char_count} Слов: {word_count}')


window = Tk()
window.title("Блокнот")


frame = Frame(window)
frame.pack()


text = Text(frame, width=50, height=10, bg='gray', wrap=WORD)
text.pack(side=LEFT)
text.bind("<Key>", lambda event: update_status())


scroll = Scrollbar(frame, command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)


# b1 = Button(window, text="Открыть файл", command=insert)
# b1.pack(side=LEFT)
# b2 = Button(window, text="Удаление текста", command=delete)
# b2.pack(side=LEFT)
# b3 = Button(window, text="Сохранить файл", command=save)
# b3.pack(side=LEFT)


status_label = Label(text='proba', anchor='w')
status_label.pack(fill=X)


menu_bar = Menu(window)
window.config(menu=menu_bar)

"""кнопка на окне"""
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)

"""меню в этой кнопке"""
file_menu.add_command(label="Открыть", command=insert)
file_menu.add_command(label="Сохранить", command=save)
file_menu.add_command(label="Удалить", command=delete)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=quit)


process_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Обработка", menu=process_menu)
process_menu.add_command(label="Трансляция", command=transliter)
process_menu.add_command(label="Перевод", command=translate)


update_status()
window.mainloop()
