import os


def show_dir_content():
    content = os.listdir(os.getcwd())
    for i in content:
        print(i)


def remove_dir(dir_name):
    path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(path)
        print(f'Директория {path} успешно удалена')
    except FileExistsError:
        print(f'Директория {path} не была удалена, так как не существует')


def make_dir(dir_name):
    path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(path)
        print(f'Директория {path} успешно создана')
    except FileExistsError:
        print(f'Директория {path} не была создана, так как уже существует')
