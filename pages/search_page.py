from playwright.sync_api import Page
from pages.base_page import BasePage
from components.search_content import SearchContent
from components.search_filter import SearchFilter
from components.active_filters import ActiveFilters


class SearchPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, url = "https://search.rsl.ru/ru/search")
        self._search_filter = SearchFilter(page, page.locator("#filter-container"))
        self._search_content = SearchContent(page, page.locator("#content-box"))
        self._active_filters = ActiveFilters(page, page.locator(".col-xs-11 rsl-descr"))