from playwright.sync_api import Page, Locator
from components.base_component import BaseComponent


class SearchFilter(BaseComponent):
    def __init__(self, page: Page, locator: Locator):
        super().__init__(page, locator)