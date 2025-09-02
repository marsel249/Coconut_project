'''Запуск плэйрайта, браузера, открытие вкладки, загрузка url, закрытие браузера, остановка плэйрайта'''
from time import sleep

# from playwright.sync_api import sync_playwright
#
#  '''Эта строка говорит Python, что нам нужен специальный инструмент (функция sync_playwright)
#  из библиотеки Playwright для работы с браузером. sync_api означает,
# что мы будем использовать синхронный (последовательный) стиль программирования'''
#
#
# import time
#
# # import platform
# # os_name = platform.system().lower()
# # linux_name = 'linux' in os_name # Не на linux - возвращает False
#
# # Создаем экземпляр Playwright и запускаем его
# playwright = sync_playwright().start()
#
# # Далее, используя объект playwright, можно запускать браузер и работать с ним
# # browser = playwright.chromium.launch(headless=False, slow_mo=50)
# # browser = playwright.chromium.launch(headless=linux_name, slow_mo=50) #Сделал так, что не на linux - браузер открывается
# #На linux - работа в безголовом режиме, чтобы запускаться на серверах
# # browser = (playwright.firefox.launch(headless=False, slow_mo=50)) #firefox
# browser = (playwright.webkit.launch(headless=False, slow_mo=50)) #safari
# page = browser.new_page()
# page.goto('https://demoqa.com/')
# time.sleep(10)  # Сделаем sleep иначе браузер сразу закроектся перейдя к следующим строкам
#
# # После выполнения необходимых действий, следует явно закрыть браузер
# browser.close()
#
# # И остановить Playwright, чтобы освободить ресурсы
# playwright.stop()



''' Запуск 2х браузеров'''
# from playwright.sync_api import sync_playwright
# import time
#
#
# def test_multiple_browsers():
#     with sync_playwright() as p:
#         chromium_browser = p.chromium.launch(headless=False)
#         firefox_browser = p.firefox.launch(headless=False)
#
#         chromium_page = chromium_browser.new_page()
#         firefox_page = firefox_browser.new_page()
#
#         chromium_page.goto("https://www.example.com")
#         firefox_page.goto("https://www.google.com")
#
#         time.sleep(10)
#
#         chromium_browser.close()
#         firefox_browser.close()

'''Page создается внутри Context. Может быть несколько Page в одном Context (как несколько вкладок в одном окне браузера).

Открываем один браузер, 5 вкладок'''

# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context()
#     page1 = context.new_page()  # Первая страница (вкладка)
#     page2 = context.new_page()  # Вторая страница (вкладка)
#     page3 = context.new_page()  # Третья страница (вкладка)
#     page4 = context.new_page()  # Четвертая страница (вкладка)
#     page5 = context.new_page()  # Пятая страница (вкладка)
#
#     page1.goto("https://www.google.com")
#     page2.goto("https://www.google.com")
#     page3.goto("https://www.google.com")
#     page4.goto("https://www.google.com")
#     page5.goto("https://www.google.com")
#     sleep(5)
#
#     # ... (работаем с page1 и page2)
#
#     context.close()
#     browser.close()

'''Разбор примера

Запуск двух окон браузера(1 браузер, 2 контекста(окна)), в каждом по 2 страницы'''

# from playwright.sync_api import sync_playwright
# import time
#
#
# def test_some_entities():
#     with sync_playwright() as p:
#         # Запускаем браузер
#         browser1 = p.chromium.launch(headless=False)
#
#         # создаем 2 контекста
#         context1_1 = browser1.new_context()
#         context1_2 = browser1.new_context()
#
#         # В каждом контексте создаем по 2 пейджи
#         page1_1_1 = context1_1.new_page()
#         page1_1_2 = context1_1.new_page()
#         page1_2_1 = context1_2.new_page()
#         page1_2_2 = context1_2.new_page()
#
#         # переходим на разные сайты
#         page1_1_1.goto("https://www.example.com")
#         page1_1_2.goto("https://www.google.com")
#         page1_2_1.goto("https://www.wikipedia.org")
#         page1_2_2.goto("https://www.yandex.ru")
#
#         # немного ждем чтобы осмотреться
#         time.sleep(10)
#
#         # Закрываем пейджи
#         page1_1_1.close()
#         page1_1_2.close()
#         page1_2_1.close()
#         page1_2_2.close()
#
#         # Закрываем контексты
#         context1_1.close()
#         context1_2.close()
#
#         # Закрываем браузер
#         browser1.close()


'''Тест фикстур'''

def test_example(page):  # page автоматически будет предоставлена фикстурой
    page.goto("https://www.example.com")

def test_google(page):  # page автоматически будет предоставлена фикстурой
    page.goto("https://www.google.com")

import time


def test_some_entities(page):
    page.goto('https://demoqa.com')
    time.sleep(10)