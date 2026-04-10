from playwright.sync_api import Page, Locator
from components.base_component import BaseComponent
from controls.input_search_catalog import SearchCatalog
from controls.button_search import SearchButton
from controls.profile_menu import ProfileMenu


class Header(BaseComponent):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)
        self._search_catalog = SearchCatalog(page, self.wrapper.locator("input.form-control[placeholder='Поиск по электронному каталогу']"))
        self._search_button = SearchButton(page, self.wrapper.locator("input.find_submit.btn.btn-primary"))
        self._profile_menu = ProfileMenu(page, self.wrapper.locator(".menu-wrapper"))

    def get_button_resonal_account(self):
        """Кнопка для не авторизованного пользователя"""
        return self.wrapper.locator("a.label-login")

    def hover_profile_menu(self):
        self._profile_menu.hover_over()

    def get_menu_content_profile_menu(self):
        return self._profile_menu.get_menu_content()

    def get_name_button_profile_menu(self):
        """Метод возвращает локатор имени пользователя"""
        return self._profile_menu.get_username_locator()

    def get_profile_link_in_menu(self):
        """Метод возвращает локатор пункта Профиль в меню профиля"""
        return self._profile_menu.get_profile_link()

    def get_logout_link_in_menu(self):
        """Метод возвращает локатор пункта Выйти в меню профиля"""
        return self._profile_menu.get_logout_link()