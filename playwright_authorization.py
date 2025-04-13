from playwright.sync_api import sync_playwright, expect

# Запуск Playwright в синхронном режиме
with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в Headless режиме, чтобы видеть процесс)
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page() # Создаем новую вкладку

    # Переходим на страницу авторизации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    
    # Находим поля ввода для электронной почты и заполняем его
    email_input = page.get_by_test_id("login-form-email-input").locator('input')
    email_input.fill('user@gmail.com') 

    # Находим поле ввода для пароля и заполняем его
    password_input = page.get_by_test_id("login-form-password-input").locator('input')
    password_input.fill('password')

    # Находим кнопку "Login" и нажимаем ее
    login_button = page.get_by_test_id("login-page-login-button")
    login_button.click()

    # Находим сообщение об ошибке и проверяем, что оно отображается на странице
    wrong_email_or_password_alert = page.get_by_test_id("login-page-wrong-email-or-password-alert")
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text('Wrong email or password')

    # Пауза 5 секунд для демонстрации результата
    page.wait_for_timeout(5000)