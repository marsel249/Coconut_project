'''Сделать переменную time, которая содержит время в секундах реализовать программу,
которая переводит их в часы, минуты и секунды и выводит время на экран

Пример работы:

time = 3661

результат работы: 1 час 1 минута 1 секунда'''

# time = 3661
# one_hour = 3600
# one_min = 60
# hours = 0
# minute = 0
# second = 0
#
# hours = time//one_hour
# # print(hours)
# minute = (time - (one_hour*hours))//one_min
# # print(minute)
# second = time - one_hour*hours - minute*one_min
# # print(second)
# print(f'результат работы: {hours} час {minute} минут {second} секунд')

time = 3661
one_hour = 3600
one_min = 60

hours = time//one_hour
remainder = time%one_hour
minute = remainder//one_min
second = remainder%one_min
print(f'результат работы: {hours} час {minute} минут {second} секунд')