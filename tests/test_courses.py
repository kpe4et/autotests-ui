from playwright.sync_api import sync_playwright, expect

def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input = page.get_by_test_id("registration-form-email-input").locator("input")
        email_input.fill("test@mail.ru")

        username_input = page.get_by_test_id("registration-form-username-input").locator("input")
        username_input.fill("test_username")

        password_input = page.get_by_test_id("registration-form-password-input").locator("input")
        password_input.fill("test_password")

        registration_buttton = page.get_by_test_id("registration-page-registration-button")
        registration_buttton.click()

        context.storage_state(path="browser-state.json")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_title = page.get_by_test_id("courses-list-toolbar-title-text")
        expect(courses_title).to_have_text("Courses")

        course_results_icon = page.get_by_test_id("courses-list-empty-view-icon")
        expect(course_results_icon).to_be_visible()

        course_results_title = page.get_by_test_id("courses-list-empty-view-title-text")
        expect(course_results_title).to_have_text("There is no results")

        course_results_info = page.get_by_test_id("courses-list-empty-view-description-text")
        expect(course_results_info).to_have_text("Results from the load test pipeline will be displayed here")