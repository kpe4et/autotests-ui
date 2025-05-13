from typing import Pattern

from playwright.sync_api import Page, expect
import allure

from tools.logger import get_logger

logger = get_logger("BASE_PAGE")


class BasePage:
    # Конструктор класса, принимающий объект Page
    def __init__(self, page: Page):
        self.page = page # Присваиваем объект page атрибуту класса

    def visit(self, url: str):
        step = f'Opening the url "{url}"'

        with allure.step(step):
            logger.info(step)
            self.page.goto(url, wait_until="networkidle") # Переходим по указанному URL и ждем, пока все сетевые запросы завершатся

    def reload(self):
        step = f'Reloading page with url "{self.page.url}"'

        with allure.step(step):
            logger.info(step)
            self.page.reload(wait_until="domcontentloaded") # Перезагружаем страницу и ждем, пока загрузится содержимое документа

    def check_current_url(self, expected_url: Pattern[str]):
        step = f'Checking current url against "{expected_url.pattern}"'

        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)
