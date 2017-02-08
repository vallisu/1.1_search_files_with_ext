#!C:\Python30\python

# Входные данные: путь к папке и расширение файла
# Выходные данные: самый последний по дате создания файл заданного расширения.
# Если в директории несколько файлов с заданным расширением, то результатом должен
# быть самый "свежий" файл +  список файлов
# дата создания которых отличается от этого файла не более чем на 10 секунд.

# Import of the os module for working with OS
import os

print('Search a latest created file(s) with a given extension.\n')

# Enter path
path = input('Enter path with files: ')
while os.path.exists(path) is False:
    path = input('The entered path is incorrect. Try again: ')

# Create a list of files in the entered folder
files = os.listdir(path)

# Add absolute path for each file
files = [os.path.join(path, file) for file in files]

# Enter extension
ext = input('Enter an file extension: ')

# Create a list of files with the entered extension
files_with_ext = list(filter(lambda x: x.endswith(ext), files))
if len(files_with_ext) == 0:
    input('Files with the entered extension are absent. Press any key to exit. ')
    exit(0)

# Find a latest created file
last = max(files_with_ext, key=os.path.getctime)

# Create a list of create times
create_time = [os.path.getctime(file) for file in files_with_ext]

# Loop for searching files with 10 sec difference
length = len(create_time)
for i in range(length):
    if os.path.getctime(last) - create_time[i] <= 10:
        print(os.path.basename(files_with_ext[i]))
