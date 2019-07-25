# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
from shutil import copyfile
import sys


def make_dirs():
    for i in range(1, 10):
        path = os.path.join(os.getcwd(), 'dir_' + str(i))
        try:
            os.mkdir(path)
            print(f'Директория {path} успешно создана')
        except FileExistsError:
            print(f'Директория {path} не была создана, так как уже существует')


def remove_dirs():
    for i in range(1, 10):
        path = os.path.join(os.getcwd(), 'dir_' + str(i))
        try:
            os.rmdir(path)
            print(f'Директория {path} успешно удалена')
        except FileExistsError:
            print(f'Директория {path} не была удалена, так как не существует')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def show_dirs():
    path = os.path.join(os.getcwd())
    with os.scandir(path) as scan_dir:
        for entry in scan_dir:
            if not entry.name.startswith('.') and entry.is_dir():
                print(entry.name)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_file():
    file_for_copy_path = os.path.realpath(__file__)
    copy_file_path = os.path.join(os.getcwd(), __file__[:-3] + '_copy' + __file__[-3:])
    try:
        copyfile(file_for_copy_path, copy_file_path)
        print('Файл успешно скопирован')
    except IOError:
        print('Нет возможности создать копию. Недоступна запись.')


if __name__ == '__main__':

    print('sys.path = ', sys.path)
    do = {'make_dirs': make_dirs,
          'remove_dirs': remove_dirs,
          'copy_file': copy_file}
    while True:
        print('Доступныe команды: make_dirs - создает папки, remove_dirs - удаляет созданные папки, '
              'copy_file - копирует файл, из которого был запущен данный скрипт')
        command = input('Введите команду: ')
        try:
            do[command]()
        except KeyError:
            print('Такой команды нет. Введите корректную команду')
