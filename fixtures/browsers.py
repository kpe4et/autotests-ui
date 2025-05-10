import allure
import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Page, Playwright

from pages.authentication.registration_page import RegistrationPage
from tools.playwright.pages import initialize_playwright_page


@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно1
def chromium_page(request: SubRequest,playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright, test_name=request.node.name)

# Установка состояния браузера в качестве фикстуры
@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright) -> None:
    # Инициализируем браузер и страницу
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Переходим на страницу авторизации
    registration_page = RegistrationPage(page)
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.registration_form.fill('test@mail.ru', 'username', 'test_password')
    registration_page.click_registration_button()

    # Сохраняем состояние браузера
    context.storage_state(path="browser-state.json")
    browser.close()


# Фикстура для запуска тестов с сохраненным состоянием браузера
@pytest.fixture
def chromium_page_with_state(initialize_browser_state, request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright, test_name=request.node.name, storage_state="browser-state.json")
