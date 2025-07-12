'''Задания:
* Списки: Создайте список colors с элементами "red", "green", и "blue". Добавьте в этот список "yellow", а затем удалите "green".
Проверьте идентификатор списка до и после изменений.
* Множества: Создайте множество numbers с числами 1, 2, 3. Добавьте в это множество 4 и удалите 1.
Проверьте, как изменилось содержимое множества.
* Словари: Создайте словарь person с ключами "name" и "age". Добавьте новый ключ "job" со значением "developer".
Затем измените значение "age" на 30. Проверьте, остаётся ли идентификатор словаря неизменным.
* Сравнение с неизменяемыми типами:Создайте список и кортеж с одинаковыми элементами.
Попробуйте изменить содержимое каждого из них. Объясните, почему список изменяется, а кортеж — нет.
'''

# x = ["red", "green", "blue"]
# x.append('yellow')
# print(x[3])
# print(x)
# x.remove('green')
# print(x)

# x = {1,2,3}
# print(type(x))
# print(x)
# x.add(4)
# print(x)
# x.remove(1)
# print(x)

person = {'name':1, 'age':2}
print(type(person), person)
person['job'] = 'developer'
print(type(person), person)
person['age'] = 30
print(type(person), person)

# x_list = [1, 2, 3]
# print(f'({x_list} - x_list', type(x_list))
# y_tuple = (1, 2, 3)
# print(f'({y_tuple} - y_tuple', type(y_tuple))
# x_list[0] = 4
# print(f'({x_list} - x_list', type(x_list))
# y_tuple[0] = 4 #error
# print(f'({y_tuple} - y_tuple', type(y_tuple)) #error

print(id(person)) #получаем id элемента в памяти
