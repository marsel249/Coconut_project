from time import sleep

from playwright.sync_api import Page
import time

'''DemoQA'''

# def test_text_box(page: Page):
#     page.goto('https://demoqa.com/text-box')
#
#     # # вариант №1
#     # username_locator = '#userName'
#     # page.fill(username_locator, 'testQa')
#     #
#     # # вариант №2
#     # page.locator('#userName').fill('testQa')
#
#     # вариант №3
#     page.fill(selector='#userName', value='testQa_1')
#
#     page.fill(selector='#userEmail', value='testQa_2@mail.ru')
#     page.fill(selector='#currentAddress', value='testQa_3')
#     page.fill(selector='#permanentAddress', value='testQa_4')
#
#
#     # page.locator('#submit').click()  # можно сначала определить локатор, а потом кликнуть
#     page.click('#submit')  # а можно сразу селектор передать внутрь метода click()
#     time.sleep(10)



# from playwright.sync_api import Page, expect
# import time
#
#
# def test_text_box_1(page: Page):
#     page.goto('https://demoqa.com/text-box')
#
#     username_locator = '#userName'
#     page.fill(username_locator, 'testQa')
#     page.fill('#userEmail', 'test@qa.com')
#     page.fill('#currentAddress', 'Phuket, Thalang 99')
#     page.fill('#permanentAddress', 'Moscow, Mashkova 1')
#
#     page.click('button#submit')
#
#     expect(page.locator('#output #name')).to_have_text('Name:testQa')
#     expect(page.locator('#output #email')).to_have_text('Email:test@qa.com')
#     expect(page.locator('#output #currentAddress')).to_have_text('Current Address :Phuket, Thalang 99')
#     expect(page.locator('#output #permanentAddress')).to_have_text('Permananet Address :Moscow, Mashkova 1')


'''Cinescope'''

from playwright.sync_api import Page
import time


# def test_text_box_2(page: Page):
#     page.goto('https://dev-cinescope.coconutqa.ru/register')
#
#     # вариант №1
#     username_locator = '[data-qa-id="register_full_name_input"]'
#     page.fill(username_locator, 'Жмышенко Валерий Альбертович')
#
#     # вариант №2
#     page.locator('[data-qa-id="register_full_name_input"]').fill('Жмышенко Валерий Альбертович')
#
#     # вариант №3
#     page.fill(selector='[data-qa-id="register_full_name_input"]', value='Жмышенко Валерий Альбертович')
#
#     time.sleep(10)


# from playwright.sync_api import Page
# from random import randint
# import time
#
#
# def test_registration(page: Page):
#     page.goto('https://dev-cinescope.coconutqa.ru/register')
#
#     # вариант №1
#     username_locator = '[data-qa-id="register_full_name_input"]'
#     email_loacor = '[data-qa-id="register_email_input"]'
#     password_locator = '[data-qa-id="register_password_input"]'
#     repeat_password_locator = '[data-qa-id="register_password_repeat_input"]'
#
#     user_email = f'test{randint(1, 9999)}@mail.ru'
#
#     page.fill(username_locator, 'Жмышенко Валерий Альбертович')
#     page.fill(email_loacor, user_email)
#     page.fill(password_locator, 'Qwerty123')
#     page.fill(repeat_password_locator, 'Qwerty123')
#
#     page.click('[data-qa-id="register_submit_button"]')
#
#     time.sleep(10)


# from playwright.sync_api import Page, expect
# from random import randint
# import time
#

# def test_registration_1(page: Page):
#     page.goto('https://dev-cinescope.coconutqa.ru/register')
#
#     # вариант №1
#     username_locator = '[data-qa-id="register_full_name_input"]'
#     email_loacor = '[data-qa-id="register_email_input"]'
#     password_locator = '[data-qa-id="register_password_input"]'
#     repeat_password_locator = '[data-qa-id="register_password_repeat_input"]'
#
#     user_email = f'test{randint(1, 9999)}-admin@email.qa'
#
#     page.fill(username_locator, 'Жмышенко Валерий Альбертович')
#     page.fill(email_loacor, user_email)
#     page.fill(password_locator, 'qwerty123Q')
#     page.fill(repeat_password_locator, 'qwerty123Q')
#
#     page.click('[data-qa-id="register_submit_button"]')
#
#     page.wait_for_url('https://dev-cinescope.coconutqa.ru/login') #Ждать этот url
#     expect(page.get_by_text("Подтвердите свою почту")).to_be_visible(visible=True) #проверить, есть ли этот текст на странице,
#     # дождаться момента, когда он будет виден
#
#     sleep(5)


import re
from playwright.sync_api import Page, expect


def test_codegen(page: Page) -> None:
    page.goto('https://demoqa.com/text-box', timeout=50000)

    page.get_by_role("textbox", name="Full Name").click()
    page.get_by_role("textbox", name="Full Name").fill("Ivan Ivanov")
    page.get_by_role("textbox", name="Full Name").press("Tab")
    page.get_by_role("textbox", name="name@example.com").fill("ivanov@mail.ru")
    page.get_by_role("textbox", name="name@example.com").press("Tab")
    page.get_by_role("textbox", name="Current Address").fill("lalalallnrfrjberjfbjh349438")
    page.get_by_role("textbox", name="Current Address").press("Tab")
    # page.pause() #Запускает отладчик, во время теста
    page.locator("#permanentAddress").fill("nvjdkvnkjnvkjfenvkj")
    page.get_by_role("button", name="Submit").click()
    expect(page.locator("#name")).to_contain_text("Name:Ivan Ivanov")
    expect(page.locator("#email")).to_contain_text("Email:ivanov@mail.ru")
    expect(page.locator("#output")).to_contain_text("Current Address :lalalallnrfrjberjfbjh349438")
    expect(page.locator("#output")).to_contain_text("Permananet Address :nvjdkvnkjnvkjfenvkj")

    # tree = page.accessibility.snapshot() #Поиск всех ролей на странице
    # # print(tree)
    #
    # # def walk(node):
    # #     if node.get("role") == "textbox":
    # #         print("textbox:", node.get("name"))
    # #     for child in node.get("children", []):
    # #         walk(child)
    # #
    # # walk(tree)

    sleep(5)

    '''
    
    CSS 
    
    page.locator("input#search.input_main")
    <input id="search" class="input_main" type="text" placeholder="Поиск...">
    
    page.locator('.submit-button')
    <button class="submit-button">Отправить</button>
    
    page.locator('#search')
    <input id="search" type="text" placeholder="Поиск...">
    
    page.locator('[name="agreement"]')
    <input type="checkbox" name="agreement">
    
    page.locator('p:has-text("Загрузка завершена")') 
    <p>Процесс завершен. Загрузка завершена успешно.</p>
    #фильтрует найденные элементы по тексту. Он оставляет только те элементы, которые содержат переданный текст
    #ищет текст только внутри самого элемента, на котором он применяется. Он не ищет текст во вложенных элементах!!11
    
    page.locator('button', text='Отправить')
    <button class="submit-button">Отправить</button>
    page.locator(text='Отправить')
    
    page.locator("input") #найдет все input
    <input type="checkbox" name="agreement">
    <input type="checkbox" name="agreement1">
    <input type="checkbox" name="agreement2">
    
    page.locator("#product-card span").text_content() #3 одинаковых локатора
    page.locator("#product-card >> .price")
    page.locator("#product-card").locator(".price")
      
        <div id="product-card">
            <span class="price">1000 руб.</span>
                </div>
                '''
                
'''page.get_by_role()
    
    <button>Sign in</button>
    page.get_by_role("button", name="Sign in").click()
    
    locator = page.get_by_role("button", name="Sign in")
    locator.hover()  # Элемент DOM будет найден перед наведением
    locator.click()  # И снова элемент DOM будет найден перед кликом
    
    <h3>Sign up</h3>
    <label>
      <input type="checkbox" /> Subscribe
    </label>
    <br/>
    <button>Submit</button>

    expect(page.get_by_role("heading", name="Sign up"))
    page.get_by_role("checkbox", name="Subscribe")
    page.get_by_role("button", name=re.compile("submit", re.IGNORECASE)) #Регулярное выражение для name
    
    Ролевые локаторы включают `button`, `checkbox`, `heading`, `link`, `list`, `table` и 
    многие другие и соответствуют спецификациям W3C для ARIA role, ARIA attributes и доступного имени. 
    Обратите внимание, что многие HTML-элементы, такие как `<button>`, имеют *подразумеваемую роль*, 
    которая распознается локатором роли    
    
    
    Как элемент получает ARIA роль
    Неявная (implicit) роль — из тега/атрибутов:
    <button> → role="button"
    <a href="..."> → role="link"
    <h1>…<h6> → role="heading"
    <input type="checkbox"> → role="checkbox"
    <input type="submit"> → role="button"
    <img alt="..."> → role="img"
    Явная (explicit) роль — через атрибут:
    <div role="dialog">...</div>
    <div role="tablist">...</div>
    
    # sync API
tree = page.accessibility.snapshot()
print(tree)  # большой словарь с roles/names/children

# найти все кнопки и их имена:
def walk(node):
    if node.get("role") == "button":
        print("BUTTON:", node.get("name"))
    for child in node.get("children", []):
        walk(child)

walk(tree)

РЕКОМЕНДУЕТСЯ
Использоать с интеративными элементами, кнопки, ссылки, чекбоксы..
    '''

'''page.get_by_text()

<span>Welcome, John</span>
page.get_by_text("Welcome") #Найдет элемент, содержащий "Welcome"
page.get_by_text("John") #Найдет элемент, содержащий "John"

<span>Welcome, John</span>
page.get_by_text("Welcome, John", exact=True)
#Этот код найдет элемент <span> с точным текстом "Welcome, John".  Элемент <span>Welcome, John!</span> не будет найден.

<span>Welcome, John</span>
page.get_by_text(re.compile("welcome, john", re.IGNORECASE))
#Этот код найдет элемент <span>, содержащий текст "welcome, john" (регистр не важен).

РЕКОМЕНДУЕТСЯ 
Используют текстовые локаторы для поиска НЕинтерактивных элементов, таких как <div>, <span>, <p> и т.д. 
Для интерактивных элементов, таких как button, <a>, <input> и т.д., лучше использовать ролевые локаторы
'''

'''
page.get_by_label()

Метод page.get_by_label() ищет элемент управления формы (например, <input>, <textarea>, <select>), 
связанный с указанной меткой <label>.  Связь между меткой и элементом управления обычно устанавливается 
с помощью атрибута for у <label>, который ссылается на id элемента управления.

Убедитесь, что метка <label> имеет атрибут for, который корректно ссылается на id соответствующего элемента управления. 
Это ключевое условие для работы get_by_label()

<label for="password">Password</label>
<input type="password" id="password" />

page.get_by_label("Password")

<label for="message">Message</label><br/>
<textarea id="message"></textarea>

page.get_by_label("Message").fill("This is my message.")

<label for="country">Country:</label>
<select id="country">
  <option value="us">United States</option>
  <option value="ca">Canada</option>
</select>

page.get_by_label("Country:").select_option("ca")

РЕКОМЕНДУЕТСЯ 
Используют этот локатор при поиске элементов управления форм.  
Это предпочтительный способ взаимодействия с полями ввода.
'''

'''
page.get_by_placeholder()

<input type="email" placeholder="name@example.com" />
page.get_by_placeholder("name@example.com").fill("playwright@microsoft.com")

<input type="text" placeholder="Search..." />
page.get_by_placeholder("Search...").fill("my query")

<input type="password" placeholder="Enter your password" />
page.get_by_placeholder("Enter your password").fill("mysecretpassword")

РЕКОМЕНДУЕТСЯ
Используйте get_by_placeholder(), когда работаете с полями ввода, у которых есть атрибут placeholder, но отсутствуют метки.'''


'''
page.get_by_alt_text()

<img alt="playwright logo" src="/img/playwright-logo.svg" width="100" />
page.get_by_alt_text("playwright logo").click()

<img alt="playwright logo" src="/img/playwright-logo.svg" width="100" />
<img alt="another logo" src="/img/another-logo.svg" width="100" />

page.get_by_alt_text("playwright logo").click() #Кликнет по первому изображению с alt="playwright logo"


<img src="navigation.gif" usemap="#map">

<map name="map">
  <area shape="rect" coords="0,0,82,126" href="news.html" alt="News">
  <area shape="circle" coords="90,58,3" href="products.html" alt="Products">
</map>

page.get_by_alt_text("News").click()
'''

'''
page.get_by_title()

<span title='Issues count'>25 issues</span>

page.get_by_title("Issues count")

<a href="/about" title="About us page">About</a>
page.get_by_title("About us page").click()

<img src="logo.png" alt="Company Logo" title="Company Logo - Home Page" />
page.get_by_title("Company Logo - Home Page").click()

Используйте этот локатор, когда у вашего элемента есть атрибут title
'''

'''
page.get_by_test_id()

<button data-testid="directions">Itinéraire</button>

page.get_by_test_id("directions").click()

playwright.selectors.set_test_id_attribute("data-pw")
Теперь в HTML вы можете использовать data-pw в качестве своего test id вместо data-testid по умолчанию

<button data-pw="directions">Itinéraire</button>
page.get_by_test_id("directions").click()
#По-прежнему используем "directions", но ищем по data-pw
'''

