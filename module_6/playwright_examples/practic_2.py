'''Локаторы'''
from time import sleep
from datetime import date
import calendar
import re
from pathlib import Path

import pytest
from playwright.sync_api import Page, expect

def test_locators(page: Page):
    page.goto('https://demoqa.com/webtables')

    page.get_by_role('button', name='add').click()
    page.get_by_role("button", name="Close").click() #Выход из окна, чтобы повторно нажать кнопку, другим методом
    page.locator('#addNewRecordButton').click()

    page.get_by_role("button", name="Submit").is_visible()
    page.get_by_text('Registration Form').is_visible()

    page.get_by_role("textbox", name="First Name").fill('My First Name')
    page.get_by_placeholder('Last Name').fill('My Last name')
    page.locator('#userEmail').fill('example@example.com')
    page.locator('//*[@id="age"]').fill('99')
    page.locator('#salary').fill('1000')
    page.locator("//input[@placeholder='Department' and @id='department']").fill('something')
    page.get_by_role("button", name="Submit").click()

'''Взаимодействие с элементами'''
def test_interaction_with_elements(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')

    first_name = 'First Name'
    last_name = 'Last Name'
    email = 'example@mail.com'
    phone = '7999888888'
    year = '2024'
    month = '8' # По индексу
    day = '03'
    day_n = f"0{day}"
    address = 'Its Cerrent adress'
    state = "Rajasthan"
    city = "Jaipur"

    # деалем из переменных дату, формата 01 Jan 2000
    d = date(int(year), int(month) + 1, int(day))
    date_str = f"{d:%d} {calendar.month_abbr[d.month]} {d:%Y}"

    page.get_by_role("heading", name="Practice Form").is_visible()

    #textbox
    page.get_by_role("textbox", name="First Name").fill(first_name)
    page.get_by_role("textbox", name="Last Name").type(last_name)
    page.get_by_placeholder('name@example.com').fill(email)

    #radiobutton
    page.locator('label[for="gender-radio-1"]').click()
    page.get_by_role("radio", name="Female").check(force=True)
    page.locator('label[for="gender-radio-3"]').click()
    expect(page.locator('#gender-radio-3')).to_be_checked()

    #phone
    page.get_by_placeholder('Mobile Number').fill(phone)

    #calendar

    d = date.today()
    today_str = f"{d:%d} {calendar.month_abbr[d.month]} {d:%Y}"
    expect(page.locator("#dateOfBirthInput")).to_have_value(today_str) #Проверяем, что дефолт дата == сегодня


    page.locator("#dateOfBirthInput").click()
    expect(page.locator(".react-datepicker")).to_be_visible()

    page.locator(".react-datepicker__year-select").select_option(year)
    page.locator(".react-datepicker__month-select").select_option(month)  # January

    page.locator(f".react-datepicker__day--{day_n}:not(.react-datepicker__day--outside-month)").click()

    expect(page.locator("#dateOfBirthInput")).to_have_value(date_str)

    #Subject
    # page.locator("#subjectsInput").click()
    # page.locator("#subjectsInput").fill("Maths")
    # page.keyboard.press("Enter")
    # page.locator("#subjectsInput").fill("English")
    # page.keyboard.press("Enter")
    # chips = page.locator('.subjects-auto-complete__multi-value__label')
    # expect(chips).to_contain_text(["Maths", "English"])
    # page.pause()

    subjects = page.locator("#subjectsInput")

    def add_subject(name: str):
        subjects.click()
        subjects.fill(name)
        menu = page.locator(".subjects-auto-complete__menu")
        expect(menu).to_be_visible()  # ждём выпадение списка
        menu.get_by_text(name, exact=True).click()  # кликаем нужный пункт

    add_subject("Maths")
    add_subject("English")

    chips = page.locator('.subjects-auto-complete__multi-value__label')
    expect(chips).to_contain_text(["Maths", "English"])


    #checkbox
    # page.get_by_role("checkbox", name="Sports").check(force=True)
    # page.locator('label[for="hobbies-checkbox-2"]').click()
    # page.locator('label[for="hobbies-checkbox-3"]').click()
    #
    # page.get_by_text("Sports").click()
    # page.get_by_text("Reading").click()
    # page.get_by_text("Music").click()

    hobbies = page.locator("#hobbiesWrapper")  # контейнер
    for name in ["Sports", "Reading", "Music"]:
        cb = hobbies.get_by_text(name)
        cb.set_checked(True)
        expect(cb).to_be_checked()

    #file_upload
    file_name = "file_to_upload.jpg"
    file_path = Path(__file__).parent / file_name
    page.locator("#uploadPicture").set_input_files(str(file_path))

    #textbox
    page.get_by_role("textbox", name="Current Address").type(address)

    #Select
    page.get_by_text("Select State").click()
    page.get_by_text(state, exact=True).click()

    page.locator("div").filter(has_text=re.compile(r"^Select City$")).nth(3).click()
    page.get_by_text(city, exact=True).click()

    page.get_by_role("button", name="Submit").click()

    expect(page.get_by_text("Thanks for submitting the form")).to_be_visible()


    first_last_name = f'{first_name} {last_name}'
    expect(page.get_by_role("cell", name=first_last_name)).to_be_visible()
    expect(page.get_by_role("cell", name='Other')).to_be_visible()
    expect(page.get_by_role("cell", name=phone)).to_be_visible()
    date_str = f"{day} {calendar.month_name[int(month)+1]},{year}"
    expect(page.get_by_role("cell", name=date_str)).to_be_visible()
    objeccts = ["Maths", "English"]
    objeccts = ", ".join(objeccts)
    expect(page.get_by_role("cell", name=objeccts)).to_be_visible()
    expect(page.get_by_role("cell", name=file_name)).to_be_visible()
    expect(page.get_by_role("cell", name=address)).to_be_visible()
    location = f"{state} {city}"
    expect(page.get_by_role("cell", name=location)).to_be_visible()

    expect(page.locator("//span[text()='© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.']")).to_be_visible()


    sleep(5)

# Предыдущий тест, только с параметризацией (добавлена проверка на None)
@pytest.mark.parametrize("first_name,last_name,email,phone,year,month,day,address,state,city,gender,"
                         "subject1,subject2,subject3,hobie1,hobie2,hobie3", [
    ('Ivan', 'Ivanov', 'example@mail.com', '7999888888', '2024', '8', '02', 'Its Cerrent adress', 'Rajasthan', 'Jaipur',
     'Female', 'English', 'Maths', 'History', 'Sports', 'Reading', 'Music'),
('Alexandr', 'Suvorov', 'example1@gmail.com', '7999999999', '2020', '0', '11', 'My adress', 'Haryana', 'Panipat',
     'Male', 'Physics', 'English', None, 'Sports', None, 'Music')
])
def test_interaction_with_elements_with_parametrs(page: Page, first_name,last_name,email,phone,year,month,day,address,state,city,gender,
                         subject1,subject2,subject3,hobie1,hobie2,hobie3):
    page.goto('https://demoqa.com/automation-practice-form')

    day_n = f"0{day}"

    # деалем из переменных дату, формата 01 Jan 2000
    d = date(int(year), int(month) + 1, int(day))
    date_str = f"{d:%d} {calendar.month_abbr[d.month]} {d:%Y}"

    page.get_by_role("heading", name="Practice Form").is_visible()

    #textbox
    page.get_by_role("textbox", name="First Name").fill(first_name)
    page.get_by_role("textbox", name="Last Name").type(last_name)
    page.get_by_placeholder('name@example.com').fill(email)

    #radiobutton
    gender_ids = {"Male": "gender-radio-1", "Female": "gender-radio-2", "Other": "gender-radio-3"}
    gid = gender_ids[gender]

    page.locator(f"label[for='{gid}']").click()
    expect(page.locator(f"#{gid}")).to_be_checked()

    #phone
    page.get_by_placeholder('Mobile Number').fill(phone)

    #calendar
    d = date.today()
    today_str = f"{d:%d} {calendar.month_abbr[d.month]} {d:%Y}"
    expect(page.locator("#dateOfBirthInput")).to_have_value(today_str) #Проверяем, что дефолт дата == сегодня

    page.locator("#dateOfBirthInput").click()
    expect(page.locator(".react-datepicker")).to_be_visible()

    page.locator(".react-datepicker__year-select").select_option(year)
    page.locator(".react-datepicker__month-select").select_option(month)  # January

    page.locator(f".react-datepicker__day--{day_n}:not(.react-datepicker__day--outside-month)").click()

    expect(page.locator("#dateOfBirthInput")).to_have_value(date_str)

    subjects = page.locator("#subjectsInput")

    def add_subject(name=None):
        if name is None:
            return None
        subjects.click()
        subjects.fill(name)
        menu = page.locator(".subjects-auto-complete__menu")
        expect(menu).to_be_visible()  # ждём выпадение списка
        menu.get_by_text(name, exact=True).click()  # кликаем нужный пункт

    add_subject(subject1)
    add_subject(subject2)
    add_subject(subject3)

    chips = page.locator('.subjects-auto-complete__multi-value__label')
    expected_subjects = [s for s in (subject1, subject2, subject3) if s]
    expect(chips).to_have_count(len(expected_subjects))
    expect(chips).to_contain_text(expected_subjects)

    hobbies = page.locator("#hobbiesWrapper")  # контейнер
    for name in filter(None, (hobie1, hobie2, hobie3)):
        cb = hobbies.get_by_text(name)
        cb.set_checked(True)
        expect(cb).to_be_checked()

    #file_upload
    file_name = "file_to_upload.jpg"
    file_path = Path(__file__).parent / file_name
    page.locator("#uploadPicture").set_input_files(str(file_path))

    #textbox
    page.get_by_role("textbox", name="Current Address").type(address)

    #Select
    page.get_by_text("Select State").click()
    page.get_by_text(state, exact=True).click()

    page.locator("div").filter(has_text=re.compile(r"^Select City$")).nth(3).click()
    page.get_by_text(city, exact=True).click()

    page.get_by_role("button", name="Submit").click()

    expect(page.get_by_text("Thanks for submitting the form")).to_be_visible()

    first_last_name = f'{first_name} {last_name}'
    expect(page.get_by_role("cell", name=first_last_name)).to_be_visible()
    expect(page.get_by_role("cell", name=gender)).to_be_visible()
    expect(page.get_by_role("cell", name=phone)).to_be_visible()
    date_str = f"{day} {calendar.month_name[int(month)+1]},{year}"
    expect(page.get_by_role("cell", name=date_str)).to_be_visible()
    expected_subjects = [s for s in (subject1, subject2, subject3) if s]
    subjects_cell = ", ".join(expected_subjects)
    if subjects_cell:
        expect(page.get_by_role("cell", name=subjects_cell)).to_be_visible()
    expect(page.get_by_role("cell", name=file_name)).to_be_visible()
    expect(page.get_by_role("cell", name=address)).to_be_visible()
    location = f"{state} {city}"
    expect(page.get_by_role("cell", name=location)).to_be_visible()

    expect(page.locator("//span[text()='© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.']")).to_be_visible()

'''Ожидания и состояния'''

def test_element_to_be_enabled(page: Page):
    page.goto('https://demoqa.com/radio-button')

    page.locator('//label[@for="yesRadio"]').is_enabled()
    page.locator('//label[@for="impressiveRadio"]').is_enabled()
    page.locator('//label[@for="noRadio"]').is_disabled()

def test_element_to_be_visible(page: Page):
    page.goto('https://demoqa.com/checkbox')

    expect(page.locator("//span[contains(text(), 'Home')]")).to_be_visible()
    page.locator("//span[contains(text(), 'Desktop')]").is_hidden()
    page.get_by_role("button", name="Toggle").first.click()
    expect(page.locator("//span[contains(text(), 'Desktop')]")).to_be_visible()

def test_element_to_be_visible_five_sec(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')

    page.locator("//button[contains(text(), 'Visible After 5 Seconds')]").is_hidden()
    page.wait_for_selector("//button[contains(text(), 'Visible After 5 Seconds')]")


def test_expect(page: Page):
    page.goto("https://demoqa.com/radio-button")
    yes_radio = page.get_by_role("radio", name="Yes")
    impressive_radio = page.get_by_role("radio", name="Impressive")
    no_radio = page.get_by_role("radio", name="No")
    expect(no_radio).to_be_disabled()  # проверяем, что не доступен
    expect(yes_radio).to_be_enabled()  # проверяем, что доступен
    expect(impressive_radio).to_be_enabled()  # проверяем, что доступен
    page.locator('[for="yesRadio"]').click()  # тут хитрый лейбл не позволяет кликнуть прямо на инпут, обращаемся по лейблу
    expect(yes_radio).to_be_checked()  # проверяем, что отмечен
    expect(impressive_radio).not_to_be_checked()  # проверяем, что не отмечен




