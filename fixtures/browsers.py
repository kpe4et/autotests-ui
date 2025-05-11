import allure
import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Page, Playwright
from config import settings

from pages.authentication.registration_page import RegistrationPage
from tools.playwright.pages import initialize_playwright_page
from tools.routes import AppRoute


@pytest.fixture(params=settings.browsers)  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно1
def chromium_page(request: SubRequest,playwright: Playwright) -> Page:
    yield from initialize_playwright_page(
        playwright, 
        test_name=request.node.name, 
        browser_type=request.param
    )

# Установка состояния браузера в качестве фикстуры
@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright) -> None:
    # Инициализируем браузер и страницу
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    # Переходим на страницу авторизации
    registration_page = RegistrationPage(page)
    registration_page.visit(AppRoute.REGISTRATION)
    registration_page.registration_form.fill(settings.test_user.email, settings.test_user.username, settings.test_user.password)
    registration_page.click_registration_button()

    # Сохраняем состояние браузера
    context.storage_state(path=settings.browser_state_file)
    browser.close()


# Фикстура для запуска тестов с сохраненным состоянием браузера
@pytest.fixture(params=settings.browsers)
def chromium_page_with_state(initialize_browser_state, request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(
        playwright, 
        test_name=request.node.name, 
        storage_state=settings.browser_state_file, 
        browser_type=request.param
    )
