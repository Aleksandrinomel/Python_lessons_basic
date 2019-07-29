import math


class Figure:
    def __init__(self,verts):
        self.verts = [v[0:] for v in verts]

    def get_length(self, v1, v2):

        return math.sqrt((v1[0]-v2[0])**2+(v1[1]-v2[1])**2)

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


class Triangle(Figure):
    def __init__(self, verts):
        if len(verts)!=3:
            print('это не треугольник!')
        super().__init__(verts)
        self.sides = []
        self.sides.append(super().get_length(self.verts[0], self.verts[1]))
        self.sides.append(super().get_length(self.verts[2], self.verts[1]))
        self.sides.append(super().get_length(self.verts[0], self.verts[2]))

    def perimeter(self):
        return self.sides[0]+self.sides[1]+self.sides[2]

    def square(self):
        p = self.perimeter()/2

        return math.sqrt(p*(p-self.sides[0])*(p-self.sides[1])*(p-self.sides[2]))

    def height(self, v):
        s = self.square()
        if v == 1:
            return 2 * s / self.sides[0]
        elif v == 2:
            return 2 * s / self.sides[1]
        elif v == 3:
            return 2 * s / self.sides[2]


vertexes = [[0,0],[0,2],[3,0]]
tr = Triangle(vertexes)
print(tr.verts)
print('периметр = ', '{:.2f}'.format(tr.perimeter()))
print('площадь = ', '{:.2f}'.format(tr.square()))
print('высота из первой вершины: ', '{:.2f}'.format(tr.height(1)))


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Isosceles_trapezium(Figure):
    def __init__(self, verts):
        super().__init__(verts)
        self.sides = self.get_sides()

    def get_sides(self):
        sides = []
        v_prev = self.verts[3]
        for v in self.verts:
            sides.append(self.get_length(v_prev, v))
            v_prev = v
        return sides

    def is_isosceles(self):
        def is_parallel(v1,v2,v3,v4):
            return (v1[1] == v2[1] and v3[1] == v4[1])or(v1[0]-v2[0])/(v1[1]-v2[1]) == (v4[0]-v3[0])/(v4[1]-v3[1])

        if is_parallel(self.verts[0], self.verts[1], self.verts[2], self.verts[3]) and self.sides[0]==self.sides[2]\
            or is_parallel(self.verts[1], self.verts[2], self.verts[3], self.verts[0]) and self.sides[1]==self.sides[3]:
                return True
        else:
            return False

    def perimeter(self):
        return sum(self.sides)

    def square(self):

        if self.sides[0]==self.sides[2]:
            a = self.sides[1]
            b = self.sides[3]
            c = self.sides[0]
        else:
            a = self.sides[0]
            b = self.sides[2]
            c = self.sides[1]
        return (a+b)/2*math.sqrt(c*c-((a-b)/2)**2)


vertexes = [[0,0],[2,5],[7,5],[9,0]]
trapezium = Isosceles_trapezium(vertexes)
print('это равнобокая трапеция' if trapezium.is_isosceles() else 'это НЕ равнобокая трапеция')
print('длины сторон: ', *['{:.2f}'.format(i) for i in trapezium.sides])
print('периметр = ', '{:.2f}'.format(trapezium.perimeter()))
print('площадь = ', '{:.2f}'.format(trapezium.square()))