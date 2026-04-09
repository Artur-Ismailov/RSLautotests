from playwright.sync_api import Page, Locator


class BasePage:
    def __init__(self, page: Page, url: str):
        self.page = page
        self.url = url

    def open(self):
        return self.page.goto(self.url)

    """Метод ожидает открытие новой вкладки по локатору"""
    def wait_for_new_tab_from_locator(self, locator: Locator):
        with self.page.expect_popup() as popup_info:
            locator.click()
        return popup_info.value

    """Ожидание загрузки новой вкладки"""
    def wait_for_page_load(self, new_page: Page, timeout: int = 30000):
        new_page.wait_for_load_state(timeout=timeout)