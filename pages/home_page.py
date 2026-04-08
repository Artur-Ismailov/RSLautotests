from playwright.sync_api import Page
from components.header import Header
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, url = "https://www.rsl.ru/")
        self._header = Header(page, page.locator("#header"))

    def fill_search_field(self, text: str):
        self._header._search_catalog.fill_text(text)

    def click_search_button(self):
        self._header._search_button.click()

    def get_value_in_input_field(self):
        return self._header._search_catalog.get_value()