from tkinter import *
from tkinter import filedialog as fd
import os

window = Tk()
window.withdraw()

direct = fd.askdirectory()

def direct():
    for file in os.listdir(direct):
        print(file)


window.mainloop()