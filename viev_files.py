from os import listdir
from os.path import isfile, join

path = input("Ведите путь для поиска файлов: ") #input .
f = '.'
onlyfiles = []
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
print(*onlyfiles)