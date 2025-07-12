# x = ()
# print(type(x))

# my_tuple = 1, 2, 3, 4, 5, 6
# print(type(my_tuple))
# del my_tuple[0]
# print(my_tuple)
# print(my_tuple[0])

# tuple1 = ({"object": "in_tuple"}, 2)
# tuple2 = tuple(tuple1)
# assert tuple1 == tuple2, f'кортеж {tuple1} не равен {tuple2}'
# print(tuple1 == tuple2)  # Вывод: True
# print(tuple2)

# Дан кортеж `("apple", "banana", "cherry", "apple")`
#
# 1. Найти индекс первого вхождения "apple”
# 2. Вывести в консоль сколько раз в кортеже встречается `"apple"`
# 3. Распаковать `"apple"` и `"banana"` в переменные `a` и `b`, а остальное - в массив `rest`
# 4. На основе полученного массива сделать кортеж `tuple_2`
# 5. написать `assert` на длину `tuple_2` , что она равна 2, с выводом ошибки

# x = ("apple", "banana", "cherry", "apple")
# print(x.index('apple'))
# print(x.count('apple'))
# a, b, *rest = x
# print(a, b, rest)
# tuple2 = (a, b, rest)
# print(tuple2, type(tuple2))
# c, d = rest
# print(c, d)
# tuple3 = (a,b,c,d)
# print(tuple3, type(tuple3))
# print(len(tuple2))
# assert len(tuple2) == 2, 'Все ошибаются, брат'
