from playwright.sync_api import Page, Locator
from controls.base_control import BaseControl


class Input(BaseControl):
    """Базовый контрол для полей ввода"""
    
    def __init__(self, page: Page, locator: Locator):
        super().__init__(page, locator)

    def fill(self, text: str):
        """Заполняет поле ввода текстом"""
        self.locator.fill(text)

    def clear(self):
        """Очищает поле ввода"""
        self.locator.clear()

    def get_value(self) -> str:
        """Возвращает текущее значение поля"""
        return self.locator.input_value()

    def is_visible(self) -> bool:
        """Проверяет видимость поля"""
        return self.locator.is_visible()
