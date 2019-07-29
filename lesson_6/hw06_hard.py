# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла
import os


class Worker:

    def __init__(self, name, salary, position, hour_rate, hours_worked=0):
        self.name = name
        self.salary = salary
        self.position = position
        self.hour_rate = hour_rate
        self.hours_worked = hours_worked

    @property
    def real_salary(self):
        if self.hours_worked == self.hour_rate:
            return self.salary
        elif self.hours_worked < self.hour_rate:
            return self.hours_worked / self.hour_rate * self.salary
        elif self.hours_worked > self.hour_rate:
            return self.salary + (self.hours_worked - self.hour_rate) * self.salary / self.hour_rate * 2


with open(os.path.join(os.getcwd(), 'data/hours_of.txt'), 'r', encoding='utf-8') as hours:
    h = {string.split()[0] + ' ' + string.split()[1]: int(string.split()[2]) for string in hours.readlines()[1:]}

with open(os.path.join(os.getcwd(), 'data/workers.txt'), 'r', encoding='utf-8') as workers:
    print("Имя                 Должность     Норма часов  Факт. часов   Оклад   Факт. зарплата")
    for string in workers.readlines()[1:]:
        s = string.split()
        w = Worker(s[0] + ' ' + s[1], int(s[2]), s[3], int(s[4]), h.get(s[0] + ' ' + s[1]))
        print(f'{w.name:<20}{w.position:<14}{w.hour_rate:<13}{w.hours_worked:<14}{w.salary:<8}{w.real_salary:.0f}')






