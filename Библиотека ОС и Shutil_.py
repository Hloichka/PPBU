""""помогает упорядочивать, изменять,
 перемещать файлы внутри ПК с помощью Пайтон
 в свойстве файла указаны его данные которые можно
 так же получить с помощью библиотеке ОС"""

import os
import shutil

"""полезные команиды"""

os.mkdir("new_folder") ###позволяет создать новую папку с именем new_folder

filepath = os.path.join(dir, file)  ### join даст полный путь соединяя две переменные

### dir - это переменная, создержащая путь к папки (путь как в пк С://...)
### file - переменная содержащая имя файла (как на пк)

last_time = os.path.getmtime(filepath) ### применяется для получения времени последнего изменения файла.

###filepath указывает на конкретный файл в файловой системе

####функция возвращает время последнего изменения файла (timestamp) с секундах с начала эпохи Unix
###Unix создан с (00:00 1.01.1970)

"""Например 1"""
import os
filepath = "C://path//to//yor//file.txt"
last_modified_time = os.path.getmtime(filepath)
print("время последнего изменения:",
      last_modified_time)
###время последнего изменения: 1704641921.6406274 секунд
"""Например 2"""
import os
from datetime import datetime
filepath = "C://path//to//yor//file.txt"
It = os.path.getmtime(filepath)
print("время последнего изменения:", last_modified_time)
ft = datetime.fromtimestamp(It).strftime("%Y-%m-%d %H:%M:%S")
print("дата и время изменения:", ft)
##время последнего изменения: 1704641921.6406274 секунд
##дата и время изменения: 2024-01-07 18:41:00


"""Например 3"""
os.path.exists("путь файла с пк вводится") ###существует ли вообще папка с этим именем (возвращает true or false)
import os
new_dir = "C://path//to//yor//new_folder"
if os.path.exists(new_dir):
    print("папка существует.")
else:
    print("папка не существует.")

"""Например 4"""
os.makedirs("путь к папки - которую хотите создать") ###сездает новые папки на пк по указаному пути
import os
new_directory = "C://path//to//yor//new_folder"
os.makedirs(new_directory)
print(f'папка {new_directory} успешно создана.')

"""Например 5"""
### shutil библиетека помогает копировать и изменять все содержимое папки)
shutil.copytree("C://path//to//yor//new_folder","имя файла") ###все содержимое с одного места в другое
import shutil
source_dir = "C://path//to//yor//new_folder"
destination_dir = "C://path//to//yor//new_folder_2"
print(f"все содержимое из {source_dir} скопировано в {destination_dir}")

"""Например 6"""
####shutil.move(путь - src, куда перемещаем - dst) перемещаем с одного места в другое
import shutil
shutil_file = "C://path//to//yor//file.txt"
destination_dir = "C://path//to//yor//new_folder"
shutil.move(shutil_file, destination_dir)
print(f"файл {shutil_file} перемещен в {destination_dir}")

"""Например 7""" ###перемещаем и меняем имя файлу
import shutil
source_file = "C://path//to//yor//file.txt"
destination_file = "C://path//to//yor//newname.txt"
shutil.move(source_file, destination_file)
print(f"файл {source_file} перемещен в {destination_file}")






