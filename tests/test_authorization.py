from playwright.sync_api import expect, Page
import pytest

@pytest.mark.parametrize("email, password", 
        [("user.name@gmail.com", "password"), 
        ("user.name@gmail.com", "  "), 
        ("  ", "password")]
        )
@pytest.mark.regression
@pytest.mark.authorization
# Использование фикстуры 'chromium_page', которая автоматически предоставляет готовую страницу
def test_wrong_email_or_password_authorization(chromium_page: Page, email, password):

    # Теперь страница передаётся в тест через фикстуру 'chromium_page', браузер не нужно инициализировать вручную
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    
    # Находим поля ввода для электронной почты и заполняем его
    email_input = chromium_page.get_by_test_id("login-form-email-input").locator('input')
    email_input.fill(email) 

    # Находим поле ввода для пароля и заполняем его
    password_input = chromium_page.get_by_test_id("login-form-password-input").locator('input')
    password_input.fill(password)

    # Находим кнопку "Login" и нажимаем ее
    login_button = chromium_page.get_by_test_id("login-page-login-button")
    login_button.click()

    # Находим сообщение об ошибке и проверяем, что оно отображается на странице
    wrong_email_or_password_alert = chromium_page.get_by_test_id("login-page-wrong-email-or-password-alert")
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text('Wrong email or password')

