import datetime
from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame


t = 0


def set():
    global t
    rem = sd.askstring("Time Reminder", "Enter a Reminder HH:MM")
    if rem:
        try:
            hour = int(rem.split(":")[0])
            minute = int(rem.split(":")[1])  #почему не 3?
            now = datetime.datetime.now()
            print(now)
            dt = now.replace(hour=hour, minute=minute)
            # print(dt)
            t = dt.timestamp()
            # print(t)
        except Exception as e:
            mb.showerror("Error!", f"Error: {e}")


def check():
    global t
    if t:
        now = time.time()
        if now >= t:
            play_snd()
            t = 0
    window.after(10000, check) # -> check здесь включает рекурсию (повторение, каждые 10000 (мл. сек) = 10 секунд)


def play_snd():
    pygame.mixer.init()
    pygame.mixer.music.load("Sound_01036.mp3")
    pygame.mixer.music.play()



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
