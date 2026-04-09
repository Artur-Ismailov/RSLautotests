from playwright.sync_api import Page, Locator
from components.base_component import BaseComponent
from controls.input_search_catalog import SearchCatalog
from controls.button_search import SearchButton
from controls.button_personal_account import PersonalAccountButton


class Header(BaseComponent):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)
        self._search_catalog = SearchCatalog(page, self.wrapper.locator("input.form-control[placeholder='Поиск по электронному каталогу']"))
        self._search_button = SearchButton(page, self.wrapper.locator("input.find_submit.btn.btn-primary"))
        self._personal_account_button = PersonalAccountButton(page, self.wrapper.locator(".menu-wrapper"))

    def get_button_resonal_account(self):
        return self.wrapper.locator("a.label-login")