import pytest
from module_4.Cinescope.utils.data_generator import DataGenerator
from module_7.Cinescope_ui.classes_page_object import CinescopeRegister as CinescopRegisterPage
from playwright.sync_api import sync_playwright, Page

@pytest.fixture
def registered_user():
    with sync_playwright() as playwright:
        full_name = DataGenerator.generate_random_name()
        email = DataGenerator.generate_random_email()
        password = DataGenerator.generate_random_password()

        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        register_page = CinescopRegisterPage(page)
        register_page.open()
        register_page.register(fullname=full_name, email=email, password=password, confirm_password=password)

        register_page.wait_redirect_to_login_page()
        register_page.check_allert()

        return {'email': email, 'password': password}


