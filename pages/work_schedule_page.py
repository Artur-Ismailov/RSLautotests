from playwright.sync_api import Page
from pages.base_page import BasePage


class WorkSchedulePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, url = "https://www.rsl.ru/ru/4readers/schedules/")
        self._page_title_h1 = self.page.locator("h1.page-title")
        self._breadcrumbs = self.page.locator("#breadcrumb")

    def get_page_title_h1(self):
        return self._page_title_h1

    def get_breadcrumbs_container(self):
        return self._breadcrumbs

    def get_breadcrumb_readers_link(self):
        return self._breadcrumbs.locator("a:has-text('Читателям')")

    def get_breadcrumb_home_link(self):
        return self._breadcrumbs.locator("a[rel='Home']")

    def click_breadcrumb_by_title(self, title: str):
        self._breadcrumbs.locator(f"role=link[name='{title}']").click()