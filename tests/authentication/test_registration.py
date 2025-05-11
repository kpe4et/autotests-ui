import pytest
import allure
from allure_commons.types import Severity

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.routes import AppRoute
from config import settings



@pytest.mark.regression  # Добавили маркировку regression
@pytest.mark.registration  # Добавили маркировку registration
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@allure.epic(AllureEpic.LMS)
@allure.parent_suite(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:
    @allure.title("Registration with correct email, username and password")
    @allure.severity(Severity.CRITICAL)
    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.registration_form.check_visible(email='', username='', password='')
        registration_page.registration_form.fill(
            email=settings.test_user.email, 
            username=settings.test_user.username, 
            password=settings.test_user.password
        )
        registration_page.registration_form.check_visible(
            email=settings.test_user.email, 
            username=settings.test_user.username, 
            password=settings.test_user.password
        )
        registration_page.click_registration_button()
        # Проверка, что слово Dashboard присутствует на странице
        dashboard_page.dashboard_toolbar_view.check_visible()
