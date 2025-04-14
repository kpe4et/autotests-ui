from playwright.sync_api import sync_playwright, expect

# Запуск Playwright в синхронном режиме
with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в Headless режиме, чтобы видеть процесс)
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page() # Создаем новую вкладку

    # Переходим на страницу авторизации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Ожидаем, что кнопка регистрации будет неактивирована
    registration_button = page.get_by_test_id("registration-page-registration-button")
    expect(registration_button).to_be_disabled()

    email_input = page.get_by_test_id("registration-page-email-input")
    email_input.fill("user.name@gmail.com")

    username_input = page.get_by_test_id("registration-page-username-input")
    username_input.fill("username")

    password_input = page.get_by_test_id("registration-page-password-input")
    password_input.fill("password")

    # Ожидаем, что кнопка регистрации станет активной после заполнения всех полей
    expect(registration_button).to_be_enabled()

