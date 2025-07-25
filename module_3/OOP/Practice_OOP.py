'''Практический пример'''

''' **Описание задачи:**

Интернет-магазин должен предоставлять следующие возможности:

- Управление каталогом товаров.
- Добавление товаров в корзину.
- Оформление заказа с подсчётом общей стоимости.

 **Результат:**

- Программа поддерживает удобное добавление новых функций (например, скидки).
- Код становится более читаемым за счёт модульной структуры.'''

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class Cart:
#     def __init__(self):
#         self.items = []
#
#     def add_product(self, product, quantity):
#         self.items.append({"product": product, "quantity": quantity})
#
#     def calculate_total(self):
#         # return sum(item["product"].price * item["quantity"] for item in self.items) #Вариант реализации из курса
#         totall = []
#         for i in self.items:
#             result = i["product"].price * i["quantity"]
#             totall.append(result)
#             result = sum(totall)
#         return result #Вариант реализации мой
#
# class Order:
#     def __init__(self, cart):
#         self.cart = cart
#         self.status = "Pending"
#
#     def complete_order(self):
#         total = self.cart.calculate_total()
#         self.status = "Completed"
#         return f"Заказ завершён. Итоговая стоимость: {total} рублей"
#
# # Пример использования
# laptop = Product("Laptop", 1000)
# mouse = Product("Mouse", 50)
#
# cart = Cart()
# cart.add_product(laptop, 1)
# cart.add_product(mouse, 2)
#
# order = Order(cart)
# print(order.complete_order())  # Итоговая стоимость: 1100 рублей

