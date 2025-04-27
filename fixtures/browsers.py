import pytest # Импортируем pytest
from playwright.sync_api import Page, Playwright  # Имопртируем класс страницы, будем использовать его для аннотации типов


@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно1
def chromium_page(playwright: Playwright) -> Page:  # Аннотируем возвращаемое фикстурой значение
    # Запускаем браузер
    browser = playwright.chromium.launch(headless=False)

    # Передаем страницу для использования в тесте
    yield browser.new_page()

    # Закрываем браузер после выполнения тестов
    browser.close()

# Установка состояния браузера в качестве фикстуры
@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright) -> None:
    # Инициализируем браузер и страницу
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Переходим на страницу авторизации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Вводим данные для регистрации
    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    email_input.fill("test@mail.ru")

    username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    username_input.fill("test_username")

    password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    password_input.fill("test_password")

    registration_buttton = page.get_by_test_id("registration-page-registration-button")
    registration_buttton.click()

    # Сохраняем состояние браузера
    context.storage_state(path="browser-state.json")
    browser.close()


# Фикстура для запуска тестов с сохраненным состоянием браузера
#@pytest.fixture(autouse=True) мешает
@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    yield context.new_page()
    browser.close()
