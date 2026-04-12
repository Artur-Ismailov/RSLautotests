from playwright.sync_api import Page, Locator
from controls.base_control import BaseControl


class Link(BaseControl):
    """Базовый контрол для ссылок"""
    
    def __init__(self, page: Page, locator: Locator):
        super().__init__(page, locator)

    def click(self):
        """Кликает по ссылке"""
        self.locator.click()

    def is_visible(self) -> bool:
        """Проверяет видимость ссылки"""
        return self.locator.is_visible()

    def get_href(self) -> str:
        """Возвращает атрибут href ссылки"""
        return self.locator.get_attribute("href")

    def get_text(self) -> str:
        """Возвращает текст ссылки"""
        return self.locator.text_content()
