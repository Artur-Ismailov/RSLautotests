from playwright.sync_api import Page, Locator
from controls.base_control import BaseControl


class ProfileMenu(BaseControl):
    def __init__(self, page: Page, locator: Locator):
        super().__init__(page, locator)
        self._menu_header = locator.locator(".menu-header")
        self._menu_content = locator.locator(".menu-content-wrapper")
        self._username_span = locator.locator(".menu-username")
        self._profile_link = locator.locator(".menu-list a[href*='profile']")
        self._logout_link = locator.locator(".menu-list a[href*='logout']")

    def hover_over(self):
        """Наводит курсор на кнопку профиля"""
        self._menu_header.hover()

    def get_menu_content(self):
        """Метод возвращает локтаор выпадающего меню"""
        return self._menu_content

    def get_username_locator(self):
        """Метод возвращает локатор имени пользователя"""
        return self._username_span

    def get_profile_link(self) -> Locator:
        """Метод возвращает локатор пункта Профиль"""
        return self._profile_link

    def get_logout_link(self) -> Locator:
        """Метод возвращает локатор пункта Выйти"""
        return self._logout_link