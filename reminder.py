from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame



t = 0
music = False


def set():
    global t
    rem = sd.askstring("Time Reminder", "Enter a Reminder HH:MM")
    if rem:
        try:
            hour = int(rem.split(":")[0])
            minute = int(rem.split(":")[1])  #почему не 3?
            now = datetime.datetime.now()
            print(now)
            dt = now.replace(hour=hour, minute=minute, second=0, microsecond=0 )
            # print(dt)
            t = dt.timestamp()
            # print(t)
            text = sd.askstring("What Reminder?", "Please Write me a reminder of what?")
            label.config(text=f"Reminder at {hour:02}:{minute:02}")
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
    global music
    music = True
    pygame.mixer.init()
    pygame.mixer.music.load("Sound_01036.mp3")
    pygame.mixer.music.play()


def stop_snd():
    global music
    if music:
        pygame.mixer.music.stop()
        music = False
    label.config(text="try again?")




window = Tk()
window.geometry("280x150")
window.title("Simple Reminder")
window.config(bg="pink")
canvas = Canvas(width=250, height=180)
img = PhotoImage("hour.ico")
window.iconbitmap(True, img)
label = Label(window, text="Add a Reminder", font=("Times New Roman", 14), bg="pink", fg="black")
label.pack(pady=10)


set_button = Button(text="Set a Reminder", command=set, bg="green", fg="black")
set_button.pack(pady=10)
set_button.pack(pady=10)
stop_button = Button(text="Stop a Reminder", command=stop_snd, bg="red", fg="black")
stop_button.pack(pady=10)

check()


window.mainloop()
