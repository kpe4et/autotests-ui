from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.dashboard_title = page.get_by_test_id("dashboard-toolbar-title-text")

    def validate_dashboard_page_title(self, expected_title):
        expect(self.dashboard_title).to_be_visible()
        expect(self.dashboard_title).to_have_text(expected_title)
        