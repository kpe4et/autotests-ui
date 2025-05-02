from playwright.sync_api import expect, Page
import pytest

from pages.login_page import LoginPage


@pytest.mark.parametrize("email, password", 
        [("user.name@gmail.com", "password"), 
        ("user.name@gmail.com", "  "), 
        ("  ", "password")]
        )
@pytest.mark.regression
@pytest.mark.authorization
# Использование фикстуры 'chromium_page', которая автоматически предоставляет готовую страницу
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    login_page.login_form.check_visible(email='', password='') # проверим, что форма авторизации отображается и не заполнена
    login_page.login_form.fill(email=email, password=password)
    login_page.login_form.check_visible(email=email, password=password)  # проверим, что форма авторизации отображается и заполнена
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()
