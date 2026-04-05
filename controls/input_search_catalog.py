from  playwright.sync_api import Page, Locator
from controls.base_control import BaseControl


class SearchCatalog(BaseControl):
    def __init__(self, page: Page, locator: Locator):
        super().__init__(page, locator)

    """Метод для заполнения поля ввода"""
    def fill_text(self, text: str):
        self.locator.fill(text)

    """МЕтод для получение текущего значения"""
    def get_value(self):
        return self.locator.input_value()