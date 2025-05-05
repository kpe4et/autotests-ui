from typing import Pattern

from playwright.sync_api import Page, expect

class BasePage:
    # Конструктор класса, принимающий объект Page
    def __init__(self, page: Page):
        self.page = page # Присваиваем объект page атрибуту класса

    def visit(self, url: str):
        self.page.goto(url, wait_until="networkidle") # Переходим по указанному URL и ждем, пока все сетевые запросы завершатся

    def reload(self):
        self.page.reload(wait_until="domcontentloaded") # Перезагружаем страницу и ждем, пока загрузится содержимое документа

    def check_current_url(self, expected_url: Pattern[str]):
        expect(self.page).to_have_url(expected_url)