from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from tkinter import filedialog as fd
import requests
import json
import pprint
from bottle import response


def root_ask():
    pass


def ask_prof():
    with open('ask_prof.txt', 'r', encoding='utf-8') as f:
        ls = f.read().title().split()
        if ls in ask_prof:
            print(f"{f}")
    pass


def answer_prof():
    try:
        with open('ask_prof.txt', 'r', encoding='utf-8') as f:
            ls = f.read().title().split()
            if ls in answer:


    pass


def test_result():
    pass


def quit():
    root.destroy()
    pass







root = Tk()
root.title("Как ты устроен.")
root.geometry("500x200")


Label(root, text=f'Вопрос {root_ask}.').pack(pady=5, side=LEFT)

Label(root, text=f'{ask_prof}?').pack(pady=5, side=LEFT)

btn_answer_prof = Button(root, text="Ответить")
btn_next_ask = Button(root, text="Следующий")
btn_quit = Button(root, text="Выход")






root.mainloop()








