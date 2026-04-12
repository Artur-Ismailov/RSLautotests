from playwright.sync_api import Page, Locator
from controls.base_control import BaseControl


class Button(BaseControl):
    """Базовый контрол для кнопок"""
    
    def __init__(self, page: Page, locator: Locator):
        super().__init__(page, locator)

    def click(self):
        """Кликает по кнопке"""
        self.locator.click()

    def is_visible(self) -> bool:
        """Проверяет видимость кнопки"""
        return self.locator.is_visible()

    def is_enabled(self) -> bool:
        """Проверяет доступность кнопки"""
        return self.locator.is_enabled()

    def get_text(self) -> str:
        """Возвращает текст кнопки"""
        return self.locator.text_content()
