from playwright.sync_api import Page, Locator
from components.base_component import BaseComponent


class ActiveFilters(BaseComponent):
    def __init__(self, page: Page, locator: Locator):
        super().__init__(page, locator)

    """Метод проверяет, отображается ли указанный текст в фильтрации"""
    def contains_active_filter_text(self, text: str):
        filter_element = self.wrapper.locator(".rsl-filter-badge").get_by_text(text).first
        filter_element.wait_for(state="visible", timeout=50000)
        return filter_element.count() > 0