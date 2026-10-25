from tkinter import *
from tkinter import filedialog as fd
import os
from datetime import datetime

window = Tk()
window.withdraw()

direct = fd.askdirectory()

def direct():
    for file in os.listdir(direct):
        if file.lower().endswith((".jpg, .jpeg, .png")):
            filepath = os.path.join(direct, file)
            lt = os.path.getmtime(filepath)
            ###print(lt)
            ft = datetime.fromtimestamp(lt).strftime("%d-%m-%Y %H:%M:%S")

            print(ft)


window.mainloop()