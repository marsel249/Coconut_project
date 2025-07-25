class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        if new_radius < 0:
            print("Радиус не может быть отрицательным.")
        else:
            self._radius = new_radius

    @property
    def area(self):  # Вычисляемое свойство (площадь круга)
        return 3.14159 * self._radius**2

circle = Circle(5)
print(circle.area)  # Вывод: 78.53975
circle.radius = 10
print(circle.area) #вывод 314.159
circle.radius = -5
print(circle.area) #вывод 314.159