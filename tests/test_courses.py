from playwright.sync_api import sync_playwright, expect, Page
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
        
        chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_title = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
        expect(courses_title).to_have_text("Courses")

        course_results_icon = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
        expect(course_results_icon).to_be_visible()

        course_results_title = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
        expect(course_results_title).to_have_text("There is no results")

        course_results_info = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
        expect(course_results_info).to_have_text("Results from the load test pipeline will be displayed here")
