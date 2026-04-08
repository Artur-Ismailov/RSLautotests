from playwright.sync_api import Page, Locator
from components.base_component import BaseComponent


class SearchContent(BaseComponent):
    def __init__(self, page: Page, locator: Locator):
        super().__init__(page, locator)

    """Метод ждет появления хотя бы одного результата поиска внутри wrapper"""
    def wait_for_search_results(self, timeout: float = 30000):
        first_result = self.wrapper.locator(".search-container").first
        first_result.wait_for(state="visible", timeout=timeout)

    """Метод проверяет, есть ли хотя бы один элемент содержащий указанный текст"""
    def contains_document_text(self, text: str):
        matching_elements = self.wrapper.get_by_text(text, exact=False)
        return matching_elements.count() > 0