from playwright.sync_api import Page, Locator
from controls.base_control import BaseControl


class SearchButton(BaseControl):
    def __init__(self, page: Page, locator: Locator):
        super().__init__(page, locator)

    """Метод для клика по кнопке"""
    def click(self):
        self.locator.click()