# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Person:
    def __init__(self, fio):
        self.fio = fio.title()
        fio = self.fio.split()
        self.sur_name = fio[0]
        self.first_name = fio[1]
        self.patronymic = fio[2]

    @property
    def short_fio(self):
        return self.sur_name + ' ' + self.first_name[0] + '.' + self.patronymic[0] + '.'


class Teacher(Person):
    def __init__(self, fio, subject):
        Person.__init__(self, fio)
        self.subject = subject


class Student(Person):
    def __init__(self, fio, mother, father):
        Person.__init__(self, fio)
        self.mother = Person(mother)
        self.father = Person(father)


class TheClass:
    def __init__(self, students, teachers):
        self.students = students
        self.teachers = teachers


class School:
    def __init__(self, classes):
        self.classes = classes


teacher1 = Teacher('Терёхина Светлана Анатольевна', 'Maths')
teacher2 = Teacher('Корольчук Ирина Валерьевна', 'English')
teacher3 = Teacher('Старкова Наталья Юрьевна', 'Biology')

student1 = Student('Бобылёв Витольд Валерьевич', 'Бобылёва Белла Созоновна', 'Бобылёв Валерий Натанович')
student2 = Student('Селиверстов Дмитрий Артемович', 'Лыткина Гражина Альбертовна', 'Лыткин Артем Анатольевич')
student3 = Student('Кулагин Степан Феликсович', 'Кулагина Злата Геннадиевна', 'Кулагин Феликс Онисимович')
student4 = Student('Горшков Ипполит Максимович', 'Горшкова Арьяна Рубеновна', 'Горшков Максим Вадимович')
student5 = Student('Горбачёв Тарас Егорович', 'Горбачёва Динара Руслановна', 'Горбачёв Егор Петрович')
student6 = Student('Фролов Вальтер Артёмович', 'Фролова Виргиния Филипповна', 'Фролов Артем Робертович')

students_5A = [student1, student2, student3]
teachers_5A = [teacher1, teacher2]

students_5B = [student4, student5, student6]
teachers_5B = [teacher3, teacher2]

class_5A = TheClass(students_5A, teachers_5A)
class_5B = TheClass(students_5B, teachers_5B)

classes = {'5A': class_5A, '5B': class_5B}
school = School(classes)

while True:
    print("Меню:")
    print("Введите: '1' чтобы получить полный список всех классов школы")
    print("Введите: '2 (название класса)' чтобы получить список всех учеников в указанном классе ")
    print("Введите: '3 (ФИО ученика)' чтобы получить список всех предметов указанного ученика ")
    print("Введите: '4 (ФИО ученика)' чтобы узнать ФИО родителей указанного ученика ")
    print("Введите: '5 (название класса)' чтобы получить список всех Учителей, преподающих в указанном классе ")
    print("Введите: '6' чтобы выйти")
    command = input()
    if command[0] == '1':
        print("Список классов:")
        print(*school.classes.keys(), sep=', ')
    elif command[0] == '2':
        the_class = command[2:]
        print(*[student.short_fio for student in school.classes.get(the_class).students], sep=', ')
    elif command[0] == '3':
        st = command[2:]
        for value in school.classes.values():
            for student in value.students:
                if st == student.fio:
                    print(*[teacher.subject for teacher in value.teachers], sep=', ')
                    break
    elif command[0] == '4':
        st = command[2:]
        for value in school.classes.values():
            for student in value.students:
                if st == student.fio:
                    print(f"Мать: {student.mother.fio}, Отец: {student.father.fio}")
                    break
    elif command[0] == '5':
        the_class = command[2:]
        print(*[teacher.fio for teacher in school.classes.get('5A').teachers], sep=', ')
    elif command[0] == '6':
        break
    print('_____________________________________________________________________________')
