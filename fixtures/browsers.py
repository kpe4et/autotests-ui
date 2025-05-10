import allure
import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Page, Playwright

from pages.authentication.registration_page import RegistrationPage


@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно1
def chromium_page(request: SubRequest,playwright: Playwright) -> Page:
    # Запускаем браузер
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(record_video_dir='./videos')
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    # Передаем страницу для использования в тесте
    yield browser.new_page()

    # Закрываем браузер после выполнения тестов. request.node.name содержит название текущего автотеста
    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    browser.close()

    allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', attachment_type='application/zip')
    allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)

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
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json", record_video_dir='./videos')
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    
    yield context.new_page()
    
    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    browser.close()

    allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', attachment_type='application/zip')
    allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)
