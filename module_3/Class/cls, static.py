class Dog:
    species = "Canis familiaris"  # Атрибут класса

    @classmethod
    def get_species(cls):  # cls ссылается на класс Dog
        return cls.species

print(Dog.get_species())

#_________
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def is_positive(x):
        return x > 0


# Использование статических методов
print(MathUtils.add(5, 7))  # Вывод: 12
print(MathUtils.multiply(3, 4))  # Вывод: 12