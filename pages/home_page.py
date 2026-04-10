from playwright.sync_api import Page
from components.header import Header
from components.menu_center import MenuCenter
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, url = "https://www.rsl.ru/")
        self._header = Header(page, page.locator("#header"))
        self._menu_center = MenuCenter(page, page.locator("#menuWrapper"))

    def get_button_search(self):
        return self._header._search_button.locator

    def fill_search_field(self, text: str):
        self._header._search_catalog.fill_text(text)

    def get_value_in_input_field(self):
        return self._header._search_catalog.get_value()

    def hover_over_button_in_menu(self, title: str):
        """Метод наводит курсор на элемент по названию"""
        self._menu_center.get_button_by_title(title).hover()

    def get_dpordown_menu_readers(self):
        return self._menu_center.get_dropdown_menu_readers()

    def click_button_menu_by_title(self, title: str):
        self._menu_center.get_button_by_title(title).click()

    def click_button_resonal_account(self):
        self._header.get_button_resonal_account().click()

    def hover_over_button_profile_menu(self):
        self._header.hover_profile_menu()

    def get_dropdown_profile_menu(self):
        return self._header.get_menu_content_profile_menu()

    def get_usermane_in_button_profile_menu(self):
        return self._header.get_name_button_profile_menu()

    def get_profile_link_in_dropdown(self):
        """Метод возвращает локатор пункта Профиль в выпадающем меню"""
        return self._header.get_profile_link_in_menu()

    def get_logout_link_in_dropdown(self):
        """Метод возвращает локатор пункта Выйти в выпадающем меню"""
        return self._header.get_logout_link_in_menu()

    def click_logout_in_dropdown(self):
        """Метод кликает по кнопке Выйти в выпадающем меню профиля"""
        self._header.get_logout_link_in_menu().click()