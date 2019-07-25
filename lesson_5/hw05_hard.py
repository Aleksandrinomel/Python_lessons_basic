# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys
from shutil import copyfile

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - копия файла")
    print("rm <file_name> - удаление файла")
    print("cd <full_path or relative_path> сменить директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not dir_name:
        print('Укажите name path')
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print(f'path {dir_name} make')
    except FileExistsError:
        print(f'path {dir_name} exists')


def ping():
    print('pong')


def delete_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(os.getcwd(), file_name)
    try:
        os.remove(file_path)
        print(f'Файл {file_name} успешно удален')
    except FileNotFoundError:
        print(f'Невозможно удалить {file_name} - такой файл не существует')


def change_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(path)
        print('Вы успешно перешли в директорию {dir_name}')
        print(os.getcwd())
    except FileNotFoundError:
        print('Невозможно перейти в {dir_name} - такой директории не существует')


def copy_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_name_copy = str("copy_" + file_name)
    file_path = os.path.join(os.getcwd(), file_name_copy)
    try:
        copyfile(file_name, file_path)
        print(f'файл {file_name_copy} создан')
    except FileExistsError:
        print(f'файл {file_name} уже существует')
    except FileNotFoundError:
        print(f'файл {file_name} не существует')


def full_path():
    path = os.getcwd()
    print(path)


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "ls": full_path,
    "rm": delete_file,
    "cd": change_dir
}


try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print('Задан неверный ключ')
        print('Укажите ключ help для справки')
