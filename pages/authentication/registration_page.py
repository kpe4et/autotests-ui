from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button

from playwright.sync_api import Page

import re


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)
        
        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration')

    def click_registration_button(self):
        self.registration_button.click()
        self.check_current_url(re.compile(".*/#/auth/registration"))
