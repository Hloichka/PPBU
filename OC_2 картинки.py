from tkinter import *
from tkinter import filedialog as fd
import os

window = Tk()
window.withdraw()

direct = fd.askdirectory()

def direct():
    for file in os.listdir(direct):
        if file.lower().endswith((".jpg, .jpeg, .png")):
            print(file)


window.mainloop()