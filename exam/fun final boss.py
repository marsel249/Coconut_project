# Магазин гоблина из Warcraft 3

'''Гоблин открыл свой магазин, где продаются зелья, свитки и артефакты. Вам нужно написать программу, которая:

1. Имеет словарь товаров и их цен. Например:
    - Зелье лечения: 100 золотых
    - Зелье маны: 80 золотых
    - Свиток скорости: 150 золотых
    - Артефакт магии: 300 золотых
2. Запрашивает у игрока название товара и количество.
3. Проверяет, есть ли товар в магазине:
    - Если есть, программа рассчитывает стоимость и выводит её.
    - Если общая стоимость заказа превышает 500 золотых, гоблин делает скидку 20%.
    - Если товара нет, гоблин говорит: "У меня такого нет, попробуй в другом месте!"'''

shop = {'Зелье лечения': 100, 'Зелье маны': 80, 'Свиток скорости': 150, 'Артефакт магии': 300}

print('Welcome to VURDALAK SHOP\nname\t\t\tprice')
for name, price in shop.items():
    print(f'{name}\t\t{price}')

try:
    user_choice_name = input('What do you want?: ')
    if user_choice_name not in shop:
        print('Not have what you wnat :(')
        exit()
    user_choice_quantity = int(input('How many you want?: '))
    if user_choice_quantity <= 0:
        print('We not sale 0 items bro..')
        exit()

    total = shop[user_choice_name]*user_choice_quantity
    if user_choice_name in shop and total < 500:
        print(f'Yes! in stock..  {total} gold.. (Pss.. if you buy over 500gold, you get 20% sale)')
        # print(shop[user_choise_name])
    elif user_choice_name in shop and total >= 500:
        print(f'Yes! in stock..  {total*0.8:.2f} gold, (SALE 20%!!11, original price - {total} gold)')
    else:
        print('Error bro')
except(ValueError, TypeError):
    print('WTF bro?')
except Exception as e:
    print(f'Произошла ошибка: {e}')


