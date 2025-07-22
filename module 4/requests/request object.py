import requests
'''Можем смотреть отправленные заголовки,заголовки в ответе'''
# r = requests.get('https://en.wikipedia.org/wiki/Monty_Python')
# print(r.headers) #Смотрим хедеры
# print(r.request.headers) #Смотрим отправленные заголовки


'''Метод можно отправлять в параметрах, с помощью метода requests.request '''
# method = 'get'
# url = 'https://en.wikipedia.org/wiki/Monty_Python'
# response = requests.request(method=method, url=url)
# print(response.headers)
# print(response.request.headers)
#
# """То есть абсолютно идентичны следующие варианты написания:"""
#
# base_url = 'https://restful-booker.herokuapp.com/booking'
#
# response = requests.get(url=base_url)
# response = requests.request(method="GET", url=base_url)



