from tkinter import *
from tkinter import filedialog as fd, filedialog
import os
import shutil
from datetime import datetime
from tkinter import messagebox as mb


window = Tk()
window.withdraw()


def choose_dir():
    direct = fd.askdirectory()
    if direct:
        organize_photos(direct)


def organize_photos(directory):
    for file in os.listdir(directory):
        if file.lower().endswith(('.jpg', '.jpeg', '.png', 'HEIF')):
            filepath = os.path.join(directory, file)
            timestamp = os.path.getmtime(filepath)
            data = datetime.fromtimestamp(timestamp).strftime('%Y_%m')
            new_dir = os.path.join(directory, data)
            if not os.path.exists(new_dir):
                os.mkdir(new_dir)
            shutil.move(filepath, os.path.join(new_dir, file))
    mb.showinfo("готово.", "фотографии рассортированны!")






choose_dir()
window.mainloop()



