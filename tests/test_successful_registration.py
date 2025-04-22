from playwright.sync_api import Page, expect
import pytest

@pytest.mark.regression  # Добавили маркировку regression
@pytest.mark.registration  # Добавили маркировку registration
def test_successful_registration(chromium_page: Page):

        # Открытие страницы с формой регистрации
        chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        # Заполнение формы регистрации
        email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')
        
        username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')
        
        password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        # Нажатие кнопки регистрации
        registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        # Проверка, что слово Dashboard присутствует на странице
        dashboard_title = chromium_page.get_by_test_id("dashboard-toolbar-title-text")
        chromium_page.wait_for_load_state('load')
        expect(dashboard_title).to_have_text("Dashboard")

        # context.storage_state(path="browser-state.json")
        # page.wait_for_timeout(5000)




    # with sync_playwright() as playwright:
    #     browser = playwright.chromium.launch(headless=False)
    #     context = browser.new_context(storage_state="browser-state.json") # Указываем файл с сохраненным состоянием
    #     page = context.new_page()

    #     page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

    #     page.wait_for_timeout(5000)