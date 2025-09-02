import pytest
from playwright.sync_api import sync_playwright
from module_6.playwright_examples.trace_ex import Tools

DEFAULT_UI_TIMEOUT = 30000  # Пример значения таймаута (30 секунд)


@pytest.fixture(scope="session")  # Браузер запускается один раз для всей сессии
def browser(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=100)  # headless=True для CI/CD, headless=False для локальной разработки
    yield browser  # yield возвращает значение фикстуры, выполнение теста продолжится после yield
    browser.close()  # Браузер закрывается после завершения всех тестов


# @pytest.fixture(scope="function")  # Контекст создается для каждого теста
# def context(browser):
#     context = browser.new_context()
#     context.tracing.start(screenshots=True, snapshots=True, sources=True)  # Трассировка для отладки
#     context.set_default_timeout(DEFAULT_UI_TIMEOUT)  # Установка таймаута по умолчанию
#     yield context  # yield возвращает значение фикстуры, выполнение теста продолжится после yield
#     context.close()  # Контекст закрывается после завершения теста

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    '''screenshots=True: Записывает скриншоты.
    snapshots=True: Записывает DOM-дерево.
    sources=True: Записывает исходный код теста.'''
    context.set_default_timeout(DEFAULT_UI_TIMEOUT)
    yield context
    #добавлено после рефакторинга, добавления трассировки
    log_name = f"trace_{Tools.get_timestamp()}.zip"
    trace_path = Tools.files_dir('playwright_trace', log_name)
    context.tracing.stop(path=trace_path)
    #добавлено после рефакторинга, добавления трассировки
    context.close()


@pytest.fixture(scope="function")  # Страница создается для каждого теста
def page(context):
    page = context.new_page()
    yield page  # yield возвращает значение фикстуры, выполнение теста продолжится после yield
    page.close()  # Страница закрывается после завершения теста