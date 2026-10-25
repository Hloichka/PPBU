import datetime
from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame


def set():
    rem = sd.askstring("Time Reminder", "Enter a Reminder HH:MM")
    if rem:
        try:
            hour = int(rem.split(":")[0])
            minute = int(rem.split(":")[1])  #почему не 3?
            now = datetime.datetime.now()
            print(now)
            dt = now.replace(hour=hour, minute=minute)
            print(dt)
            t = dt.timestamp()
            print(t)
        except Exception as e:
            mb.showerror("Error!", f"Error: {e}")




window = Tk()
window.geometry("300x200")
window.title("Simple Reminder")
img = PhotoImage("hour.ico")
window.iconbitmap(True, img)
label = Label(window, text="Add a Reminder")
label.pack(pady=10)


set_button = Button(text="Set a Reminder", command=set)
set_button.pack(pady=10)




window.mainloop()
