# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

x = 2.5
equation = 'y = -12x + 11111140.2121'
exec(equation[:7] + f'{x}' + equation[9:])
print(y)
# вычислите и выведите y


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
#date = '01.11.1985'

# Примеры некорректных дат
#date = '01.02.1001'
#date = '1.12.1001'
#date = '-2.10.3001'

long_month = [1, 3, 5, 7, 8, 10, 12]
date = input("Введите дату в формате 'dd.mm.yyyy'")
day, month, year = date.split(".")

if len(day) != 2 or len(month) != 2 or len(year) != 4:
    print("Неверный формат даты!")
elif int(day) not in range(1, 32 if int(month) in long_month else 31):
    print("Неверно указан день!")
elif int(month) not in range(1, 13):
    print("Неверно указан месяц!")
elif int(year) not in range(1, 10000):
    print("Неверно указан год!")
else:
    print(f"Дата {date} указана верно")


# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

n = int(input("Введите номер комнаты:"))
rooms_numbers = 0
floors = 0
if 1 <= n <= 2000000000:
    for i in range(1, n + 1):
        if rooms_numbers + i ** 2 < n:
            rooms_numbers += i ** 2
            floors += i
        else:
            floor = floors + (n - (rooms_numbers + 1)) // i + 1
            pos = (n - (rooms_numbers + 1)) % i + 1
            print(f"Комната №{n} находится на {floor} этаже {pos}-ая слева)")
            break
else:
    print("Неверно введен номер!")



