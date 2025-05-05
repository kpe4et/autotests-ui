from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link

from playwright.sync_api import Page

import re


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)
        
        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration')

        self.login_link = Link(page, 'login-page-registration-link', 'Login')

    def click_registration_button(self):
        self.registration_button.click()

    def click_login_link(self):
        self.login_link.click()
        self.check_current_url(re.compile(".*/#/auth/login"))

