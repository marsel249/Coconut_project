my_list = [1, 2, 3, 4, 5, 6, 7, 8, 10]
new_list = []

for i in my_list:
    new_list.append(i * 2)
print(new_list)

new_list = [i * 2 for i in my_list]
print(new_list)

new_list = map(lambda x: x * 2, my_list)
print(list(new_list))



my_list = [1, 2, 3, 4, 5, 6, 7, 8, 10]

new_list = []
for x in my_list:
    if x % 2 == 0:
        new_list.append(x)
print(new_list)

new_list = filter(lambda x: x % 2 == 0, my_list)
print(list(new_list))

new_list = filter(lambda x: x % 2 == 0, my_list)
new_list = list(new_list)
print(new_list)

new_list = [x for x in my_list if x % 2 == 0] # Добавить х, в список [], каждый, что найдем в списке my_list, что соответствует условию if x%2==0
print(new_list)


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 10]
new_dict = {}

for x in my_list:
    new_dict[x] = x * 3
print(new_dict)

new_dict = {x: x * 3 for x in my_list}
print(new_dict)

new_dict = {x * 3: x for x in my_list}
print(new_dict)


data = [('one', 'two'), ('three', 'four')]

new_dict = {}
for key, value in data:
    new_dict[key] = value
print(new_dict)

new_dict = {key: value for key, value in data}
print(new_dict)

new_dict = dict(data)
print(new_dict)


countries = ['USA', 'Hawaii', 'Cuba']
temps = [23, 33, 35]

data = list(zip(countries, temps))
print(data)
data = dict(data)
print(data)