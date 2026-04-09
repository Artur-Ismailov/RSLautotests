from playwright.sync_api import Page, Locator
from components.base_component import BaseComponent


class SearchContent(BaseComponent):
    def __init__(self, page: Page, locator: Locator):
        super().__init__(page, locator)

    def wait_for_search_results(self, timeout = 10000):
        """Метод ждет появления хотя бы одного результата поиска внутри wrapper"""
        first_result = self.wrapper.locator(".search-container").first
        first_result.wait_for(state="visible", timeout=timeout)

    def get_results_count(self):
        """Возвращает количество элементов, соответствующих внутри wrapper."""
        results_locator = self.wrapper.locator(".search-container")
        return results_locator.count()