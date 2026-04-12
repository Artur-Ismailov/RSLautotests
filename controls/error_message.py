from playwright.sync_api import Page, Locator
from controls.base_control import BaseControl


class ErrorMessage(BaseControl):
    """Базовый контрол для сообщений об ошибках"""
    
    def __init__(self, page: Page, locator: Locator):
        super().__init__(page, locator)

    def is_visible(self) -> bool:
        """Проверяет видимость сообщения об ошибке"""
        return self.locator.is_visible()

    def get_text(self) -> str:
        """Возвращает текст сообщения об ошибке"""
        return self.locator.text_content()

    def wait_for_visible(self, timeout: float = 5000):
        """Ожидает появления сообщения об ошибке"""
        self.locator.wait_for(state="visible", timeout=timeout)
