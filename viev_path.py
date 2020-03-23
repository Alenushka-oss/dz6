import json
import os

def viev_path():
    dir_list = os.listdir(os.getcwd())
    for item in dir_list:
        if os.path.isfile(item):
            list_dir_data['files'].append(item)
        else:
            list_dir_data['dirs'].append(item)

FILE_NAME = 'dir_list'
if os.path.exists(FILE_NAME):
    list_dir_data = {
            'files': [],
            'dirs': [],
            }

with open('dir_list', 'r', encoding='utf-8') as f:
    f.read(json.dumps(list_dir_data))
with open('dir_list', 'w', encoding='utf-8') as f:
    f.write(json.dumps(list_dir_data)

if json.load(f) == list_dir_data :
    print ('Содержимое записано в файл dir_list')
else:
    print('Ошибка сохранения данных директории в файл')
