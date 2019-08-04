# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    array = [1,1]
    while len(array) < m:
        index_last1, index_last2 = len(array) - 2, len(array) - 1
        new_fib_number = array[index_last1] + array[index_last2]
        array.append(new_fib_number)
    return array[n:(m+1)]


print(fibonacci(5, 10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


# что-то вроде сортировки вставкой
def sort_to_max(origin_list):
    new_list = []
    while len(origin_list)>0:
        number = origin_list.pop()
        if len(new_list) == 0 :
            new_list.append(number)
        elif number >= max(new_list):
            new_list.append(number)
        elif number <= min(new_list):
            new_list.insert(0, number)
        else:
            for i in range(len(new_list)):
                if number >= new_list[i] and number <= new_list[i+1]:
                    new_list.insert(i+1, number)
                    break
    return new_list


sorted_list = sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
print(sorted_list)

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_filter(f, lst):
    return [x for x in lst if f(x)]


sample = [1,4,3,65,9,35,3,78,12]
print(my_filter(lambda x: x % 3 == 0, sample))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

points = [(0, 0),  (4, 0),  (1, 3),  (5, 3)]


def get_midpoint(point1, point2):
    return (point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2


def is_parallelogram(points):
    midpoints = {}
    p = 4
    for i in range(p):
        for j in range(p):
            if j <= i: continue
            midpoint = get_midpoint(points[i], points[j])
            if midpoint in midpoints:
                midpoints[midpoint] += 1
            else:
                midpoints[midpoint] = 1
    ones, twos = 0, 0
    for v in midpoints.values():
        if v == 1: ones += 1
        if v == 2: twos += 1
    return ones == 4 and twos == 1


print(is_parallelogram(points))
