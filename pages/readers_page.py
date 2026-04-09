from playwright.sync_api import Page
from pages.base_page import BasePage


class ReadersPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, url = "https://www.rsl.ru/ru/4readers/")
        self._page_title_h1 = self.page.locator("h1.page-title")
        self._reader_content = self.page.locator(".grid_content")
        self._breadcrumbs = self.page.locator("#breadcrumb")

    def get_page_title_h1(self):
        return self._page_title_h1

    def get_reader_subsection_elements(self):
        return self._reader_content.locator(".gridElement")

    def get_breadcrumb_home_link(self):
        return self._breadcrumbs.locator("a[rel='Home']")

    def click_reader_subsection_by_title(self, title: str):
        self.get_reader_subsection_elements().locator(f".gridElementIntroWrapperLink:has(.gridElementIntroWrapperTitle:has-text('{title}'))").click()