from playwright.sync_api import Page
from pages.base_page import BasePage
from components.search_content import SearchContent
from components.search_filter import SearchFilter


class SearchPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, url = "https://search.rsl.ru/ru/search")
        self._search_filter = SearchFilter(page, page.locator("#filter-container"))
        self._search_content = SearchContent(page, page.locator("#content-wrapper"))

    def search_results(self):
        """Метод проверяет, отображаются ли на странице результаты поиска"""
        results_count = self._search_content.get_results_count()
        return results_count > 0

    def no_search_results(self):
        """Метод проверяет, отсутсвуют ли на странице результаты поиска"""
        results_count = self._search_content.get_results_count()
        return results_count == 0

    def wait_for_search_results(self, timeout=10000):
        """Метод ждет появления хотя бы одного результата поиска внутри wrapper"""
        first_result = self._search_content.wrapper.locator(".search-container").first
        first_result.wait_for(state="visible", timeout=timeout)

    def contains_document_text(self, text: str):
        """Метод проверяет, есть ли хотя бы один элемент содержащий указанный текст"""
        matching_elements = self._search_content.wrapper.get_by_text(text, exact=False)
        return matching_elements.count() > 0