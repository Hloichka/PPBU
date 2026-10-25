from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datatime
import time
import pygame


window = Tk()
window.title("Simple Reminder")
label = Label(window, text="Add a reminder")
label.pack(pady=10)


set_button = Button(text="Set a reminder", command=set)
set_button.pack(pady=10)
