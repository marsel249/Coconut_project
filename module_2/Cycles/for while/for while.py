# FOR

# numbers = [1, 2, 3, 4, 5]
# for number in numbers:
#     print("Число:", number)

# count = 5
# while count > 0:
#     print("Счётчик:", count)
#     count -= 1


# fruits = ["яблоко", "банан", "вишня"]
# for fruit in fruits:
#     print("Фрукт:", fruit)

# word = "Python"
# for letter in word:
#     print("Буква:", letter)

# student_grades = {"Аня": 85, "Борис": 90, "Вика": 75}
# for student, grade in student_grades.items():
#     print(student, "получил(а)", grade)

# unique_numbers = {10, 20, 30}
# for number in unique_numbers:
#     print("Число из множества:", number)

# WHILE

# countdown = 5
# while countdown > 0:
#     print("Обратный отсчёт:", countdown)
#     countdown -= 1  # Уменьшаем значение
# print("Поехали!")

# user_input = ""
# while user_input != "да":
#     user_input = input("Хотите выйти? (да/нет): ")
# print("Вы вышли из программы.")

# counter = 0
# while True:
#     print("Итерация:", counter)
#     counter += 1
#     if counter == 3:  # Завершаем бесконечный цикл
#         break

# text = "Python"
# for char in text:
#     print(char)

text = "Hello, Python!"
vowels = "aeiou"
count = 0

for char in text.lower():
    if char in vowels:
        count += 1

print("Количество гласных:", count)