from tkinter import *
from tkinter import filedialog as fd
import os
from datetime import datetime
import shutil


window = Tk()
window.withdraw()

direct = fd.askdirectory(title="выберите с изображениями:")

if direct:
    new_dir = direct + "_new"
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
    else:
        print(f"папка {new_dir} уже существует")
    for file in os.listdir(direct):
        if file.lower().endswith((".jpg", ".jpeg", ".png", "HEIF")):
            sourse_file = os.path.join(direct, file)  ###sourse это файл источник - где он находится ->
            destination_file = os.path.join(new_dir, file)
            try:
                shutil.move(sourse_file, destination_file)
                print("файл перемещен")
            except Exception as e:
                print(f"Ошибка перемещения файла {file}: {e}")
    print("Все скопированно")
else:
    print("папка не была выбрана")




window.mainloop()



