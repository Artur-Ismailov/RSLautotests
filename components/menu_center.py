from playwright.sync_api import Page, Locator
from components.base_component import BaseComponent


class MenuCenter(BaseComponent):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def get_button_by_title(self, title: str):
        """Метод находит элемент по названию"""
        return self.wrapper.get_by_text(title)

    def get_dropdown_menu_readers(self):
        return self.wrapper.locator("ul.local_menu.menu_readers")