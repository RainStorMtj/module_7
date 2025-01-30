import os
import time
directory = "."
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(os.path.abspath(file))
        filetime = os.path.getmtime(file)
        formated_time = time.strftime('%d.%m.%Y %H:%M', time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formated_time}, '
              f'Родительская директория: {parent_dir}')