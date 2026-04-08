from playwright.sync_api import Page, Locator
from components.base_component import BaseComponent
from controls.input_search_catalog import SearchCatalog
from controls.button_search import SearchButton


class Header(BaseComponent):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)
        self._search_catalog = SearchCatalog(page, self.wrapper.locator("input.form-control[placeholder='Поиск по электронному каталогу']"))
        self._search_button = SearchButton(page, self.wrapper.locator("input.find_submit.btn.btn-primary"))

    def get_search_catalog(self):
        return self._search_catalog