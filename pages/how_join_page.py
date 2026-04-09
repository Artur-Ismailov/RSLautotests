from playwright.sync_api import Page
from pages.base_page import BasePage


class HowJoinPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, url = "https://www.rsl.ru/ru/4readers/how-to-join")
        self._page_title_h1 = self.page.locator("h1.page-title")

    def get_page_title_h1(self):
        return self._page_title_h1