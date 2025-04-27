from playwright.sync_api import Page, expect
import pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage
import time


@pytest.mark.parametrize("email, password, username", [('user.name@gmail.com', "username", "password") ])
@pytest.mark.regression  # Добавили маркировку regression
@pytest.mark.registration  # Добавили маркировку registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage, email, username, password):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        time.sleep(2)
        registration_page.fill_registration_form(email=email, username=username, password=password)
        registration_page.click_registration_button()
        time.sleep(2)
        # Проверка, что слово Dashboard присутствует на странице
        dashboard_page.validate_dashboard_page_title("Dashboard") # может, метод стоило назвать validate_title, раз контекст и так понятен
        time.sleep(2)
        # context.storage_state(path="browser-state.json")
        # page.wait_for_timeout(5000)




    # with sync_playwright() as playwright:
    #     browser = playwright.chromium.launch(headless=False)
    #     context = browser.new_context(storage_state="browser-state.json") # Указываем файл с сохраненным состоянием
    #     page = context.new_page()

    #     page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

    #     page.wait_for_timeout(5000)