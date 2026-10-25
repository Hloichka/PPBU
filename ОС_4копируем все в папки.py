from tkinter import *
from tkinter import filedialog as fd
import os
from datetime import datetime
import shutil


window = Tk()
window.withdraw()

direct = fd.askdirectory(title="выберите папку копирования:")

if direct:
    new_dir = direct + "_new"
    if not os.path.exists(new_dir):
        try:
            shutil.copytree(direct, new_dir)
            print(f"все содержимое папки {direct} скопированно в папку {new_dir}")
        except Exception as e:
            print(f"ошибка при кодирование: {e}")
    else:
        print(f"папка {new_dir} уже существует")
else:
    print("папка не была выбрана")




window.mainloop()