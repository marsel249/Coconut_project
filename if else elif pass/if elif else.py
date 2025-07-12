'''* Задание№1
дан код temperature = 120
*
* if temperature < 0:
*     print("Вода замёрзла (лёд)")
* elif 0 <= temperature < 100:
*     print("Вода жидкая")
* elif temperature == 100:
*     print("Вода закипела")
* else:
*     print("Вода в состоянии пара")
*
    1. Прочесть и код и попробовать без его запуска определить, какой будет вывод в консоль
    2. Воспроизвести это IDE и сверить
'''

temperature = 120

if temperature < 0:
    print("Вода замёрзла (лёд)")
elif 0 <= temperature < 100:
    print("Вода жидкая")
elif temperature == 100:
    print("Вода закипела")
else:
    print("Вода в состоянии пара")